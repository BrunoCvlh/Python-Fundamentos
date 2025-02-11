import re

text = "Udemy - uma plataforma com muitos cursos"

# índice inicial e final e palavras
# o r significa uma raw string (string bruta)

match = re.search(r"uma plataforma", text)
print(f"Índice Inicial: {match.start()}") 
print(f"Índice Inicial: {match.end()}")

# Buscando indice que possui ponto
site = "https://udemy.com"
match = re.search(r".", site)
print(match)

# Buscando caracteres dentro de uma frase
pattern = "[g-m]"
result = re.findall(pattern, text)
print(result)

# Verificando o início de uma string
rule = r'^A'
phrases = ["A casa está suja", "O dia está limpo", "Vamos passear"]
for f in phrases:
    if re.match(rule, f):
        print(f"Corresponde: {f}")
    else:
        print(f"Não corresponde: {f}")