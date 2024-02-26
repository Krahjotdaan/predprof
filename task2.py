import csv


with open("game.txt", 'r', encoding='utf8') as fl:
    data = list(csv.reader(fl, delimiter='$', quotechar='"'))
    data = data[1:]

data.sort()
counter = {}
for line in data:
    counter[line[0]] = counter.get(line[0], 0) + 1

keys = counter.keys()

for key in keys:
    print(f"{key} - количество багов: {counter[key]}")
