import numpy as np

inps = open("input", "r").readlines()

arr2d = []

for line in inps:
    array = []
    for numb in line.strip():
        array.append(int(numb))

    arr2d.append(array)

arr2d = np.array(arr2d)
m, n = arr2d.shape


basins = np.array([[0] * n] * m)
basin_list = []

for i in range(m):
    for j in range(n):
        curr = arr2d[i][j]
        above = arr2d[i - 1][j] if i - 1 >= 0 else None
        below = arr2d[i + 1][j] if i + 1 < m else None
        left = arr2d[i][j - 1] if j - 1 >= 0 else None
        right = arr2d[i][j + 1] if j + 1 < n else None

        if all(dir > curr for dir in [above, below, left, right] if dir is not None):
            basins[i, j] += 1
            basin_list.append((i, j))


def get_val(arr2d, i, j):
    m, n = arr2d.shape
    return arr2d[i][j] if i >= 0 and i < m and j >= 0 and j < n else None


def is_contender(arr2d, curr, *coord):
    val = get_val(arr2d, *coord)

    if val is not None and val > curr and val != 9:
        return True


def get_contender_neighbours(arr2d, curr, i, j):

    above = (i - 1, j)
    below = (i + 1, j)
    left = (i, j - 1)
    right = (i, j + 1)
    contenders = set()

    for coord in [above, below, left, right]:
        if is_contender(arr2d, curr, *coord):
            contenders.add(coord)

    return contenders


basin_areas = []

for basin in basin_list:
    need_check = [basin]
    visited = set()
    part_of_basin = set()

    while need_check:
        contender = need_check.pop()
        val = get_val(arr2d, *contender)
        part_of_basin.add(contender)
        visited.add(contender)
        poss_contenders = get_contender_neighbours(arr2d, val, *contender)

        new_checks = list(poss_contenders - visited)
        need_check.extend(new_checks)

    basin_areas.append(part_of_basin)

basin_areas = [len(area) for area in basin_areas]
basin_areas.sort()

print(basin_areas[-3:], np.prod(basin_areas[-3:]))