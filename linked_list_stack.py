class Stack:

  class Node:
    
    def __init__(self, item=None, next_obj=None):
      self.item = item
      self.next_obj = next_obj
      
    def __repr__(self):
      return self.item.__str__()

  def __init__(self):
    self.header = self.Node()

  def pop(self):
    if self.isEmpty(): return None
    result = self.header.next_obj
    self.header.next_obj = self.header.next_obj.next_obj
    return result

  def push(self, obj):
    oldFirst = self.header.next_obj
    newFirst = self.Node(obj)
    newFirst.next_obj = oldFirst
    self.header.next_obj = newFirst

  def isEmpty(self):
    return self.header.next_obj is None  
    
# test client   
stack = Stack()
test = "be to not to - or be - - - - -"
for i in test.split():
  if i == '-':
    print(stack.pop(),' ', end='')
  else: stack.push(i)