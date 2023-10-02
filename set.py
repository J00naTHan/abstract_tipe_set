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
      if val is not False and val is not None:
        self.insert(val)
        pset.delete(key)

  def intersection(self, pset):
    pass

  def difference(self, pset):
    pass
