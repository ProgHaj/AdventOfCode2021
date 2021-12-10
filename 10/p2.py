inp = open("input", "r").readlines()

closers = {"}": "{", "]": "[", ">": "<", ")": "("}
openers = {"{": "}", "[": "]", "<": ">", "(": ")"}

point_map = {")": 1, "]": 2, "}": 3, ">": 4}

points = 0

scores = []
for line in inp:
    invalid = False
    queue = []
    for i, val in enumerate(line.strip()):
        close = closers.get(val)

        if close:
            opener = queue.pop()
            if opener != close:
                invalid = True
                break
        else:
            queue.append(val)

    if invalid:
        continue

    complete_needed = []
    score = 0
    while queue:
        cur = queue.pop()
        next_closer = openers[cur]
        complete_needed.append(next_closer)
        score *= 5
        score += point_map[next_closer]

    scores.append(score)
    print(complete_needed)

scores.sort()
print(scores[len(scores) // 2])
