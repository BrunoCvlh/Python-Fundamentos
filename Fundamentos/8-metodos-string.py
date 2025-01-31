movieName = "Top Gun"
description = """
    Top Gun Maverick é um filme de aviação
    muito consagrado na indústria.
"""

print(movieName.upper())
print(movieName.lower())
print(movieName.capitalize()) #primeira letra maiúscula
print(movieName.title()) #todas as letras maiúsculas
print(movieName.center(20, "-")) #preenche os espaços vazios com a string escolhida
print(movieName.find("u")) #retorna a posição do caractere
print(movieName.replace("Top", "Matrix")) #troca uma string por outra
print(description.split(",")) #separa os valores