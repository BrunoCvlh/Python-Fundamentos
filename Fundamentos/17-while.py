moviesList = ["Jurassic World", "Inception", "The Godfather", "Titanic"]

#1 - iterando valores de uma lista de filmes utilizando while
index = 0
while index < len(moviesList):
    print(moviesList[index])
    index +=1

#2 - Quando a condição for atendida o loop será encerrado
index = 0
while index < len(moviesList):
    if moviesList[index] == "The Godfather":
        break
    print(moviesList[index])
    index +=1

#3 - Quando a condição for atendida o loop vai para a próxima iteração
index = 0
while index < len(moviesList):
    if moviesList[index] == "The Godfather":
        index +=1
        continue
    print(moviesList[index])
    index +=1

#4 - Avaliação do filme com While
movieName = input("Digite o nome do filme: ")
movieRating = int(input("Digite quantas avaliações deseja fazer: "))
total = 0
count = 0

while count < movieRating:
    input("Qual nota você dá para o filme: ")
    total += note
    count +=1

if movieRating > 0:
    average = total / movieRating
else:
    average = 0

print(f"A nota média do filme {movieName} é {average}")
