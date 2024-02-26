import csv


with open("game.txt", 'r', encoding='utf8') as fl: # открытие файла
    data = list(csv.reader(fl, delimiter='$', quotechar='"'))
    data = data[1:]

counter = {}
for line in data: # подсчет значений
    counter[line[0]] = counter.get(line[0], 0) + 1


for line in data:
    line.append(str(counter[line[0]]))

ans = []
for line in data:
    ans.append('$'.join(line) + '\n')

with open("game_counter.csv", 'w', encoding='utf8') as fl: # запись файла
    fl.write("GameName$characters$nameError$date$counter")
    fl.writelines(ans)
