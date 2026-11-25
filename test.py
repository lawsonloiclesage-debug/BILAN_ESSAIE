import json

with open("pcg.json", "r", encoding="utf-8") as f:
   data = json.load(f)

#numero de classe
for num in data:
   print(num)

print("-------------------------------------------------------")



# Nom de Classe
for classe in range(1,8):
   print(data[str(classe)]['nom_classe'])

print("-------------------------------------------------------")

"""
# Sous_classe
for num_classe in range(1,8):
   donne1 = data[str(classe)]['nom_classe']
   for num_sous_classe in donne1[]
   print(data[str(classe)]['comptes']['10']['libelle'])
"""
"""
#Sous_compte
for classe in range(1,8):
    donne1 = data[str(classe)]['comptes']   
    for num in range(10,109):
        if not donne1[str(num)]:
           pass
        print(donne1[str(num)]['libelle'])
    if classe > 1:
       break
print("-------------------------------------------------------")
"""

# Schema pour acceder a un compte
data2 = data[str(1)]['comptes']['10']['sous_comptes']['101']
print(data2)
