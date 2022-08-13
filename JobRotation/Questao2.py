quantidade = int(input('quantos valores?' ))
penultimo = 1
ultimo = 1
print(penultimo,ultimo,end=' ')
for i in range(quantidade-2):
  proximo = ultimo + penultimo
  print(proximo,end=' ')
  penultimo = ultimo
  ultimo = proximo
