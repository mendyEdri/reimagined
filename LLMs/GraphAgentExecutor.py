from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain.agents import AgentExecutor, create_tool_calling_agent
from langchain_core.messages import SystemMessage, HumanMessage

class GraphAgentExecutor:

    default_llm = ChatOpenAI(model='gpt-4o-mini', temperature=0)

    def get_agent(self, llm=default_llm, tools=[], system="", next_options=[], variable_placeholder="messages"):
        llm = ChatOpenAI(model='gpt-4o-mini', temperature=0)

        prompt = ChatPromptTemplate.from_messages([
            SystemMessage(content=system), 
            MessagesPlaceholder(variable_name=variable_placeholder), 
            SystemMessage(content=f"""
                Given the conversation above, who should act next?
                Or should we FINISH? select one of: {next_options}
                """),
            MessagesPlaceholder(variable_name="agent_scratchpad")
        ])

        agent = create_tool_calling_agent(llm, tools, prompt)
        model = AgentExecutor(agent=agent, tools=tools, verbose=True)

        return model
