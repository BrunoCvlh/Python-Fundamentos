import random

# 1 - Seleciona valor aleatório de uma lista
listaNum = [7, 6, 5, 4, 3, 1]
print(random.choice(listaNum))

# 2 - Gera um número aleatório em um intervalo de valores
r1 = random.randint(1,25)
print(r1)

# 3 - Seleciona caracter aleatorio em uma string
name = "Curso Python"
r2 = random.choice(name)
print(r2)

# 4 - Seleciona mais de um valor aleatório
# random.sample(sequencia, tamanho)
print(random.sample(listaNum, 3))
s = "Teste"
print(random.sample(s, 2))