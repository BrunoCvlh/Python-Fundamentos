filmList = ["Inception", "The Shawshank Redemption", "The Dark Knight", "Pulp Fiction", "Interstellar"]

print(len(filmList)) #tamanho da lista

print(filmList.index("Interstellar")) #encontrar o index pelo nome

filmList.append("The lord of the rings") #adicionar item a lista
print(filmList)

filmList.sort() #Ordena os itens da lista
print(filmList)

filmsCopy = filmList.copy() #Copia itens de uma lista para outra
filmsCopy.remove("Pulp Fiction")
print(filmsCopy)

filmsCopy.clear() #limpa todos os itens de uma lista
print(filmsCopy)