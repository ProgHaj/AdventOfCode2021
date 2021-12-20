from collections import deque, Counter


lines = open("input", "r").readlines()

start_seq = lines[0].strip()
mappings = {}

for line in lines[2:]:
    line = line.strip()

    key, val = line.split(" -> ")
    mappings[key] = val


print(start_seq)
seq = deque(start_seq)
print(seq)

entries = Counter()

seq = start_seq

entries = Counter()

for i in range(len(start_seq) - 1):
    entries[start_seq[i] + start_seq[i + 1]] += 1


print(entries)
steps = 40
for step in range(steps):
    i = 0
    new_entries = Counter()
    for key, val in entries.items():
        new_char = mappings[key]
        if not new_char:
            new_entries[key] += val
        else:
            key1 = key[0] + new_char
            key2 = new_char + key[1]
            new_entries[key1] += val
            new_entries[key2] += val

    entries = new_entries


print(entries)
print("finished")
quant = Counter({start_seq[-1]: 1})

for key, val in entries.items():
    quant[key[0]] += val

res = quant.most_common()
print(res)
print(res[0][1] - res[-1][1])