"""
    ## Listas em python 3

    As listas em python são objetos heterogênios iteráveis, isso significa que podem
    armazenar em tempo de execução dados de valores e tipos diferentes.

    - Exemplo:

    ```python
    >>> lista = ["NOME 1", 12, "QUIN. B", 1.90]
    >>> lista
    ['NOME 1', 12, 'QUIN. B', 1.9]
    ```

    ### Índices
    
    Para acessar os valores de uma lista em python usa-se os índicies, eles podem ser
    negativos (-N, ..., -2, -1) e positivos (0, 1, 2, .., N). Os positivos acessam os
    itens de forma crescente e os negativos decrescente.

    - Exemplo:

    ```python
    >>> lista[0]
    NOME 1
    >>> lista[3]
    1.90
    >>> lista[1]
    12
    >>> lista[-1]
    1.90
    >>> lista[-2]
    QUINT. B
    >>> lista[-3]
    12
    ```

    ### Adicionar itens

    Para adicionar itens na lista é possível usando ```.append()```, ```.insert()``
    ```.extend()``, ```[ ] + [ ]```.

    - Exemplo:

    ```python
    >>> lista.append("CENTRO")
    >>> lista
    ['NOME 1', 12, 'QUIN. B', 1.9, 'CENTRO']
    >>> lista.insert(-1, 78.4)
    >>> lista
    ['NOME 1', 12, 'QUIN. B', 1.9, 78.4, 'CENTRO']
    >>> lista.extend(["MANAUS", "AMAZONAS"])
    >>> lista
    ['NOME 1', 12, 'QUIN. B', 1.9, 78.4, 'CENTRO', 'MANAUS', 'AMAZONAS']
    >>> lista = lista + ["BRASIL"]
    >>> lista
    ['NOME 1', 12, 'QUIN. B', 1.9, 78.4, 'CENTRO', 'MANAUS', 'AMAZONAS', 'BRASIL']
    ```

    ### Remover itens

    Para remover é possível usar ```.pop()```, sem parâmetro remove o últimos elemento,
    passando um parâmetro remove o item que tem como índice o parâmtro, caso passe o número
    2 remove o item na posição 2. Outra opção é o ```.remove()``` passando como parâmetro o 
    elemento que se deseja remover. Há ainda a possibilidade de remover todos os elementos
    de uma lista usando o ```.clear()```

    - Exemplo:

    ```python
    >>> lista.pop()
    'BRASIL'
    >>> lista
    ['NOME 1', 12, 'QUIN. B', 1.9, 78.4, 'CENTRO', 'MANAUS', 'AMAZONAS']
    >>> lista.pop(2)
    'QUIN. B'
    >>> lista
    ['NOME 1', 12, 1.9, 78.4, 'CENTRO', 'MANAUS', 'AMAZONAS']
    >>> lista.remove(78.4)
    >>> lista
    ['NOME 1', 12, 1.9, 'CENTRO', 'MANAUS', 'AMAZONAS']
    >>> lista.clear()
    >>> lista
    []
    ```

"""

lista_1 = []
lista_1.append(["DAYVSON", 12, "QUIN. B", 1.90])
lista_1.append(["THAYANE", 9, "QUIN. B.", 1.85])
print(lista_1)

for i in range(2):
    nome = input(" informe seu nome: ")
    idade = input(" informe sua idade: ")
    endereco = input(" informe seu endereco: ")
    altura = input(" informe sua altura: ")
    
    lista_3 = []
    lista_3.append(nome)
    lista_3.append(idade)
    lista_3.append(endereco)
    lista_3.append(altura)
    lista_1.append(lista_3)
    
    print(lista_1)
