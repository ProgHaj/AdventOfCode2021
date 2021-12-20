hexa_str = open("input", "r").read().strip()
inp_val = int(hexa_str, 16)

bits = len(hexa_str) * 4

print(hexa_str, bits)


def extract_bits(val, end, length):
    return (val >> (bits - end)) & length


def product(x):
    prod = 1
    for val in x:
        prod *= val

    return prod


def gt(x):
    return int(x[0] > x[1])


def lt(x):
    return int(x[0] < x[1])


def eq(x):
    return int(x[0] == x[1])


sum_package_versions = 0
operand = {
    0: sum,
    1: product,
    2: min,
    3: max,
    5: gt,
    6: lt,
    7: eq,
}


def parse_package(inp_val, i=0):
    global sum_package_versions
    i += 3
    package_ver = extract_bits(inp_val, i, 0b111)
    i += 3
    package_type = extract_bits(inp_val, i, 0b111)

    if package_type == 4:
        should_cont = 1
        total = 0
        while should_cont:
            i += 1
            should_cont = extract_bits(inp_val, i, 0b1)
            i += 4
            val = extract_bits(inp_val, i, 0b1111)
            total = (total << 4) + val

        val = total
    else:
        i += 1
        length_type_id = extract_bits(inp_val, i, 0b1)
        op = operand[package_type]
        values = []
        if length_type_id == 0:
            i += 15
            length_of_subpack = extract_bits(inp_val, i, 0b111111111111111)
            stop = i + length_of_subpack
            while i < stop:
                i, value = parse_package(inp_val=inp_val, i=i)
                values.append(value)

        elif length_type_id == 1:
            i += 11
            number_of_subpacks = extract_bits(inp_val, i, 0b11111111111)
            for _ in range(number_of_subpacks):
                i, value = parse_package(inp_val=inp_val, i=i)
                values.append(value)
        else:
            raise

        val = op(values)

    return i, val


i, value = parse_package(inp_val, i=0)
print(i, value)