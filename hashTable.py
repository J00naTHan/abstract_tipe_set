class hashTable:
  def __init__ (self, size):
    self.size = size
    self.table = [None for i in range(self.size)]

  def getHash(self, key):
    hash = 0
    key = str(key)
    for char in key:
      hash += ord(char)
    return hash % self.size
    
  def __getitem__(self, key):
    h = self.getHash(key)
    return self.table[h]
    
  def __setitem__(self, key, val):
    h = self.getHash(key)
    self.table[h] = val 
    return self.table[h]
        
  def __delitem__(self, key):
    h = self.getHash(key)
    b = self.table[h]
    self.table[h] = None
    return b
