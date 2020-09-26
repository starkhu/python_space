

'''
case 1
import time
def logging_time(func):
  start_time = time.time()
  func()
  end_time = time.time()
  print("the execution of the function is {} seconds".format(end_time-start_time))


def hello_func():
  print("hello")

# logging_time(hello_func)
'''
# case 2
import time
from functools import wraps
def logging_time(func):
  @wraps(func)
  def wrapper():
    start_time = time.time()
    func()
    end_time = time.time()
    print("the execution of the function {} is {} seconds".format(func.__name__, end_time-start_time))
  return wrapper

@logging_time
def hello_func():
  print("hello")

hello_func()
print hello_func.__name__
'''
# case 3
import time
def logging_time(func):
  def wrapper(*args, **kwargs):
    start_time = time.time()
    func(*args, **kwargs)
    end_time = time.time()
    print("the execution of the function is {} seconds".format(end_time-start_time))
  return wrapper

@logging_time
def hello_func(caller="caller"):
  print("hello, {}".format(caller))

hello_func("Caller")
'''
'''
# case 4
import time
def logging_time(python_version="2"):
  def inner_func(func):
    print("python version is: {}".format(python_version))
    def wrapper(*args, **kwargs):
      start_time = time.time()
      func(*args, **kwargs)
      end_time = time.time()
      print("the execution of the function is {} seconds".format(end_time-start_time))
    return wrapper
  return inner_func
  

@logging_time(python_version="2.7")
def hello_func(caller="caller"):
  print("hello, {}".format(caller))

hello_func("Caller")
'''

'''
import time
class logging_time(object):
  def __init__(self, func):
    self.func = func
  
  def __call__(self, *args, **kwargs):
    start_time = time.time()
    self.func(*args, **kwargs)
    end_time = time.time()
    print("the execution of the function is {} seconds".format(end_time-start_time))

@logging_time
def hello_func(caller="caller"):
  print("hello, {}".format(caller))

hello_func("Caller")
'''

'''
import time
class logging_time(object):
  def __init__(self, python_version):
    self.python_version = python_version
  
  def __call__(self, func):
    print("python version is: {}".format(self.python_version))
    def wrapper(*args, **kwargs):
      start_time = time.time()
      func(*args, **kwargs)
      end_time = time.time()
      print("the execution of the function is {} seconds".format(end_time-start_time))
    return wrapper

@logging_time(python_version="2.7")
def hello_func(caller="caller"):
  print("hello, {}".format(caller))

hello_func("Caller")
'''
