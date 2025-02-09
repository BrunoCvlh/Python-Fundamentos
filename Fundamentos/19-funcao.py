# 1 - Função para imprimir uma mensagem

def welcome():
    print("Seja bem vindo!")

welcome()

#for i in range(10):
#welcome()
# 2 - Função para calcular a média de notas
def calculate_average():
    num_ratings = int(input("Digite quantas notas deseja declarar:"))
    total = 0
    for i in range(num_ratings):
        note = float(input("Digite a nota do filme: "))
        total += note

    if num_ratings > 0:
        average = total / num_ratings
    else:
        average = 0
    return average


print(f"A média das notas foi {calculate_average()}")

