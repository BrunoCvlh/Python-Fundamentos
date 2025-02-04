moviesList = ["Jurassic World", "Inception", "The Godfather", "Titanic"]

# Iterando valores de uma lista
for movie in moviesList:
    print(movie)

# Quando a condição for atendida o loop será encerrado
for movie in moviesList:
    print(movie)
    if movie == "Inception":
        break

# Quando a condição for atendida o loop vai para a proxima iteração
for movie in moviesList:
    if movie == "The Godfather":
        continue
    print(movie)

# Avaliação do filme
movieName = input("Digite o nome do filme: ")
movieRating = int(input("Digite quantas avaliações deseja fazer: "))

total = 0
for item in range(movieRating):
    note = float(input("Digite a nota para o filme: "))
    total += note

if movieRating > 0:
    average = total / movieRating
else:
    average = 0

print(f"A nota média de avaliação do filme {movieName} é {average}")