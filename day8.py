def day8_part_1():
    input_file = open("day8.txt", "r")
    instructions: str = ""
    map: dict[str, tuple[str,str]] = {}
    for index, line in enumerate(input_file):
        line = line.strip()
        if index == 0:
            instructions = line
        else:
            if line != "":
                map[line[0:3]] = (line[7:10], line[12:15])
    input_file.close()
    number_of_steps: int = 0
    current_location: str = "AAA"
    while current_location != "ZZZ":
        direction: str = instructions[number_of_steps%len(instructions)]
        number_of_steps += 1
        current_location = map[current_location][direction == "R"]
    print(number_of_steps)
