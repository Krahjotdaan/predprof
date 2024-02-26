import csv
import string


def hash(s):
    p = 67
    m = 10 ** 9 + 9
    d = {}
    char = string.ascii_letters + string.digits + ":-'."
    for i, l in enumerate(char, 1):
        d[l] = i

    hs = 0
    for i in range(len(s)):
        hs += (d[s[i]] * p ** i) % m

    return str(hs)


with open("game.txt", 'r', encoding='utf8') as fl:
    data = list(csv.reader(fl, delimiter='$', quotechar='"'))
    data = data[1:]

for line in data:
    st = line[0] + line[1]
    st = st.split()
    st = ''.join(st)
    hs = hash(st)
    line.reverse()
    line.append(hs)
    line.reverse()

ans = []
for line in data:
    ans.append('$'.join(line) + '\n')

with open("game_with_hash.csv", 'w', encoding='utf8') as fl:
    fl.write("Hash$GameName$characters$nameError$date")
    fl.writelines(ans)


