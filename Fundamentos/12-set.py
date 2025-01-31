filmsSet = {"Inception", "The Shawshank Redemption", "The Dark Knight", "Pulp Fiction", "Interstellar"}

print(type(filmsSet))

print(len(filmsSet))

# fazendo mescla de sets
exampleSet = {"Inception", 1, 8, "The Prince"}
filmsSet.update(exampleSet)
print(filmsSet)