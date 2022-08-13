import json

with open("dados.json") as meu_json:
    dados = json.load(meu_json)

array = []
for i in dados:
    array.append((i['valor']))

array_aux = []
for i in array:
    if i != 0:
      array_aux.append(i)
array = array_aux
del array_aux
 
soma = 0
for i in range(len(array)):
    soma += array[i]
media = soma/len(array)
print("A media geral é: ",media)

maior = 0
menor = 0
for i in range(len(array)):  
  if array[i] > maior:
    maior = array[i]
  if array[i] < maior:
    menor = array[i]

print("O maior valor de faturamento é: ",maior)
print("O menor valor de faturamento é: ",menor)

soma = 0
for i in range(len(array)):
    soma += array[i]
media = soma/len(array)
print("Média mensal: ",media)

dias = 0
for i in range(len(array)):
    if array[i] > media:
        dias = dias + 1;
print("Total de dias que o valor diario ultrapassou a média mensal: ",dias)
