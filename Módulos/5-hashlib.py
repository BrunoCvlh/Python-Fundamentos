import hashlib

# 1 - Verificar os algoritmos disponíveis no módulo
print(hashlib.algorithms_available)

# 2 - Verificar os algoritmos de acordo com o SO
print(hashlib.algorithms_guaranteed)

# 3 - Utilizando o algoritmo SHA256
algorithm = hashlib.sha256()
print(algorithm.digest())
message = "A melhor forma de prever o futuro é criá-lo".encode()
algorithm.update(message)
print(algorithm.hexdigest())

# 4 - Utilizando MD5
md5 = hashlib.md5()
md5.update(message)
print(md5.hexdigest())