class QuickUnion:
  
  def __init__(self, n):
    self.table = list(range(n))

  def _findRoot(self, index):
    while self.table[index] != index:
      index = self.table[index]
    return index 

  def union(self, a, b):
    self.table[self._findRoot(a)] = self._findRoot(b)
    
  def connected(self, a, b):
    return self._findRoot(a) == self._findRoot(b)
    


test = QuickUnion(10)
test.union(2,5)
test.union(5,7)
test.union(2,3)
test.union(1,6)
print(test.connected(2,7))
print(test.connected(1,2))
print(test.table)