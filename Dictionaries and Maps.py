#d = {key1: value1, key2: value2}
# print(movie['director'])

n = int(input())
d = dict()

for _ in range(0, n):
    name, number = input().split()
    d[name] = number

while True:
    try:
        name = input()
        if name in d:
            print('{}={}'.format(name, d[name]))
        else:
            print(d.get("", "Not found"))
    except EOFError:
        break
