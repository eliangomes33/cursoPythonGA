# Quase uma lista, mas que não pode ter valores iguais

conjunto = {"alho", "sal", "cenoura", "sal", "banana", "sal", "alface"}

cp_conjunto = conjunto.copy()

print(conjunto)
print(cp_conjunto)
conjunto.add("uva")
print(conjunto)
conjunto.pop()
print(conjunto)
print(sorted(conjunto))

conjunto_comparar = {"alho", "sal", "cenoura"}
print(conjunto_comparar)
print(conjunto.difference(conjunto_comparar))
