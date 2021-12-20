from typing import Counter


lines = open("input", "r").readlines()

start_seq = lines[0].strip()
mappings = {}

for line in lines[2:]:
    line = line.strip()

    key, val = line.split(" -> ")
    mappings[key] = val


steps = 10
seq = start_seq
for step in range(steps):
    i = 0
    while True:
        if i >= len(seq) - 1:  # Finished step
            break

        letters = seq[i] + seq[i + 1]
        extra = mappings.get(letters)
        if extra:
            seq = seq[: i + 1] + extra + seq[i + 1 :]
            i += 1

        i += 1
    print("step", step)


print("finished")
quant = Counter()

for char in seq:
    quant[char] += 1

res = quant.most_common()
print(res)
print(res[0][1] - res[-1][1])