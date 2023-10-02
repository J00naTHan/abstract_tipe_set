# Tipo Abstrato Set com Hash Table

Esta é minha implementação de tipo abstrato set (conjunto), feita inteiramente em Python, usando como forma de controle de dados a estrutura de dados hash table. O tipo implementado possui as operações: `insert`, `delete`, `search`, `union`, `intersection` e `difference`.

## Escolha da Estrutura de Dados

Optei pelo uso da hash table por conta de suas capacidades de:

- **Insert, Delete e Search Eficientes**: A tabela hash oferece operações de `insert`, `delete` e `search` com tempo médio e memória constantes, mostrando que é uma estrutura de dados interessante para esse propósito.

- **Espaço e Tempo Previsíveis**: A complexidade de tempo e espaço é geralmente previsível.

E também por ser uma estrutura já abordada em aula, e suas operações já terem sido demonstrados como potencialmente eficientes.

## Complexidade de Tempo e Espaço

Analisando tempo e espaço da minha implementação, podemos chegar à seguinte conclusão:

### `Insert`

- Complexidade de Tempo:
  - O(1) em média, devido à inserção direta na tabela hash por meio de um índice.
- Complexidade de Espaço:
  - O(1) em média, para armazenar o valor na tabela hash.

### `Delete`

- Complexidade de Tempo:
  - O(1) em média, para excluir um valor da tabela hash, graças à localização do valor diretamente na tabela.
- Complexidade de Espaço:
  - O(1) em média, pois a exclusão libera espaço na tabela.

### `Search`

- Complexidade de Tempo:
  - O(1) em média, para encontrar um valor na tabela hash, aproveitando-se da mesma característica citada anteriormente.
- Complexidade de Espaço:
  - O(1) em média, pois não há alocação de espaço adicional.

### `Union`

- Complexidade de Tempo:
  - O(N), porque temos a iteração por cada um dos dois conjuntos (cada iteração possui complexidade O(N)) e por fim, a comparação entre valores dos dois conjuntos que gera o conjunto resultante. 
- Complexidade de Espaço:
  - O(N), para criar o conjunto resultante da operação, que possui os valores de ambos os conjuntos iniciais.

### `Intersection`

- Complexidade de Tempo:
  - O(N^2), pois nesse caso se fez necessário o uso de loops encadeados, gerando complexidade quadrática. Na implementação, foi necessário cruzar os dados da tabela auxiliar com o loop pelo segundo conjunto, para realizar as comparações que resultam no conjunto final.
- Complexidade de Espaço:
  - O(N), para criar o conjunto resultante da interseção, nesse caso, a memória auxiliar é usada, mas possui menos entradas que o conjunto.

### `Difference`

- Complexidade de Tempo:
  - O(N), possui complexidade semelhante a da operação `union`, inclusive sua estrutura é semelhante, há a iteração sobre os dois conjuntos, e então, a comparação.
- Complexidade de Espaço:
  - O(N), referente ao conjunto resultante.

## Créditos

- Implementação de hash table: [codebasics](https://github.com/codebasics/data-structures-algorithms-python/tree/master/data_structures/4_HashTable)
