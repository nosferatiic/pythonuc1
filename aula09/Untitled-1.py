# %%
produtos = (
    ("Arroz", 5.99, 10),
    ("Feijão", 7.49, 3),
    ("Leite", 4.89, 5),
    ("Óleo", 9.99, 2),
    ("Açúcar", 3.29, 5)
)

descontovalido = 0
desconto = float(input('ADMIN: Escolha o desconto (valor de 0.1 até 0.9):'))
if desconto >= 0.1 and desconto <= 0.9:
  print('Desconto válido.')
  descontovalido = desconto
else:
  print('Desconto inválido.')

print()

print("LISTA DE PRODUTOS")
precosjuntos = []
for nome, preco, qtd in produtos:
    precosjuntos.append(preco * qtd)
    print(f"{nome:.<20} R$ {preco:2.2f} / Valor Total: {(preco * qtd):.2f}")

print()
print(f'Valor total da compra: R$ {sum(precosjuntos)}')
print(f'Desconto: -{(descontovalido * 100):.0f}%')
if descontovalido > 0:
    print(f'Valor com desconto: R$ {((sum(precosjuntos))*(1-descontovalido)):.2f}')

# %%
import random as r 
medianlist = []
biglist = []

for n in range(1,100):
    medianlist.append(r.randint(1, 100))

median = round((sum(medianlist) / len(medianlist)), 2)

for i in medianlist:
  if i > median:
    biglist.append(i)


print(f'A média dos números dessa lista é {median}.')
print(f'Os números maiores que a média são {biglist}.')



# %%



