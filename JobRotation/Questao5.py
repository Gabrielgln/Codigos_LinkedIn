class Pilha:
  def __init__(self):
    self.head = []

  def append(self,valor):
    self.head.append(valor)

  def remove(self):
    return self.head.pop()

pilha = Pilha()
p_invertido = ''
palavra = input("Digite a palavra que deseja inverter: ")
for i in range(len(palavra)):
  pilha.append(palavra[i])

for i in range(len(palavra)):
  p_invertido = p_invertido + (pilha.remove())

print(p_invertido)
