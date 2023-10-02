from hashTable import hashTable

from Set import Set


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
  
