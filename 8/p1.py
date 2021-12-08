lines = open("input", "r").readlines()
comb = {2: 1, 3: 7, 4: 4, 7: 8}


ans = 0

for line in lines:
    numbers = line.split("|")[1].strip().split(" ")
    for number in numbers:
        if comb.get(len(number)):
            ans += 1

print(ans)