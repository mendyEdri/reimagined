from abc import ABC, abstractmethod

class AbstractAgent:
  modelName = "llama3-70b-8192"

  def __init__(self, model):
    self.model = model

  def path_exists(self, path):
    try:
        with open(path) as f:
            return True
    except IOError:
        return False
  
  @property
  @abstractmethod
  def content(self):
    return self.llmResponse.choices[0].message.content

  @abstractmethod
  def invoke(self):
    self.llmResponse = self.model.chat.completions.create(
      model=self.modelName,
      temperature=0.0,
      messages=[
         {
            "role": "system",
            "content": self.systemPrompt()
         },
         {
            "role": "user",
            "content": self.prompt()
         }
      ],
      # response_format={"type": "json_object"}
    )
    return self.llmResponse
  
  @abstractmethod
  def update(self, update):
    self.llmResponse = self.model.chat.completions.create(
      model=self.modelName,
      temperature=0.0,
      messages=[
         {
            "role": "user",
            "content": update
         },
         {
            "role": "system",
            "content": "Only update the file as necessary and requested, return the complete version with the your changes" + self.read()
         },
      ],
    )
    return self.llmResponse
  
  @abstractmethod
  def test(self, test):
    self.llmResponse = self.model.chat.completions.create(
      model=self.modelName,
      temperature=0.0,
      messages=[
         {
            "role": "system",
            "content": "This code needs to be test according to the user request. code:" + self.read()
         },
         {
            "role": "user",
            "content": test
         },
      ],
    )

    testFile = self.fileName() + '.test.ts'
    if not self.path_exists(testFile):
        with open(testFile, 'w') as file:
          file.write('')       
          with open(testFile, 'r') as readFile:
            first_line = readFile.readline()
            if first_line != 'lock':
              with open(testFile, 'w') as file:
                file.write(self.content)
            
    return self.llmResponse

  @abstractmethod
  def write(self):
      if not self.path_exists(self.fileName()):
          with open(self.fileName(), 'w') as file:
                file.write('')            
      with open(self.fileName(), 'r') as readFile:
        first_line = readFile.readline()
      if first_line != 'lock':
        with open(self.fileName(), 'w') as file:
          file.write(self.content)

  @abstractmethod
  def read(self):
     if self.path_exists(self.fileName()):
        with open(self.fileName(), 'r') as readFile:
          return readFile.read()

  @property
  @abstractmethod
  def role(self):
    return "You are a Software Architecture, following SOLID principles"

  @property
  @abstractmethod
  def language(self):
    return 'Typescript'

  @abstractmethod
  def fileName(self):
    pass

  @abstractmethod
  def prompt(self):
    pass

  @abstractmethod
  def systemPrompt(self):
    return f"""
    Think Step-by-step:

    The architecture:
    App Factory, which is the app entrypoint.
    
    Our Architecture:
    <app-architecture>
    1. Client - a pice of code that usually used to have concrete implementation
        of a code that could be replaceable. 
        for example, FirebaseUsersClient which implements IUserClient, 
        and has a concrete implementation of connecting to the DB with firebase package.
    2. Service - usually get the client injected and has simple methods using the client. 
        for example, LoginService implements ILoginService, gets in the constructor IUserClient, 
        and have a few methods such as isLoggedIn, getSessionToken etc, which uses the client provided to expose this methods.
    3. Domain - the business logic for the app. sometimes it gets a Service in the 
                constructor and uses it to implement a business-domain logic.
                for example, it gets in the constructor ILoginService, and use it in domain-specific methods such as, 
                loginWithToken, logout, createUser, etc.
    4. Controllers - A class usually holds a few domains, related to the same area in the app.
                    for example, in a todo app, ReminderController - where all the Reminders related code, UIController, 
                    for all domains related only to UI changes etc.

    The Factory responsibility are:
    1. To initialize all clients
    2. To initialize all services
    3. To inject the needed clients to services
    4. To initialize domains and pass the necessary services.
    5. To prefetch anything needed before the app loads
    6. To implement the return value of the app (IApp for example) which has all needed controllers and domains, the app needed.
    <app-architecture>

    <programming-language>
      {self.language}
    </programming-language>

    <formatting>
      The code must be a runnable {self.language} code.
      * You must not return any formatting special charecters.
      * You must not add backticks at the beggining or end of the code.
      * Reiterate to see if your answer includes ``` and remove them.
      * Never export default
      * always export classes, for example, export class SomeClass etc.
    </formatting>

    <reasoning>
      You must think in a step-by-step manner.
      Make sure you break down the requests to tasks and execute it correctly. 
    </reasoning>
    
    Always create an interface for the code you generate.
    You must response only with the code.
    """