import os
import random

def step(o):
    # degrau
    if o > 0:
        return 1
    else:
        return 0

def esrros(o, predc):
    global target
    erro = target[o] - predc
    print('erro:', erro)
    return erro

def somatorioExpecifc(a):
    global pesoBias
    global bias
    global entradas
    global pesos
    global target
    # calculo do neuronio - somatorio de entrada
    predicao = 0
    for j in range(coluns):
        predicao += entradas[a][j] * pesos[j]
    predicao += bias * pesoBias
    aux = step(predicao)
    print(a ,'predicao: [',  aux, ']', 'entradas:', entradas[a], 'pesos:', pesos, 'pesosBias:', pesoBias, ' esperado:', target[a])
    return aux

def corrigirPesos(a, err):
    global pesoBias
    global bias
    global entradas
    global pesos
    global coluns
    novoPesos = [0] * coluns
    novoPesosBias = 0
    for i in range(coluns):
        novoPesos[i] = pesos[i] + 0.2 * err * entradas[a][i]
    novoPesosBias = pesoBias + 0.2 * err * bias
    
    
    

    pesoBias = novoPesosBias
    for i in range(coluns):
        pesos[i] = novoPesos[i]
    print('novoPeso:', novoPesos, 'pesoBias:', pesoBias)

# definiçao global inicial
pesoBias = 0.2
bias = 1

entradas = [
    [0,0],
    [0,1],
    [1,0],
    [1,1],
]
pesos = [0.0, 0.0]
target = [0,
          1,
          1,
          1,]
coluns = len(entradas[0])
linhs = len(entradas)
#acrecimo = [0]


def aleatorio():
    global pesos
    global pesoBias
    for i in range(len(pesos)):
        pesos[i] = random.uniform(-1, 1)
    pesoBias = random.uniform(-1, 1)




def exec():
    aleatorio()
    global linhs
    global pesoBias
    contador = 1
    saida = True
    while saida:
        print('\n----------------Epoca:', contador)
        saida = False
        for i in range(linhs):
            print('--------------Amostra:', i)
            errAux = esrros(i, somatorioExpecifc(i))
            
            if errAux != 0:
                corrigirPesos(i, errAux)
                saida = True
                break
        contador += 1

def portaAnd():
    global target
    target[0] = 0
    target[1] = 0
    target[2] = 0
    target[3] = 1

def portaXor():
    global target
    target[0] = 0
    target[1] = 1
    target[2] = 1
    target[3] = 0
            
# Roda o perceptron

#print("Test do or")
#portaAnd()
#exec()

def elev(b, e):
    aux = b
    for i in range(e-1):
        aux = (aux * b)
    #print('elev:', aux)
    return aux

def targ(opn, n):
    global target
    if opn == '1':
        saida = [1] * n
        saida[0] = 0
    else:
        saida = [0] * n
        saida[n-1] = 1
    target = saida
    print('target:', target)
    

def gerador_binario_matriz(n):
    if n <= 0:
        return [[]]
    else:
        prev_combinations = gerador_binario_matriz(n - 1)
        new_combinations = []
        for combination in prev_combinations:
            new_combinations.append(combination + [0])
            new_combinations.append(combination + [1])
        return new_combinations

def menu_gerador_matriz(n):
    os.system('cls' if os.name == 'nt' else 'clear')
    global entradas
    combinations = gerador_binario_matriz(n)
    entradas = combinations
    for i in entradas:
        print(i)
    

def person():
    global linhs
    global coluns
    global entradas
    global target
    entr = int(input('Quantas entradas(colunas): '))
    amostr = int(input('Quantas amostras(linhas): '))
    os.system('cls' if os.name == 'nt' else 'clear')

    linhs = amostr  # número de linhas
    coluns = entr  # número de colunas

    # Inicialize a matriz com valores sequenciais
    print('Valores da entrada:')
    matr = [[int(input()) for j in range(coluns)] for i in range(linhs)]
    os.system('cls' if os.name == 'nt' else 'clear')
    for linha in matr:
        print(linha)
    print('\nValores target(resultado_predeterminado)')
    target = [int(input()) for i in range(amostr)]
    os.system('cls' if os.name == 'nt' else 'clear')
    print(target)
    os.system('cls' if os.name == 'nt' else 'clear')
    entradas = matr

def painel():
    #print('predefinição de Assets \n 1: or \n 2: and \n 3: personalizado\n :')
    option = input('predefinição de Assets \n 1: or \n 2: and \n 3: personalizado\n :')
    match option:
        case '1':
            opn = int(input('Quantas entradas ( 1 < ):'))
            menu_gerador_matriz(opn)
            targ(option, elev(2, opn))
            exec()
        case '2':
            opn = int(input('Quantas entradas ( 1 < ):'))
            menu_gerador_matriz(opn)
            targ(option, elev(2, opn))
            exec()
        case '3':
            person()
            exec()
painel()