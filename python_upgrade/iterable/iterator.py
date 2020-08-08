


class myIterator(object):
  def  __init__(self):
    self.arr = [1,2,3,4,5,6,7,8]
    self.index = 0
  
  def __iter__(self):
    return self

  def next1(self):
    print("next: ", self.index)
    while (self.index < len(self.arr)): 
      val = self.arr[self.index]
      self.index += 2
      return val
    raise StopIteration

  def next(self):
    print("next:", self.index)
    try:
      val = self.arr[self.index]
      self.index += 2
      return val
    except IndexError:
      raise StopIteration
 
my_iterator = myIterator()
for i in my_iterator:
  print(i)
