Grid_size = list(map(int, input("City Size: ").split()))
Map = []
for _ in range(Grid_size[0]):
    Map.append(list(map(int, input().split())))


#! Wrong how to fix best view

def Find_viewer(tower):

    def count_visible_buildings(building_heights):
        count = 0
        max_height = 0
        for height in building_heights:
            if height > max_height:
                max_height = height
                count += 1
        return count

    total_visible_buildings = 0

    for column in tower:
        total_visible_buildings += count_visible_buildings(column)

    return total_visible_buildings

#+ PASS
def Flip(direc,grid):
    num_rows = len(grid)
    num_cols = len(grid[0])
    new_map = []
    if direc == 'E':
        for row in grid[::-1]:
            new_map.append(row[::-1])
    elif direc == 'S':
        for col in range(num_cols - 1, -1, -1):
            new_row = []
            for row in range(num_rows):
                new_row.append(grid[row][col])
            new_map.append(new_row[::-1])
    elif direc == 'N':
        for col in range(num_cols - 1, -1, -1):
            new_row = []
            for row in range(num_rows):
                new_row.append(grid[row][col])
            new_map.append(new_row)
    elif direc == 'W':
        new_map = grid
    return new_map
    


direction = {'N':0,'S':0,'E':0,'W':0}
for d in direction.keys():
    direction[d] = Find_viewer(Flip(d,Map))
    #print(d,Find_viewer(Flip(d,Map)))

sorted_dict = dict(sorted(direction.items(), key=lambda item: item[1]))

max_key = max(direction, key=direction.get)
max_value = direction[max_key]

keys_with_desired_value = []

for key, value in sorted_dict.items():
    if value == max_value:
        keys_with_desired_value.append(key)

print(' '.join(keys_with_desired_value))