class Updatable:
  def __init__(self, model):
    self.model = model

  def update_llm(self, update, systemPrompt, file):
    return self.model.chat.completions.create(
      model=self.modelName,
      temperature=0.0,
      messages=[
         {
            "role": "user",
            "content": update
         },
         {
            "role": "system",
            "content": f"""
              Only update the file as necessary and requested, return the complete version with the your changes.
              
              Instructions:
              {systemPrompt}

              Code:
              {file}
              
            """ 
         },
      ],
    )