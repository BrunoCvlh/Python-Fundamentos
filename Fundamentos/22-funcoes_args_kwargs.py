"""
*args -> Utilizamos ele quando não temos certeza de quantos argumentos queremos ter na função.
- Os argumentos são passados como uma tupla

**kwargs -> Além dos valores podemos passar também as respectivas chaves de cada argumento.
- Os argumentos são passados como um dicionário
"""
"""
# 1 - Soma de numeros
def sum(*num):
    sum_total = 0
    for n in num:
        sum_total += n
        print(f"A soma é {sum_total}")
sum(7,8,9)
"""
# 2 - Apresentação de cursos
def presentation(**data):
    for key,value in data.items():
        print(f"{key} - {value}")
print("Lista de cursos: ")
presentation(name="Curso", category="Backend", level="Intermediário")
presentation(name="Cursos", category="Backend1", level="Intermediário1")
presentation(name="Cursoz", category="Backend2", level="Intermediário2")