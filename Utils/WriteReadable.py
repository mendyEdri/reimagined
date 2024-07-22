class WriteReadable:
  def __init__(self, model):
    self.model = model

  def path_exists(self, path):
    try:
        with open(path) as f:
            return True
    except IOError:
        return False

  def write_code(self, fileName, content):
    if not self.path_exists(fileName):
        with open(fileName, 'w') as file:
              file.write('')            
    with open(fileName, 'r') as readFile:
      first_line = readFile.readline()
      if first_line != 'lock':
        with open(fileName, 'w') as file:
          file.write(content)
  
  def read_code(self, fileName):
    if self.path_exists(fileName):
        with open(fileName, 'r') as readFile:
          return readFile.read()
  