import numpy as np

dots = []
max_x = 0
max_y = 0
instructions = []

parse_map = True

with open("input", "r") as f:
    lines = f.readlines()

    for line in lines:
        line = line.strip()
        if not line:
            parse_map = False
        elif parse_map:
            val_y, val_x = line.split(",")
            val_x = int(val_x)
            val_y = int(val_y)
            if val_x > max_x:
                max_x = val_x

            if val_y > max_y:
                max_y = val_y

            dots.append((val_x, val_y))

        else:
            instruction = line.split(" ")[-1]
            instruction_parsed = instruction.split("=")
            inst_map = {instruction_parsed[0]: int(instruction_parsed[1])}
            instructions.append((inst_map.get("x"), inst_map.get("y")))

print(max_x, max_y)
print(type(max_x), type(max_y))

np_dots = np.zeros((max_x + 1, max_y + 1)).astype(bool)
for dot in dots:
    np_dots[dot[0], dot[1]] = True


print(np_dots)
print(instructions)
print()

for instruction in instructions[:]:  # p1 instructions[:1]
    flip_x = instruction[0]
    flip_y = instruction[1]
    shape = np_dots.shape

    if flip_y is not None:
        flipped_dots = np.flip(np_dots, axis=0)
        flip_y_2 = shape[0] - flip_y - 1
        np_zero_y = max(flip_y_2 - flip_y, 0)
        np_zero_y_2 = max(flip_y - flip_y_2, 0)
        res1 = np.concatenate(
            (np_dots[:flip_y, :], np.zeros((np_zero_y, shape[1])).astype(bool))
        )
        res2 = np.concatenate(
            (np.zeros((np_zero_y_2, shape[1])).astype(bool), flipped_dots[:flip_y_2, :])
        )
        res = res1 + res2

    if flip_x is not None:
        flipped_dots = np.flip(np_dots, axis=1)
        res = np_dots[:, :flip_x] + flipped_dots[:, :flip_x]

        flipped_dots = np.flip(np_dots, axis=1)
        flip_x_2 = shape[1] - flip_x - 1
        print(flip_x, flip_x_2)
        np_zero_x = max(flip_x_2 - flip_x, 0)
        np_zero_x_2 = max(flip_x - flip_x_2, 0)
        res1 = np.concatenate(
            (np_dots[:, :flip_x], np.zeros((shape[0], np_zero_x)).astype(bool)), axis=1
        )
        res2 = np.concatenate(
            (
                np.zeros((shape[0], np_zero_x_2)).astype(bool),
                flipped_dots[:, :flip_x_2],
            ),
            axis=1,
        )
        res = res1 + res2

    np_dots = res
    print(np_dots)
    print()


for row in np_dots:
    for val in row:
        print("." if not val else "#", end="")

    print()

print(np.sum(np_dots))