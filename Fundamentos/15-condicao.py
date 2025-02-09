num1 = float(input("Digite um número:"))
num2 = float(input("Digite outro número:"))
oper = input("Escolha a operação (+ - * /):")

if oper == "+":
    result = num1 + num1
elif oper =="-":
    result = num1 - num2
elif oper =="*":
    result = num1 * num2
elif oper =="/":
    if num1 != 0:
        result = num1 / num2
    else:
        print("Não é possível divisão por zero")
else: 
    print("Operação inválida")


print(f"O resultado da operação é {result}")


number = 0

if number > 5:
    print("Sou lindo!")
