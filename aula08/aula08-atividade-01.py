##
# Aula 08 - Atividade 01 - Exercício 01
# Autor    : Giovanni Falconi
# Data     : 12/08/2025
##
"""
Função Saudação
    - Imprime uma mensagem de boas vindas
Função Somar
    - Soma 2 números A e B
Função Par ou Ímpar
    - Determina se um número é par ou ímpar
Função Fatorial
    - Retorna o valor de um número fatorial
Função Maior Elemento
    - Determina o maior elemento em uma lista
Função Média Aritmética
    - Determina a média aritmética de uma lista de números
Função Palíndromo
    - Determina se uma palavra é ou não palíndromo.


"""
def saudacao():
  print('\n\n\tOibomdia, que bom te ver :3\n\n')

def somar(a,b):
  print(f'O resultado da soma é {int(a)+int(b)}.')

def parouimpar(n):
  if n % 2 == 0:
    print(f'{n} é Par.')
  else:
    print(f'{n} é Ímpar.')
  
def fatorial(n):
  value = 1
  n = int(n)
  for num in range(1, n+1):
      value = value * num
  return f'O fatorial de {n} é {value}'

def maiorelemento(x):
  for elemento in x:
    resultado = 1
    if elemento > resultado:
      resultado = elemento
    else:
      pass
  return f'O maior elemento é {resultado}'

def mediaaritmetica(x):
  sumoflist = sum(x)
  mediaoflist = sumoflist / len(x)
  return f'A média aritmética desses números é {mediaoflist}'

def palindromo(x):
  if x == x[::-1]:
    return f'{x} É palíndromo.'
  else:
    return f'{x} Não é palíndromo.'

def contarvogais(texto):
  counter = 0
  vogais = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
  for char in texto:
    if char in vogais:
      counter += 1
    else:
      pass
  return counter

def tabuadade(x):
  resultado = []
  for n in range(1, 11):
    valor = x * n
    resultado.append(valor)
  return resultado




##
# Corpo do Programa
##

#saudacao()
#somar(6, 8)
#parouimpar(7)
#parouimpar(2)
#fatorial(7)
#maiorelemento([6, 9, 88, 6666, 929])
#print(mediaaritmetica([8, 9, 11, 15, 66]))
#print(palindromo('osso'))
#print(palindromo('sopa'))
#print(contarvogais('JANUARY. Delightful display. Snowdrops bow their pure white heads To the suns glory.'))
#print(tabuadade(11))



