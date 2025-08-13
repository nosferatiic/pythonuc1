# Exercício 01

def saudacao():
    print('Olá, mundo!')

def matematica():
    nbrone = int(input('Digite o primeiro número a ser somado: '))
    nbrtwo = int(input('Digite o segundo número a ser somado: '))
    print(f'O resultado da sua soma é {nbrone + nbrtwo}.')

def soma(a, b):
    return f'Seu resultado é {a+b}'

def subtracao(a, b):
    return f'Seu resultado é {a-b}'

def umadez():
    for n in range(1,11):
        print(n)

def fatorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * fatorial(n-1)

def isprime(n):
    for number in range(2, n+1):
        if n % number == 0:
            return 'Número digitado não é primo.'
        else:
            return 'Número digitado é primo.'

def usersort():
    userlist = input('Digite uma lista de números, separados por espaços.')
    listforreal = []
    for character in userlist.split():
        listforreal.append(int(character))
    listforreal.sort()
    return listforreal

def contarvogais(texto):
  counter = 0
  vogais = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
  for char in texto:
    if char in vogais:
      counter += 1
    else:
      pass
  return counter

def mediaaritmetica(x):
  sumoflist = sum(x)
  mediaoflist = sumoflist / len(x)
  return f'A média aritmética desses números é {mediaoflist}'

def stringaocontrario():
    stringcorreta = input('Escreva algo para inverter: ')
    return f'Sua string invertida é {stringcorreta[::-1]}.'

def maiorelemento(x):
  for elemento in x:
    resultado = 1
    if elemento > resultado:
      resultado = elemento
    else:
      pass
  return f'O maior elemento é {resultado}'


### ESSE CODIGO NÃO ESTÁ PRONTO ###
def fibonacci(x):
    fib = [0, 1]
    while max(fib) < x:
        newfib = fib[-1] + fib[-2]
        fib.append(newfib)
    return(fib)


if __name__ == "__main__":
    #saudacao()
    #matematica()
    #print(soma(3, 6))
    #print(subtracao(12, 6))
    #print(umadez())
    #print(fatorial(7))
    #print(isprime(11))
    #print(usersort())
    #print(contarvogais('The quick brown fox soemthing something i do not care'))
    #print(mediaaritmetica([7, 8, 6, 7, 99]))
    #print(stringaocontrario())
    #print(maiorelemento([1, 2, 66, 223, 338]))
    print(fibonacci(44))
