# Listando valores de 0 a 10 que sejam menores do que 4
listNumbers = [i for i in range(10) if i < 4]
print(listNumbers)

# Lista de filmes
moviesList = ["Jurassic World", "Inception", "The Godfather", "Titanic"]

# Filmes que possuem a letra e no título
moviesWithE = [movie for movie in moviesList if "e" in movie.lower()]
print(moviesWithE)

# Filmes assistidos
moviesWatched = [movie for movie in moviesList if movie != "The Godfather"]
print(moviesWatched)

# Encontrando um filme pelo nome
while True:
    searchName = input("Digite o nome do filme que deseja encontrar (ou digite sair para encerrar): ")
    if searchName.lower() == "sair":
        print("Programa encerrado")
        break

    foundMovies = [movie for movie in moviesList if searchName.lower() in movie.lower()]
    if foundMovies:
        print(f"Filmes encontrados com o nome: {searchName}")
        for foundMovie in foundMovies:
            print(foundMovie)
    else:
        print(f"Nenhum filme foi encontrado com o nome {searchName}. Tente novamente")