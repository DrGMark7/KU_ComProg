n = int(input())
grenade_coordinate = []
enemy_coordinate = []
kill_count = 0

# input
for i in range(n):
    row = [x for x in input()]
    # grenade_coordinate
    grenade_index = [(i, y) for y, e in enumerate(row) if e == "G"]
    grenade_coordinate.extend(grenade_index)

    # enemy_coordinate
    enemy_index = [(i, y) for y, e in enumerate(row) if e == "E"]
    enemy_coordinate.extend(enemy_index)

# check
for i, e in enumerate(enemy_coordinate):
    for g in grenade_coordinate:
        # if in grenade radius
        if -2 <= (e[0] - g[0]) <= 2 and -2 <= (e[1] - g[1]) <= 2:
            kill_count += 1
            break


print(kill_count)