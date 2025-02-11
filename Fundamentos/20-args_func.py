# 1 - Função para imprimir um nome completo
"""
def imprime_nome_completo(nome, sobrenome):
    print(f"Seu nome é {nome} {sobrenome}")

nome = input("Digite seu nome: ")
sobrenome = input("Digite seu sobrenome: ")
imprime_nome_completo(nome, sobrenome)


# 2 - Função para somar dois números - parâmetros no prompt de comando
def soma():
    a = int(input("Digite o primeiro valor: "))
    b = int(input("Digite o segundo valor: "))
    Resultado = a + b
    print(f"O resultado é {Resultado}")


print(soma())
"""

# 2 - Função para somar dois números - parâmetros no print

def sum_numbers(a, b):
    return a + b

print(f"A soma é {sum_numbers(20, 30)}")


# 3 - Função com parâmetro default
def adress(country="Brasil"):
    print(f"Eu moro em: {country}")

adress()
adress("Paraguay")

