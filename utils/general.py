def get_class_properties(cls):
  """Gets all class attributes as a list."""
  return [attr for attr in dir(cls) if not attr.startswith("__")]