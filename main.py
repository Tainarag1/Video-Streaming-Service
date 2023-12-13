from cad import funcao_cadastro
from teste import funcao_classes

nome = input('Digite seu nome: ')

print("Olá, " + nome + "! Seja bem-vindo(a)!\nDigite o número correspondente a uma das opções: \n1 - Já tenho cadastro, desejo acessar.\n2 - Não tenho cadastro, desejo me cadastrar.\n")

x = int(input())

funcao_cadastro(nome, 0, x)