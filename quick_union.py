class QuickUnion:
  
  def __init__(self, n):
    self.table = list(range(n))
    self.sz = [1] * n 

  def _findRoot(self, index):
    while self.table[index] != index:
      self.table[index] = self.table[self.table[index]]
      index = self.table[index]
    return index 

  def union(self, a, b):
    i = self._findRoot(a)
    j = self._findRoot(b)
    if i == j: return
    if self.sz[j] >= self.sz[i]:
      self.table[i] = j
      self.sz[j] += self.sz[i]
    else:
      self.table[j] = i
      self.sz[i] += self.sz[j]
      
  def connected(self, a, b):
    return self._findRoot(a) == self._findRoot(b)
    

test = QuickUnion(10)
test.union(2,5)
test.union(5,7)
test.union(2,3)
test.union(1,6)
test.union(8,6)
test.union(8,7)
print(test.connected(2,7))
print(test.connected(1,2))
print(test.table)
print(test.sz)