import pprint

filmsDict = {
    "Inception": {
            "yearRelease":2010,
            "IMDB rating":8.8,
            "genero":["sci-fi", "suspense", "mistério"]
    },
    "Dark Knight": {
            "yearRelease":2015,
            "IMDB rating":7.8,
            "genero":["sci-fi", "suspense"]
    },
    "Poderoso-Chefao": {
            "yearRelease":2001,
            "IMDB rating":8.9,
            "genero":["suspense", "mistério"]
    }
}

pp = pprint.PrettyPrinter(depth=4)
pp.pprint(filmsDict)

print("=========================")

# Buscar uma informação dentro de um dicionário aninhado
print(filmsDict["Dark Knight"]["genero"])

# Adicionar novo item
filmsDict["Poderoso-Chefao"]["yearRelease"] = 1998
print(filmsDict)

# Deletar um dicionário
del filmsDict["Dark Knight"]
pp.pprint(filmsDict)