hexa_str = open("input", "r").read().strip()
inp_val = int(hexa_str, 16)

bits = len(hexa_str) * 4

print(hexa_str, bits)


def extract_bits(val, end, length):
    return (val >> (bits - end)) & length


sum_package_versions = 0


def parse_package(inp_val, i=0):
    global sum_package_versions
    i += 3
    package_ver = extract_bits(inp_val, i, 0b111)
    versions = [package_ver]
    print(package_ver)
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

        print(total)
    else:
        i += 1
        length_type_id = extract_bits(inp_val, i, 0b1)
        if length_type_id == 0:
            i += 15
            length_of_subpack = extract_bits(inp_val, i, 0b111111111111111)
            stop = i + length_of_subpack
            while i < stop:
                i, sub_version = parse_package(inp_val=inp_val, i=i)
                versions.extend(sub_version)
        elif length_type_id == 1:
            i += 11
            number_of_subpacks = extract_bits(inp_val, i, 0b11111111111)
            for _ in range(number_of_subpacks):
                i, sub_version = parse_package(inp_val=inp_val, i=i)
                versions.extend(sub_version)
        else:
            raise

    return i, versions


i, versions = parse_package(inp_val, i=0)
print(sum(versions), versions)