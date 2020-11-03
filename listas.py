### LISTAS
# INDICE -> 0, 1, 2, .., N
#           -N, ..., -2, -1
# VALOR  -> [45, 42, 43, ..., 54]
# ACESSAR -> [2] -> 43
# ACESSA  -> [-1] -> 54
#            [-2] -> 33
# ["DAYVSON", 12, "QUIN. B", 1.90]
# ["THAYANE", 9, "QUIN. B.", 1.85]
# [[,..,].
#  [,..,],
#  [,..,].
#   ...
#  [,..,]]
# LISTA_1 = [1, 2, 3, 4, 5]
# LISTA_1[2]
# len(LISTA_1) -> 5
# LISTA_1.append(6) -> [1, 2, 3, 4, 5, 6]
###

lista_1 = []
lista_1.append(["DAYVSON", 12, "QUIN. B", 1.90])
lista_1.append(["THAYANE", 9, "QUIN. B.", 1.85])
print(lista_1)

# for qtd cad
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

###