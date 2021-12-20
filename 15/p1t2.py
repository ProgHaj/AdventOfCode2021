import numpy as np

lines = open("input", "r").readlines()
array = [list(line.strip()) for line in lines]
res_array = np.zeros(np.array(array).shape).astype(int)

network = {}

for i in range(len(array)):
    for j in range(len(array[i])):
        source = (i, j)
        targets = []
        if i - 1 >= 0:
            targets.append((i - 1, j))
        if i + 1 < len(array):
            targets.append((i + 1, j))
        if j - 1 >= 0:
            targets.append((i, j - 1))
        if j + 1 < len(array[i]):
            targets.append((i, j + 1))

        network[source] = [(targ, int(array[targ[0]][targ[1]])) for targ in targets]


queue = [((0, 0), 0, (0, 0))]
shape = res_array.shape
visited = set()
path = {}

while queue:
    coord, current_val, from_coord = queue.pop(0)
    if coord in visited:
        continue

    path[from_coord] = coord

    visited.add(coord)
    res_array[coord] = current_val
    if coord == (shape[0] - 1, shape[1] - 1):
        break

    targets = network[coord]
    new_targets = [
        (t[0], t[1] + current_val, coord) for t in targets if t[0] not in visited
    ]
    queue.extend(new_targets)
    queue.sort(key=lambda x: x[1])
    array[coord[0]][coord[1]]


print(res_array)
print(coord, shape, current_val, len(visited))
