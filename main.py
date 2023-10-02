from set import Set

if __name__ == "__main__":
  set = Set(10)
  pset = Set(10)

  pset.insert(3)
  pset.insert(10)
  pset.insert(7)

  print("\nTestes de Insert:")

  for key in range(pset.size):
    print("pset|", "chave:", key, "valor:", pset.search(key)) if pset.search(key) is not None else None
  
  set.insert(5)
  set.insert(7)
  set.insert(10)
  
  for key in range(set.size):
    print("|set|", "chave:", key, "valor:", set.search(key)) if set.search(key) is not None else None

  p = pset.search("0")  
  s = set.search("2")

  print("\nTestes de Search:")
  print(f'O valor {p}, corresponde a chave "0", de pset')
  print(f'O valor {s}, corresponde a chave "2", de set')
  
  print("\nTestes de Delete:")
  delete = pset.delete(0)
  print(f"Valor Deletado: pset| chave: 0 valor: {delete}")
  print(pset.table)

  print("\nTestes de Union:")
  print("\nTabela Set Original:\n", set.table)
  print("\nTabela Pset Original:\n", pset.table)
  u = set.union(pset)
  print("\nNova Tabela Union\n", u.table)

  print("\nTestes de Intersection:")
  print("\nTabela Set Original:\n", set.table)
  print("\nTabela Pset Original:\n", pset.table)
  i = set.intersection(pset)
  print("\nNova Tabela Intersection\n", i.table)

  print("\nTestes de Difference:")
  print("\nTabela Set Original:\n", set.table)
  print("\nTabela Pset Original:\n", pset.table)
  d = set.difference(pset)
  print("\nNova Tabela Difference\n", d.table)
