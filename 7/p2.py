import numpy as np
import json

inp = np.array(json.load(open("input", "r")))


def steps(step):
    if step == 0:
        return 0

    return steps(step - 1) + 1


def calc_steps(inp, val):
    steps = abs(inp - val)

    sum = 0
    for step in steps:
        for i in range(int(step)):
            sum += i + 1

    return sum


def find_best_step(inp, direction=1, init_val=None):
    if init_val is None:
        init_val = round(np.mean(inp))

    curr = calc_steps(inp, init_val)
    next = calc_steps(inp, init_val + direction)
    if next > curr:
        next = calc_steps(inp, init_val - direction)

        if next > curr:
            return curr
        else:
            direction = -1

    return find_best_step(inp, direction=direction, init_val=init_val + direction)


print(find_best_step(inp))