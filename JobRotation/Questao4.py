sp = 67.83643
rj = 36.67866
mg = 29.22988
es = 27.16548
outros = 19.84953

somaTotal = sp + rj + mg + es + outros

print(somaTotal)
porcemtagemSP = (sp/somaTotal)
porcemtagemRJ = (rj/somaTotal)
porcemtagemMG = (mg/somaTotal)
porcemtagemES = (es/somaTotal)
porcemtagemOutros = (outros/somaTotal)

porcemtagemSP = sp*porcemtagemSP
porcemtagemRJ = rj*porcemtagemRJ
porcemtagemMG = mg*porcemtagemMG
porcemtagemES = es*porcemtagemES
porcemtagemOutros = outros*porcemtagemOutros

print("SP: %.2f" % porcemtagemSP,"%")
print("RJ: %.2f" %porcemtagemRJ,"%")
print("MG: %.2f" %porcemtagemMG,"%")
print("ES: %.2f" %porcemtagemES,"%")
print("Outros: %.2f" %porcemtagemOutros,"%")
