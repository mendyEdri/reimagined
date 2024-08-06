from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain.agents import AgentExecutor, create_tool_calling_agent
from langchain_core.messages import SystemMessage, HumanMessage

class GraphAgentExecutor:
    
    default_llm = ChatOpenAI(model='gpt-4o-mini', temperature=0)

    def __init__(self, llm=default_llm, tools=[], system="", next_options=[], variable_placeholder="messages"):
        llm = ChatOpenAI(model='gpt-4o-mini', temperature=0)

        prompt = ChatPromptTemplate.from_messages([
            SystemMessage(content=system), 
            MessagesPlaceholder(variable_name=variable_placeholder), 
            SystemMessage(content=f"""
                You are a supervisor tasked with managing a conversation between the 
                following workers: {next_options}. Given the following user request,
                respond with the worker to act next. Each worker will perform a
                task and respond with their results and status. When finished,
                respond with FINISH.
                """),
            MessagesPlaceholder(variable_name="agent_scratchpad")
        ])

        agent = create_tool_calling_agent(llm, tools, prompt)
        self.model = AgentExecutor(agent=agent, tools=tools, verbose=True)

    def should_continue(self, state):
        print(state)
        
        