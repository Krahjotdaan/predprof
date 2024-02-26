import csv

with open("game.txt", 'r', encoding='utf8') as fl:
    data = list(csv.reader(fl, delimiter='$', quotechar='"'))
    data = data[1:]

data.sort()

name = input()

while name != "game":
    flag = False
    founded = False
    s = 0
    for line in data:
        if line[1] == name and flag == False:
            print(f"Персонаж {line[1]} встречается в играх:\n{line[0]}")
            flag = True
            founded = True
            s += 1
        elif line[1] == name and flag == True:
            print(line[0])
            s += 1
        elif s == 5:
            print('и др.')
            break

    if not founded:
        print("Этого персонажа не существует")

    name = input()
