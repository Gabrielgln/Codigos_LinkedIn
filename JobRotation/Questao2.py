valor = 5
penultimo = 1
ultimo = 1
for i in range(valor):
  proximo = penultimo + ultimo
  if valor == 1:
    print("O valor:",valor,",pertence a sequencia fibonacci!")
  elif valor == proximo:
    print("O valor:",valor,",pertence a sequencia fibonacci!")
  penultimo = ultimo
  ultimo = proximo
