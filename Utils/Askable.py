class Askable:
  def __init__(self, model):
    self.model = model
  
  def ask_llm(self, fileContent, question):
    return self.model.chat.completions.create(
      model=self.modelName,
      temperature=0.5,
      messages=[
         {
            "role": "system",
            "content": "Read the code and answer to the user questions." + fileContent
         },
         {
            "role": "user",
            "content": question
         },
      ],
    )