from collections import Counter

lines = open("input", "r").readlines()

# STATS
# Totals:
# a = 8
# b = 6
# c = 8
# d = 7
# e = 4
# f = 9
# g = 7

# 0 = abcefg
# 1 = cf
# 2 = acdeg
# 3 = acdfg
# 4 = bcdf
# 5 = abdfg
# 6 = abdefg
# 7 = acf
# 8 = abcdefg
# 9 = abcdfg

# e = 4 entries total
# b = 6 entries total
# a = {7} - {1}
# c = part of 1, 8 entries total
# f = part of 1, 9 entries total
# d = part of 4, easy after we calculated b,c,f
# g = only left after everything else


real_number_mapping = {
    "abcefg": 0,
    "cf": 1,
    "acdeg": 2,
    "acdfg": 3,
    "bcdf": 4,
    "abdfg": 5,
    "abdefg": 6,
    "acf": 7,
    "abcdefg": 8,
    "abcdfg": 9,
}

# 1, 4, 7, 8
comb = {2: 1, 3: 7, 4: 4, 7: 8}


def collect_all_numbers(numbers):
    number_list = []
    number_char_mapping = {}
    char_number_mapping = {}
    for number in numbers:
        number_set = set(number)
        if number_set not in number_list:
            number_list.append(number_set)
            correct_numb = comb.get(len(number_set))
            if correct_numb:
                number_char_mapping[correct_numb] = number_set
                char_number_mapping["".join(sorted(number_set))] = correct_numb

    # totals
    totals = Counter()
    for number_set in number_list:
        for val in number_set:
            totals[val] += 1

    assert number_char_mapping.keys() == set([1, 4, 7, 8])
    char_mapping = {}
    a_key = (number_char_mapping[7] - number_char_mapping[1]).pop()  # One value
    char_mapping[a_key] = "a"
    print(totals.values())
    for key, val in totals.items():
        if val == 4:
            char_mapping[key] = "e"

        if val == 6:
            char_mapping[key] = "b"

        if key in number_char_mapping[1]:
            if val == 8:
                char_mapping[key] = "c"

            if val == 9:
                char_mapping[key] = "f"

    for char_val in number_char_mapping[4]:
        if char_val not in char_mapping.keys():
            char_mapping[char_val] = "d"
            break

    for char_val in number_char_mapping[8]:
        if char_val not in char_mapping.keys():
            char_mapping[char_val] = "g"
            break

    for number_set in number_list:
        real_chars = set()
        for fake_char in number_set:
            real_chars.add(char_mapping[fake_char])

        # Sets fake chars to real numbers
        char_number_mapping["".join(sorted(number_set))] = real_number_mapping[
            "".join(sorted(real_chars))
        ]

    return char_number_mapping


numbers = []
output_numbers = []
for line in lines:
    numbers, output_numbs = line.split("|")
    output_numbs = output_numbs.strip().split(" ")
    numbers = numbers.strip().split(" ")

    char_number_mapping = collect_all_numbers(numbers)

    output = []

    for number in output_numbs:
        key = "".join(sorted(set(number)))
        output.append(str(char_number_mapping[key]))

    print(output)
    output_numbers.append(int("".join(output)))

print(output_numbers)
print(sum(output_numbers))