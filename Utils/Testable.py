class Testable:
  def __init__(self, model):
    self.model = model

  def content(self):
    return self.llmResponse.choices[0].message.content

  def role(self):
    return f"""
    You are senior software engineer creates unit tests. 
    
    Provide only the raw code without any markdown formatting, backticks, or language specifications. 
    The code should start directly with the first line of {self.language} and end with the last line of code.
    Make sure the code is syntactically correct and can be compiled without errors. 
    
    This code needs to be test according to the user request. code:
    
    """
  
  def test_llm(self, testCase, fileContent, fileName):
    self.llmResponse = self.model.chat.completions.create(
      model=self.modelName,
      temperature=0.0,
      messages=[
         {
            "role": "system",
            "content": self.role() + fileContent
         },
         {
            "role": "user",
            "content": testCase
         },
      ],
    )

    testFile = fileName + '.test.ts'
    if not self.path_exists(testFile):
        with open(testFile, 'w') as file:
          file.write('')       
          with open(testFile, 'r') as readFile:
            first_line = readFile.readline()
            if first_line != 'lock':
              with open(testFile, 'w') as file:
                file.write(self.content)