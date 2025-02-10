import os

# 1 - Retorna pasta atual
print(os.getcwd())

# 2 - Listar arquivos e pastas
print(os.listdir())

# 3 - Versão do SO
os.system('ver')

# 4 - Configurações das Máquinas
os.system('systeminfo')

# 5 - Limpar a tela do terminal
os.system('cls')

# 6 - Desligar o computador
#os.system('shutdown /s /t 0')
os.system('shutdown /a') #para cancelar o desligamento