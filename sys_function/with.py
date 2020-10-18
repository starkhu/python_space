class Cls:
  def __exit__(self, type, value, trace):
    print("__exit__")
    print("type: ", type)
    print("value: ", value)
    print("trace: ", trace)
  def __enter__(self):
    print("__enter__")
    return self
  def exit(self, *kargs, **kwargs):
    print("__exit")
  def enter(self):
    print("__enter")
  def do_something(self):
    assert 1>2
    print("do something")


def get_class():
  my_cls = Cls()
  return my_cls

with get_class() as cls:
  get_class().do_something()
  cls.do_something()
