import csv


with open("game.txt", 'r', encoding='utf8') as fl: # открытие файла
    data = list(csv.reader(fl, delimiter='$', quotechar='"'))
    data = data[1:]

for line in data:
    tmp = line[2].split(':')
    if tmp[1] == '55':
        print(f"У персонажа\t{line[1]}\tв игре\t{line[0]}\tнашлась ошибка с кодом:\t{line[2]}.\tДата фиксации:\t{line[3]}")
        line[2] = 'Done'
        line[3] = '0000-00-00'

ans = []
for line in data:
    ans.append('$'.join(line) + '\n')

with open("game_new.csv", 'w', encoding='utf8') as fl: # запись файла
    fl.write("GameName$characters$nameError$date")
    fl.writelines(ans)
