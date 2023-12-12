def day12_part_1():
    input_file = open("day12.txt", "r")
    sum_of_arrangements: int = 0
    for line in input_file.readlines():
        line = line.strip()
        split_line = line.split(" ")
        damaged_record: str = split_line[0]
        while ".." in damaged_record:
            damaged_record = damaged_record.replace("..", ".")
        damaged_record = damaged_record.strip(".")
        numbers: list[int] = [int(x) for x in split_line[1].split(",")]
        stack: list[tuple[str, int]] = [("", 0)]
        while stack:
            working_str, record_index = stack.pop()
            if len(working_str) == len(damaged_record):
                is_valid: bool = True
                broken_springs: list[int] = []
                temp: int = 0
                for char in working_str:
                    if char == "#":
                        temp += 1
                    else:
                        if temp != 0:
                            broken_springs.append(temp)
                            temp = 0
                if temp != 0:
                    broken_springs.append(temp)
                if broken_springs != numbers:
                    is_valid = False
                if is_valid:
                    sum_of_arrangements += 1
                continue
            else:
                if damaged_record[record_index] == "?":
                    stack.append((working_str + "#", record_index+ 1))
                    stack.append((working_str + ".", record_index + 1))
                else:
                    stack.append((working_str + damaged_record[record_index], record_index + 1))
    print(sum_of_arrangements)
