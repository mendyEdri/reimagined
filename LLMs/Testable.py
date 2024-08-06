class Testable:
  def __init__(self, model):
    self.model = model

  def content(self):
    return self.llmResponse.choices[0].message.content

  def getRole(self, content, fileName):
    return f"""
    *** Think step-by-step, and give your self tasks based on the following: ***

    You are senior software engineer creates unit tests.
    
    - Provide only the raw unit test code without any markdown formatting, backticks, or language specifications. 
    - The code should start directly with the first line of the code and end with the last line of code.
    - Make sure the code is syntactically correct and can be compiled without errors. 
    - No need to re-create the code content I gave you.
    - You can assume you can import the file to test, from the same directory with the file name - {fileName}

    The code you should create the tests for it,
    Code:
    {content}
    """
  
  def test_llm(self, testCase, fileContent, fileName):
    self.llmResponse = self.model.chat.completions.create(
      model=self.modelName,
      temperature=0.0,
      messages=[
         {
            "role": "system",
            "content": self.getRole(fileContent, fileName)
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
      if first_line != '// lock':
          with open(testFile, 'w') as file:
            file.write(self.content)