# utilizando o input

name = input("Digite o nome do filme:")
yearLaunch = int(input("Digite o ano de lançamento:"))
score = float(input("Digite a nota:"))


print("Dados do filme")
print("==========================")

# Alternativa 2
print("Nome do Filme:", name,
      "\nAno de lançamento: ", yearLaunch,
      "\nScore: ", score
      )

# Alternativa 3 \

print(
    f"Nome do filme: {name}\n",
    f"Data de lançamento: {yearLaunch}\n",
    f"Nota do filme: {score}\n"
)