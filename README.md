#Tipo Abstrato Set com Hash Table

Este é um exemplo de implementação de um Tipo Abstrato Set (conjunto) em Python usando uma estrutura de dados de tabela hash. O conjunto implementado possui as seguintes operações: `insert`, `delete`, `search`, `union`, `intersection` e `difference`.

## Escolha da Estrutura de Dados

Foi escolhida a estrutura de dados de tabela hash para a implementação do conjunto devido às seguintes vantagens:

- **Inserção, Exclusão e Pesquisa Eficientes**: A tabela hash oferece operações de inserção, exclusão e pesquisa com tempo médio constante, tornando-as muito eficientes.

- **Verificação de Duplicatas Simples**: É fácil evitar a duplicação de elementos em um conjunto usando uma tabela hash, pois os valores duplicados são naturalmente tratados.

- **Espaço e Tempo Previsíveis**: A complexidade de tempo e espaço é geralmente previsível e depende da carga da tabela.

## Complexidade de Tempo e Espaço

Aqui estão as análises de complexidade de tempo e espaço para cada operação no conjunto implementado, com base no seu código:

### `insert(val)`

- Complexidade de Tempo:
  - O(1) em média, devido à inserção direta na tabela hash.
- Complexidade de Espaço:
  - O(1) em média, para armazenar o valor na tabela hash.

### `delete(key)`

- Complexidade de Tempo:
  - O(1) em média, para excluir um valor da tabela hash.
- Complexidade de Espaço:
  - O(1) em média, pois a exclusão libera espaço na tabela.

### `search(key)`

- Complexidade de Tempo:
  - O(1) em média, para encontrar um valor na tabela hash.
- Complexidade de Espaço:
  - O(1) em média, pois não há alocação de espaço adicional.

### `union(pset)`

- Complexidade de Tempo:
  - O(N), onde N é o número total de elementos nos dois conjuntos. Isso ocorre devido à iteração sobre ambos os conjuntos e à inserção de elementos na tabela hash resultante.
- Complexidade de Espaço:
  - O(N), para criar o conjunto resultante da união.

### `intersection(pset)`

- Complexidade de Tempo:
  - O(N^2), onde N é o número total de elementos nos dois conjuntos. Isso ocorre devido à verificação de igualdade entre todos os pares de elementos.
- Complexidade de Espaço:
  - O(N), para criar o conjunto resultante da interseção.

### `difference(pset)`

- Complexidade de Tempo:
  - O(N), onde N é o número total de elementos nos dois conjuntos. Isso ocorre devido à iteração sobre ambos os conjuntos e à exclusão de elementos da tabela hash resultante.
- Complexidade de Espaço:
  - O(N), para criar o conjunto resultante da diferença.

## Exemplo de Uso

Veja o código de exemplo fornecido nos arquivos `main.py`, `set.py` e `hashTable.py` para exemplos de uso das operações do conjunto.

