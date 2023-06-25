"""
Programa: capital_do_sul
Descrição: Este programa verifica se uma cidade é a capital do sul do Brasil.
Data : 24/06/2023
Versão: 0.0.1
"""

#Atribuição de variáveis



cap = ['porto alegre', 'curitiba', 'florianópolis']
x1 = 0

#Entrada de dados

x1 = input("Qual a cidade?")

#Processamento de dados
x2 = x1.lower()
if x2 in cap:
    x1 = x1.capitalize()
    print(f"{x1} é capital de um estado da região sul do Brasi.")

else:
    x1 = x1.capitalize()
    print(f"{x1} não é capital de um estado da região sul do Brasi.")
#Saida de dadaos