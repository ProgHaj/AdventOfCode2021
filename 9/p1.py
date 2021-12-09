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


risk_lvl = 0

for i in range(m):
    for j in range(n):
        curr = arr2d[i][j]
        above = arr2d[i - 1][j] if i - 1 >= 0 else None
        below = arr2d[i + 1][j] if i + 1 < m else None
        left = arr2d[i][j - 1] if j - 1 >= 0 else None
        right = arr2d[i][j + 1] if j + 1 < n else None

        if all(dir > curr for dir in [above, below, left, right] if dir is not None):
            risk_lvl += curr + 1
            print(i, j, ":", curr)

print(risk_lvl)
