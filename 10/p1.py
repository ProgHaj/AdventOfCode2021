inp = open("input", "r").readlines()

closers = {"}": "{", "]": "[", ">": "<", ")": "("}

point_map = {")": 3, "]": 57, "}": 1197, ">": 25137}

points = 0

for line in inp:
    queue = []
    for i, val in enumerate(line.strip()):
        close = closers.get(val)

        if close:
            opener = queue.pop()
            if opener != close:
                points += point_map[val]
                print(val, points)
        else:
            queue.append(val)

print(points)