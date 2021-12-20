import numpy as np

lines = open("test_input", "r").readlines()
array = np.array([list(line.strip()) for line in lines]).astype(int)
res_array = np.zeros(array.shape).astype(int)
from_array = [[None] * array.shape[0] for i in range(array.shape[1])]

print(array)
print(res_array)

from_array[0][0] = "START"

print(np.array(from_array))
a = 0


def dynamic_lesgo(x, y):
    global res_array, from_array, a
    print(x, y)
    if not x and not y:
        return

    a += 1

    val = array[x, y]
    vals = []
    if x - 1 >= 0:
        vals.append((res_array[x - 1, y] + val, (x - 1, y)))
    if y - 1 >= 0:
        vals.append((res_array[x, y - 1] + val, (x, y - 1)))

    print(vals)
    vals.sort(key=lambda x: x[0])
    print(vals)
    best_val = vals[0]
    res_array[x, y] = best_val[0]
    from_array[x][y] = best_val[1]


current_x = 0
current_y = 0
while current_x < array.shape[0] and current_y < array.shape[1]:
    print(current_x, current_y)
    for x in range(current_x, array.shape[0]):
        dynamic_lesgo(x, current_y)

    for y in range(current_y, array.shape[1]):
        dynamic_lesgo(current_x, y)

    current_x += 1
    current_y += 1


print(res_array)
print(res_array[-1, -1])
