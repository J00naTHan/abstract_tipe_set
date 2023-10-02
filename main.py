from hashTable import hashTable


class Set(hashTable):
  def __init__ (self, size, patFactor = 0):
    super().__init__(size)
    self.patFactor = self.pattern = patFactor

  def insert(self, val):
    if self.__getitem__(self.pattern) is None:
      s = self.search(self.pattern)
      if s != val:
        inserted = self.__setitem__(self.pattern, val)
        self.pattern += 2
        return inserted
      else:
        print("O valor inserido já existe!")
        return False
    else:
      print(f"\nNão é possível adicionar dois ou mais itens com a chave: {self.pattern}!")
      return False

  def delete(self, key):
    if self.__getitem__(key):
      delItem = self.__delitem__(key)
      return delItem
    else:
      return 0
  
  def search(self, key):
    if self.__getitem__(key) is not False:
      return self.__getitem__(key)
    else:
      return False

  def union(self, pset):
    for key in range(pset.patFactor, pset.size + 1, 2):
      val = pset.search(key)
      print(key, val)
      if val is not False and val is not None:
        self.insert(val)
        pset.delete(key)
      else:
        continue
    print(set.table)
    return self

  def intersection(self, pset):
    pass

  def difference(self, pset):
    pass

if __name__ == "__main__":
  set = Set(10)
  pset = Set(10, 1)

  pset.insert(3)
  pset.insert(10)

  print("Testes de Insert:")
  print("pset", "1", pset.search("1"))
  print("pset", "3", pset.search("3"))
  
  set.insert(5)
  set.insert(7)
  set.insert(9)
  
  for key in range(set.patFactor, set.size + 1, 2):
    if set.search(key) is not None:
      print("set", key, set.search(key))

  p = pset.search("1")  
  s = set.search("0")

  print("\nTestes de Search:")
  print(p, s)

  print("")
  u = set.union(pset)
  
