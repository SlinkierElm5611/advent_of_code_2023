def day3_part_1():
    input_text = open("day3.txt", "r")
    lines = input_text.readlines()
    symbol_set: set[tuple[int,int]] = set()
    for i, line in enumerate(lines):
        line = line.strip()
        for j, char in enumerate(line):
            if not char.isdigit() and char != ".":
                symbol_set.add((j,i))
    current_sum = 0
    for j, line in enumerate(lines):
        working_str = ""
        current_int_adjacent = False
        for i, char in enumerate(line):
            if char.isdigit():
                working_str += char
                for x in range(-1,2):
                    for y in range(-1,2):
                        if (i+x,j+y) in symbol_set:
                            current_int_adjacent = True
            elif working_str != "":
                current_int = int(working_str)
                if current_int_adjacent:
                    current_sum += current_int
                current_int_adjacent = False
                working_str = ""
    print(current_sum)

def day3_part_2():
    input_text = open("day3.txt", "r")
    lines = input_text.readlines()
    symbol_set: dict[tuple[int,int], set[int]] = dict() 
    for i, line in enumerate(lines):
        line = line.strip()
        for j, char in enumerate(line):
            if char == "*":
                symbol_set[(j,i)] = []
    current_sum = 0
    for j, line in enumerate(lines):
        working_str = ""
        current_int_adjacent = False
        adjacent_set: set[tuple[int,int]] = set()
        for i, char in enumerate(line):
            if char.isdigit():
                working_str += char
                for x in range(-1,2):
                    for y in range(-1,2):
                        if (i+x,j+y) in symbol_set:
                            current_int_adjacent = True
                            adjacent_set.add((i+x,j+y))
            elif working_str != "":
                current_int = int(working_str)
                if current_int_adjacent:
                    for symbol in adjacent_set:
                        symbol_set[symbol].append(current_int)
                current_int_adjacent = False
                adjacent_set.clear()
                working_str = ""
    for symbol in symbol_set:
        if len(symbol_set[symbol]) == 2:
            current_sum += symbol_set[symbol][0] * symbol_set[symbol][1]
    print(current_sum)
