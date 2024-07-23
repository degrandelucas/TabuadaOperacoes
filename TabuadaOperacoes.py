#Programa que exibi a Tabuada de um numero de 1 a 10 ou operações matemáticas entre dois numeros

from Tabuada import Tabuada #import Tabuada para importar o modulo (arquivo) Tabuada
from Multiplicacao import Multiplicacao
from Soma import Soma
from Divisao import Divisao
from Subtracao import Subtracao

def menu():
    print("")
    print("*** Menu de Opções: ***")
    print("1 - Exibir a Tabuada de um número: ")
    print("2 - Exibir uma multiplicação entre dois números ")
    print("3 - Exibir uma soma entre dois números ")
    print("4 - Exibir uma divisão entre dois números ")
    print("5 - Exibir uma subtração entre dois números ")
    print("6 - Sair do Programa... \n")
    
    Escolha = int(input("Escolha uma opção acima: "))
    return Escolha

while True:
    Opcao = menu()
    
    if Opcao == 1:
        numero = int(input("Escolha o número para cálculo da Tabuada: "))
        Tabuada(numero) 
        
    elif Opcao == 2:
        Primeiro = int(input("Escolha o primeiro número da multiplicação: "))
        Segundo = int(input("Escolha o segundo número da multiplicação: "))
        Multiplicacao(Primeiro, Segundo) 
    
    elif Opcao == 3:
        Primeiro = int(input("Escolha o primeiro número da soma: "))
        Segundo = int(input("Escolha o segundo número da soma: "))
        Soma(Primeiro, Segundo)
    
    elif Opcao == 4:
        Primeiro = int(input("Escolha o primeiro número da divisão: "))
        Segundo = int(input("Escolha o segundo número da divisão: "))
        Divisao(Primeiro, Segundo)
    
    elif Opcao == 5:
        Primeiro = int(input("Escolha o primeiro número da subtração: "))
        Segundo = int(input("Escolha o segundo número da subtração: "))
        Subtracao(Primeiro, Segundo)
    
    elif Opcao == 6:
        print("Saindo do Programa... ")
        break

    else:
        print("Escolha uma Opção Válida!")
    



    