from hashTable import hashTable


class Set(hashTable):
  def __init__ (self, size):
    super().__init__(size)
    self.pattern = 0

  def insert(self, val):
    if self.__getitem__(self.pattern) is None:
      s = self.search(self.pattern)
      if s != val:
        inserted = self.__setitem__(self.pattern, val)
        self.pattern += 1
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
      return False
  
  def search(self, key):
    if self.__getitem__(key) is not False:
      return self.__getitem__(key)
    else:
      return False

  def union(self, pset, newSize = 10):
    union = Set(newSize)
    for key in range(self.size):
      val = self.search(key)
      if val is not False and val is not None:
        union.insert(val)
    for key in range(pset.size):
      val = pset.search(key)
      if val is not False and val is not None and val not in union.table:
        union.insert(val)
    return union

  def intersection(self, pset, newSize = 10):
    intersection = Set(newSize)
    aux = hashTable(self.size)
    for key in range(self.size):
      val = self.search(key)
      if val is not False and val is not None:
        aux.__setitem__(key, val)
    for key in range(pset.size):
      val = pset.search(key)
      if val is not False and val is not None:
        for i in range(aux.size):
          otherVal = aux.__getitem__(i)
          if val == otherVal:
            intersection.insert(val)
    return intersection

  def difference(self, pset, newSize = 10):
    difference = Set(newSize)
    aux = hashTable(self.size)
    for key in range(self.size):
      val = self.search(key)
      if val is not False and val is not None:
        aux.__setitem__(val, key)
        difference.insert(val)
    for key in range(pset.size):
      val = pset.search(key)
      if val is not False and val is not None and val in difference.table:
        i = aux.__getitem__(val)
        difference.delete(i)
    return difference
