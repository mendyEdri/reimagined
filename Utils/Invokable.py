class Invokable:
  def __init__(self, model):
    self.model = model
  
  def invoke_llm(self, systemPrompt, userPrompt):
    response = self.model.chat.completions.create(
    model=self.modelName,
    temperature=0.0,
    messages=[
        {
          "role": "system",
          "content": systemPrompt
        },
        {
          "role": "user",
          "content": userPrompt
        }
      ],
      # response_format={"type": "json_object"}
    )
    return response