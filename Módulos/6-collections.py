from collections import Counter, namedtuple, deque
from operator import itemgetter

# 1 - Lista de frutas(contagem)
fruits = ["maçã", "pera", "banana", "maçã", "mamão", "kiwi",
          "maçã", "banana", "banana"
          ]

print(fruits)
print(Counter(fruits))

# 2 - Utilizando tupla nomeada
game = namedtuple('game', ['name', 'price', 'note'])
g1 = game("Lego", 100, 7.9)
g2 = game("Fortnite", 10, 8.1)
print(g1)
print(g2)

# 3 - Ordenando dicionários
students = {"Pedro": 22, "Ana":23, "Paulo":19}
a = sorted(students.items(), key=itemgetter(0)) #itemgetter ordena por chave ou valor
print(a)

# 4 - Utilizando uma fila em ambas extremidades
deq = deque([20, 40, 60, 80])
deq.appendleft(10)
deq.append(90)
deq.popleft()
deq.pop()
print(deq)