from langchain_core.messages import SystemMessage, HumanMessage
class Invokable:
    def __init__(self, model):
        self.model = model
        self.modelName = model.name  # Assume model has a name attribute

    def invoke_llm(self, systemPrompt, userPrompt):    
        messages = [SystemMessage(content=systemPrompt), HumanMessage(content=userPrompt)]
        
        # Construct the kwargs dictionary
        kwargs = {
            "model": self.modelName,
            "temperature": 0.0,
            "messages": messages,
        }
        self.model.bind(kwargs=kwargs)

        # Call the model's completion method with the constructed kwargs
        try:
            response = self.model.invoke(messages)
            return response
        except Exception as e:
            print(f"An error occurred: {e}")
            return None