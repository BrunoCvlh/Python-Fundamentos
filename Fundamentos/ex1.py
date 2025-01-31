#Ex1
#nome = input("Escreva um nome:")
#sobrenome = input("Escreva um sobrenome:")

#print(f"{sobrenome}, {nome}")

#Ex2
texto = "Python é muito interessante"
palavras = texto.split()
textoInvertido = " ".join(palavras[::-1])
#print(textoInvertido)

#Ex3
substantivo1 = "arara"
substantivo2 = "ovo"

palindromo1 = substantivo1 == substantivo1[::-1]
palindromo2 = substantivo2 == substantivo2[::-1]

print(palindromo1)
print(palindromo2)