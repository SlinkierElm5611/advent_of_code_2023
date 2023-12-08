import math

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

def not_all_end_in_z(locations: list[str]) -> bool:
    for location in locations:
        if location[2] != "Z":
            return True 
    return False

def day8_part_2():
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
    current_locations: list[str] = [location for location in map.keys() if location[2] == "A"]
    steps_taken: list[int] = []
    while len(steps_taken) < len(current_locations):
        direction: str = instructions[number_of_steps%len(instructions)]
        number_of_steps += 1
        for i in range(len(current_locations)):
            current_locations[i] = map[current_locations[i]][direction == "R"]
            if current_locations[i][2] == "Z":
                steps_taken.append(number_of_steps)
    set_of_steps_taken = set(steps_taken)
    print(math.lcm(*set_of_steps_taken))
