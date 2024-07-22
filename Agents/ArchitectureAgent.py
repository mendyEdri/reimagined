from Agents.AbstractAgent import AbstractAgent

class ArchitectureAgent(AbstractAgent):
  
  def __init__(self, model):
    self.model = model

  def fileName(self):
    return 'AppFactory.ts'
  
  def prompt(self):
    return 'Create a empty factory based on the given architecture and instructions. do not use unnecessary implementation.'
