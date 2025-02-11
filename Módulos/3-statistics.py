import statistics

# Aplicando média
print(statistics.mean([3, 2, 3, 8, 9]))

# Aplicando mediana
print(statistics.median([1, 2, 4, 8, 9]))
print(statistics.median([1, 2, 3, 7, 8, 9]))

# Aplicando moda
print(statistics.mode([2, 5, 3, 2, 8, 3, 9, 4, 2, 5, 6]))

# Desvio padrão
"""
Quanto mais próximo de zero, significa que os dados estão menos dispersos.
"""
print(statistics.stdev([1, 1.5, 2, 2.5, 3, 3.5, 4, 4.5]))