from hashTable import hashTable


class Set(hashTable):
  def __init__ (self, size):
    super().__init__(size)

  def insert(self, val, patFactor = 0):
    pattern = 0 if patFactor == 0 else 1
    if self.__getitem__(pattern) is None:
      inserted = self.__setitem__(pattern, val)
      pattern += 2
      return inserted
    else:
      print("\nNão é possível adicionar dois itens com a mesma chave!")
      return False

  def delete(self, key):
    if self.__getitem__(key):
      delItem = self.__delitem__(key)
      return delItem
    else:
      return 0
  
  def search(self, key):
    key = str(key)
    if self.__getitem__(key):
      return self.__getitem__(key)
    else:
      return 0

  def union(self, pset):
    for x in range(pset.size):
      item = self.search(x)
      self.insert(item)

  def intersection(self, pset):
    pass

  def difference(self, pset):
    pass

if __name__ == "__main__":
  set = Set(50)
  pset = Set(10)
  set.insert(5)
  pset.insert(10, 1)
  for x in list(range(set.size * 2, 2)):
    s = set.search(x)
    print(f"Item: {s}")
  s = set.delete("10")
  print(s)
