class QuickFind:
  
  def __init__(self, n):
    self.table = list(range(n))

  def union(self, a, b):
    if self.table[a] != self.table[b]:
      temp = self.table[a]
      for i,x in enumerate(self.table):
        if x == temp:
          self.table[i] = self.table[b]

  def connected(self, a, b):
    return self.table[a] == self.table[b]
    
test = QuickFind(10)
test.union(2,5)
test.union(5,7)
test.union(2,3)
test.union(1,6)
print(test.connected(2,7))
print(test.connected(1,2))
print(test.table)