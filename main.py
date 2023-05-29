import random


palya_szelesseg = 60
palya_magassag = 30

piton_x = random.randint(1, palya_szelesseg-2)
piton_y = random.randint(1, palya_magassag-2)


palya = [[' ' for _ in range(palya_szelesseg)] for _ in range(palya_magassag)]

for i in range(palya_magassag):
    palya[i][0] = '*'
    palya[i][palya_szelesseg-1] = '*'
for j in range(palya_szelesseg):
    palya[0][j] = '*'
    palya[palya_magassag-1][j] = '*'


palya[piton_y][piton_x] = '@'


for sor in palya:
    print(''.join(sor))
print("Hova?")


while True:
    parancs = input()

    if parancs == "meguntam":
        break


    if parancs == "balra":
        piton_x -= 1
    elif parancs == "jobbra":
        piton_x += 1
    elif parancs == "fel":
        piton_y -= 1
    elif parancs == "le":
        piton_y += 1


    if palya[piton_y][piton_x] == '*':
        print("Most ennyi volt, szép napot!")
        break


    palya[piton_y][piton_x] = '@'

    for sor in palya:
        print(''.join(sor))
    print("Hova?")