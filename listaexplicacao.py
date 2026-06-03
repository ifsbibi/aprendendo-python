# Manipulado Lista

## 1. Métodos de Lista (Modificam a própria lista)

### Adicionar Elementos
##- `append(x)`: Adiciona o elemento `x` ao **final** della lista.
##- `insert(i, x)`: Insere o elemento `x` na **posição (índice) específica** `i`.
##- `extend(iterable)`: Adiciona todos os elementos de uma outra lista (ou iterável) ao final da lista atual.

### Remover Elementos
##- `remove(x)`: Remove o **primeiro** elemento com o valor `x` que encontrar. Retorna um erro se o valor não existir.
##- `pop([i])`: Remove e **retorna** o elemento da posição `i`. Se não passar o índice, ele remove e retorna o **último** elemento.
##- `clear()`: Remove **todos** os elementos da lista, deixando-a vazia `[]`.

### Ordenação e Inversão
##- `sort(reverse=False)`: Ordena os elementos da lista **definitivamente** (em ordem crescente por padrão).
##- `reverse()`: Inverte a ordem dos elementos da lista.

### Informação e Busca
##- `count(x)`: Conta quantas vezes o elemento `x` aparece na lista.
##- `index(x)`: Retorna o **índice** da primeira ocorrência do elemento `x`.

### Cópia
##- `copy()`: Retorna uma cópia rasa (*shallow copy*) da lista.

## 2. Funções Nativas (Built-in Functions)

### Análise Numérica e Tamanho
##- `len(lista)`: Retorna a **quantidade de elementos** (tamanho) da lista.
##- `max(lista)`: Retorna o **maior** elemento da lista.
##- `min(lista)`: Retorna o **menor** elemento da lista.
##- `sum(lista)`: Retorna a **soma** de todos os elementos (válido para listas numéricas).

### Ordenação e Iteração (Não modificam a lista original)
##- `sorted(lista, reverse=False)`: Retorna uma **nova lista ordenada**, mantendo a lista original intacta.
##- `reversed(lista)`: Retorna um iterador que percorre a lista de trás para frente (não altera a original).
##- `enumerate(lista)`: Retorna um objeto enumerado, permitindo iterar pelos elementos e seus respectivos **índices** ao mesmo tempo.
##- `zip(*iterables)`: Agrupa elementos de várias listas em tuplas, baseando-se na posição.