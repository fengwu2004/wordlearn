class Singleton(object):
  _instance = None
  def __new__(cls, *args):
    if not isinstance(cls._instance, cls):
        cls._instance = object.__new__(cls, *args)
    return cls._instance