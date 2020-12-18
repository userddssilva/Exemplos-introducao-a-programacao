def lado_maior(a, b, c):
    if a > b and a > c:
        return a
    elif b > a and b > c:
        return b
    else:
        return c

def lados_menores(a, b, c):
    if a > b and a > c:
        return b, c
    elif b > a and b > c:
        return a, c
    else:
        return a, b

def eh_triangulo(a, b, c):
    _a = lado_maior(a, b, c)
    _b, _c = lados_menores(a, b, c)
    if _a >= _b + _c:
        return False 
    else:
        return True

def eh_equilatero(a, b, c):
    if a == b and b == c:
        return True
    return False

def eh_isosceles(a, b, c):
    if (a == b) or (a == c) or (b == c):
        return True
    return False

def eh_escaleno(a, b, c):
    if (a != b) and (a != c) and (b != c):
        return True
    return False
        

def tipo_triangulo(a, b, c):
    _a = lado_maior(a, b, c)
    _b, _c = lados_menores(a, b, c)
    a, b, c = _a, _b, _c
    if eh_equilatero(a, b, c):
        return 1
    elif eh_isosceles(a, b, c):
        return 2
    elif eh_escaleno(a, b, c):
        return 3

ler = True
while ler == True:
    print("Informe três valores!")
    lado_a = int(input())
    lado_b = int(input())
    lado_c = int(input())

    if (lado_a < 1) or (lado_b < 1) or (lado_c < 1):
        print("Valor errado!")
        print("Insira valores maiores que 1!")
    else :
        if eh_triangulo(lado_a, lado_b, lado_c):
            print("É triangulo")
            tipo = tipo_triangulo(lado_a, lado_b, lado_c)
            if tipo == 1:
                print("Tipo Equilátero")
            elif tipo == 2:
                print("Tipo Isósceles")
            elif tipo == 3:
                print("Tipo Escaleno")
        else:
            print("Não é um triangulo")                

    novo = input("Deseja fazer nova inserção? [S/N]: ")
    if (novo == "N"):
        print("********** fim ************")
        ler = False
