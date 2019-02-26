from random import choice
import os
clear = lambda: os.system('cls')
words = ["голубь", "слово", ]
vs = ["",
      ["", "|      ", "|    ", "|    ", "|      ", "|     "],
      ["", "|___|__", "|   |", "|    ", "|      ", "|     "],
      ["", "|___|__", "|   |", "|   o", "|      ", "|     "],
      ["", "|___|__", "|   |", "|   o", "|      ", "|     "],
      ["", "|___|__", "|   |", "|   o", "|   0  ", "|     "],
      ["", "|___|__", "|   |", "|   o", "|  /0\\ ", "|     "],
      ["", "|___|__", "|   |", "|   o", "|  /0\\ ", "|  / \\"]]
print(*vs[-1], sep='\n')
i = 1
fl = False
nu = set()
print("Введите 1, если хотите ввести слово, или 2, если хотите выбрать из стандартных")
k = input()
if k == '1':
    print('Введите слово:')
    word = input()
elif k == '2':
    word = choice(words)
else:
    print("Ощибка. Выбрано случайное слово")
    word = choice(words)
word = word.upper()
w1 = "_"*len(word)
w1 = list(w1)
while i < 8 and not fl:
    print("Неугаданные буквы:")
    print(*nu)
    print("Напишите букву")
    ch = input().upper()
    clear()
    while len(ch) > 1:
        print("Ошибка, введите букву")
        ch = input().upper()
        print(ch)

    if ch not in word:
        print("Не угадал, oшибка ", i, " из 7")
        nu.add(ch)
        i += 1
        print(*w1, sep=" ")
        print(*vs[-i], sep="\n")
    else:
        print("Угадал")
        indexes = [j for j in range(len(word)) if word[j] == ch]
        for j in indexes:
            w1[j] = ch
        print(*w1, sep=" ")
        print(*vs[-i], sep="\n")
    if "_" not in w1:
        fl = True
if not fl:
    print("Изначальное слово: ", word)
else:
    print("Ура, вы выиграли")
