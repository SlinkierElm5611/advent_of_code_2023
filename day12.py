def day12_part_1():
    input_file = open("day12.txt", "r")
    sum_of_arrangements: int = 0
    for line in input_file.readlines():
        line = line.strip()
        split_line = line.split(" ")
        damaged_record: str = split_line[0]
        numbers: list[int] = [int(x) for x in split_line[1].split(",")]
        total_num_damaged: int = sum(numbers)
