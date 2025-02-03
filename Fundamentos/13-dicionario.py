filmInception ={
    "title":"Inception",
    "yearRelease":2010,
    "IMDB rating":8.8,
    "genero":["sci-fi", "suspense", "mistério"]
}

print(filmInception)
print(len(filmInception))
print(type(filmInception))

# Recuperar um elemento do dicionário
print(filmInception["genero"])
print(filmInception.get("genero"))

# Buscar chaves do dicionário
print(filmInception.keys())

# Buscar valores do dicionário
print(filmInception.values())

# Buscar itens do dicionário com chave e valor
print(filmInception.items())

# Adicionar itens no dicionário
filmInception["Director"] = "Christopher Nolan"
print(filmInception)

# Atualizar itens no dicionário
filmInception.update({"Director":"C. Nolan"})
print(filmInception)

# Remover item no dicionário (é removido pela chave)
filmInception.pop("Director")
print(filmInception)