import operator
import random
from IPython.display import Image
from langchain_openai import ChatOpenAI
from langgraph.checkpoint.aiosqlite import AsyncSqliteSaver
from langgraph.prebuilt import ToolNode
from langgraph.graph import StateGraph, END
from typing import TypedDict, Annotated
from langchain_core.messages import AnyMessage, SystemMessage

from utils.files import write_file_tool, read_file_tool

thread_id = 1

class AgentState(TypedDict):
    messages: Annotated[list[AnyMessage], operator.add]
    code: str
    docs: str

class Agents:
    Planner = "planner"
    InterfaceWriter = 'interface_code_writer'
    CodeWriter = 'code_writer'
    Tools = "tools"
    DocumentationWriter = 'docs_writer'

class ClientGraph():
    def __init__(self):
        self.memory = AsyncSqliteSaver.from_conn_string(":memory:")

    def tools(self):
        return [write_file_tool, read_file_tool]

    @property
    def state(self):
        return self.graph

    def make_graph(self):
        self.model = ChatOpenAI(model='gpt-4o-mini').bind_tools(self.tools)
        tool_node = ToolNode(self.tools)
        self.graph = StateGraph(AgentState)
        self.graph.add_node(Agents.Planner, self.planner_llm)
        self.graph.add_node(Agents.CodeWriter, self.code_writer_llm)
        self.graph.add_node(Agents.Tools, tool_node)
        self.graph.add_node(Agents.DocumentationWriter, self.documentation_writer_llm)
        self.add_nodes()

        self.graph.add_conditional_edges(Agents.Planner, self.should_continue)

        self.graph.add_edge(Agents.CodeWriter, Agents.Planner)
        self.graph.add_edge(Agents.Tools, Agents.Planner)
        self.graph.add_edge(Agents.DocumentationWriter, Agents.Planner)
        self.add_edges()
        
        self.graph.set_entry_point(Agents.Planner)

        self.graph = self.graph.compile(self.memory)
        return self.graph
    
    def start(self, messages):
        print("start:", messages)
        return self.graph.invoke(
            {"messages": messages},
            config={"configurable": {"thread_id": random.randint(1, 10)}}
        )

    def should_continue(self, state: AgentState):
        messages = state['messages']
        last_message = messages[-1]
        print("*** should continue ***", last_message)
        if last_message.tool_calls:
            return Agents.Tools
        elif not 'code' in state:
            return Agents.CodeWriter
        elif not 'docs' in state:
            return Agents.DocumentationWriter
        else: 
            return END

    def planner_llm(self, state):
        print("*** planner_llm ***")
        messages = state['messages']
        response = self.model.invoke(messages)
        self.llmResponse = [response]
    
        return {"messages": self.llmResponse}

    def code_writer_llm(self, state):
        print("*** Code Writer ***")
        messages = state['messages']
        response = self.model.invoke(messages)
        self.llmResponse = [response]
        return {"code": self.llmResponse}
    
    def documentation_writer_llm(self, input=''):
        print("*** Docs Writer ***")
        system = "You are a documentation writer. you read the code and write description above so llm can read it and understand the code responsibility. use tools to read file and write description"
        messages = [SystemMessage(content=system)]
        response = self.model.invoke(messages)
        self.llmResponse = response
        return {"docs": response}

    def draw_graph(self):
        return Image(self.graph.get_graph().draw_png())