pessoa = {"Nome": "Brenda", "idade": 26, "Filhos": {"Nome": "Catarina", "idade": 6}}

print(pessoa)

print(pessoa["Nome"])

print(pessoa["Filhos"])

print(pessoa["Filhos"]["Nome"])

del pessoa["Filhos"]

print(pessoa)