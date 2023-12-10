def day10_part_1():
    input_string: str = open('day10.txt', 'r').read()
    input_string = input_string.strip()
    map = [ line for line in input_string.split("\n")]
    position_of_start: tuple[int,int] = None
    for i, line in enumerate(map):
        for j, character in enumerate(line):
            if character == "S":
                position_of_start = (i, j)
    distances: dict[tuple[int,int], int] = {position_of_start: 0}
    stack_of_positions: list[tuple[int,int]] = [position_of_start]
    while stack_of_positions:
        current_position = stack_of_positions.pop(0)
        current_pipe = map[current_position[0]][current_position[1]]
        if current_pipe == "S":
            if current_position[0] > 0:
                pipe_below = map[current_position[0] + 1][current_position[1]]
                if pipe_below in {"|", "L", "J"}:
                    stack_of_positions.append((current_position[0] + 1, current_position[1]))
                    distances[(current_position[0] + 1, current_position[1])] = distances[current_position] + 1
            if current_position[0] < len(map) - 1:
                pipe_above = map[current_position[0] - 1][current_position[1]]
                if pipe_above in {"|", "7", "F"}:
                    stack_of_positions.append((current_position[0] - 1, current_position[1]))
                    distances[(current_position[0] - 1, current_position[1])] = distances[current_position] + 1
            if current_position[1] > 0:
                pipe_left = map[current_position[0]][current_position[1] - 1]
                if pipe_left in {"-", "L", "F"}:
                    stack_of_positions.append((current_position[0], current_position[1] - 1))
                    distances[(current_position[0], current_position[1] - 1)] = distances[current_position] + 1
            if current_position[1] < len(map[0]) - 1:
                pipe_right = map[current_position[0]][current_position[1] + 1]
                if pipe_right in {"-", "7", "J"}:
                    stack_of_positions.append((current_position[0], current_position[1] + 1))
                    distances[(current_position[0], current_position[1] + 1)] = distances[current_position] + 1
        elif current_pipe == "F":
            if (current_position[0] + 1, current_position[1]) not in distances:
                stack_of_positions.append((current_position[0] + 1, current_position[1]))
                distances[(current_position[0] + 1, current_position[1])] = distances[current_position] + 1
            if (current_position[0], current_position[1] + 1) not in distances:
                stack_of_positions.append((current_position[0], current_position[1] + 1))
                distances[(current_position[0], current_position[1] + 1)] = distances[current_position] + 1
        elif current_pipe == "|":
            if (current_position[0] - 1, current_position[1]) not in distances:
                stack_of_positions.append((current_position[0] - 1, current_position[1]))
                distances[(current_position[0] - 1, current_position[1])] = distances[current_position] + 1
            if (current_position[0] + 1, current_position[1]) not in distances:
                stack_of_positions.append((current_position[0] + 1, current_position[1]))
                distances[(current_position[0] + 1, current_position[1])] = distances[current_position] + 1
        elif current_pipe == "-":
            if (current_position[0], current_position[1] - 1) not in distances:
                stack_of_positions.append((current_position[0], current_position[1] - 1))
                distances[(current_position[0], current_position[1] - 1)] = distances[current_position] + 1
            if (current_position[0], current_position[1] + 1) not in distances:
                stack_of_positions.append((current_position[0], current_position[1] + 1))
                distances[(current_position[0], current_position[1] + 1)] = distances[current_position] + 1
        elif current_pipe == "J":
            if (current_position[0] - 1, current_position[1]) not in distances:
                stack_of_positions.append((current_position[0] - 1, current_position[1]))
                distances[(current_position[0] - 1, current_position[1])] = distances[current_position] + 1
            if (current_position[0], current_position[1] - 1) not in distances:
                stack_of_positions.append((current_position[0], current_position[1] - 1))
                distances[(current_position[0], current_position[1] - 1)] = distances[current_position] + 1
        elif current_pipe == "L":
            if (current_position[0] - 1, current_position[1]) not in distances:
                stack_of_positions.append((current_position[0] - 1, current_position[1]))
                distances[(current_position[0] - 1, current_position[1])] = distances[current_position] + 1
            if (current_position[0], current_position[1] + 1) not in distances:
                stack_of_positions.append((current_position[0], current_position[1] + 1))
                distances[(current_position[0], current_position[1] + 1)] = distances[current_position] + 1
        elif current_pipe == "7":
            if (current_position[0] + 1, current_position[1]) not in distances:
                stack_of_positions.append((current_position[0] + 1, current_position[1]))
                distances[(current_position[0] + 1, current_position[1])] = distances[current_position] + 1
            if (current_position[0], current_position[1] - 1) not in distances:
                stack_of_positions.append((current_position[0], current_position[1] - 1))
                distances[(current_position[0], current_position[1] - 1)] = distances[current_position] + 1
    print(max(distances.values()))

def day10_part_2():
    input_string: str = open('day10.txt', 'r').read()
    input_string = input_string.strip()
    map = [ [char for char in line] for line in input_string.split("\n")]
    position_of_start: tuple[int,int] = None
    for i, line in enumerate(map):
        for j, character in enumerate(line):
            if character == "S":
                position_of_start = (i, j)
    distances: dict[tuple[int,int], int] = {position_of_start: 0}
    stack_of_positions: list[tuple[int,int]] = [position_of_start]
    while stack_of_positions:
        current_position = stack_of_positions.pop(0)
        current_pipe = map[current_position[0]][current_position[1]]
        if current_pipe == "S":
            if current_position[0] > 0:
                pipe_below = map[current_position[0] + 1][current_position[1]]
                if pipe_below in {"|", "L", "J"}:
                    stack_of_positions.append((current_position[0] + 1, current_position[1]))
                    distances[(current_position[0] + 1, current_position[1])] = distances[current_position] + 1
            if current_position[0] < len(map) - 1:
                pipe_above = map[current_position[0] - 1][current_position[1]]
                if pipe_above in {"|", "7", "F"}:
                    stack_of_positions.append((current_position[0] - 1, current_position[1]))
                    distances[(current_position[0] - 1, current_position[1])] = distances[current_position] + 1
            if current_position[1] > 0:
                pipe_left = map[current_position[0]][current_position[1] - 1]
                if pipe_left in {"-", "L", "F"}:
                    stack_of_positions.append((current_position[0], current_position[1] - 1))
                    distances[(current_position[0], current_position[1] - 1)] = distances[current_position] + 1
            if current_position[1] < len(map[0]) - 1:
                pipe_right = map[current_position[0]][current_position[1] + 1]
                if pipe_right in {"-", "7", "J"}:
                    stack_of_positions.append((current_position[0], current_position[1] + 1))
                    distances[(current_position[0], current_position[1] + 1)] = distances[current_position] + 1
        elif current_pipe == "F":
            if (current_position[0] + 1, current_position[1]) not in distances:
                stack_of_positions.append((current_position[0] + 1, current_position[1]))
                distances[(current_position[0] + 1, current_position[1])] = distances[current_position] + 1
            if (current_position[0], current_position[1] + 1) not in distances:
                stack_of_positions.append((current_position[0], current_position[1] + 1))
                distances[(current_position[0], current_position[1] + 1)] = distances[current_position] + 1
        elif current_pipe == "|":
            if (current_position[0] - 1, current_position[1]) not in distances:
                stack_of_positions.append((current_position[0] - 1, current_position[1]))
                distances[(current_position[0] - 1, current_position[1])] = distances[current_position] + 1
            if (current_position[0] + 1, current_position[1]) not in distances:
                stack_of_positions.append((current_position[0] + 1, current_position[1]))
                distances[(current_position[0] + 1, current_position[1])] = distances[current_position] + 1
        elif current_pipe == "-":
            if (current_position[0], current_position[1] - 1) not in distances:
                stack_of_positions.append((current_position[0], current_position[1] - 1))
                distances[(current_position[0], current_position[1] - 1)] = distances[current_position] + 1
            if (current_position[0], current_position[1] + 1) not in distances:
                stack_of_positions.append((current_position[0], current_position[1] + 1))
                distances[(current_position[0], current_position[1] + 1)] = distances[current_position] + 1
        elif current_pipe == "J":
            if (current_position[0] - 1, current_position[1]) not in distances:
                stack_of_positions.append((current_position[0] - 1, current_position[1]))
                distances[(current_position[0] - 1, current_position[1])] = distances[current_position] + 1
            if (current_position[0], current_position[1] - 1) not in distances:
                stack_of_positions.append((current_position[0], current_position[1] - 1))
                distances[(current_position[0], current_position[1] - 1)] = distances[current_position] + 1
        elif current_pipe == "L":
            if (current_position[0] - 1, current_position[1]) not in distances:
                stack_of_positions.append((current_position[0] - 1, current_position[1]))
                distances[(current_position[0] - 1, current_position[1])] = distances[current_position] + 1
            if (current_position[0], current_position[1] + 1) not in distances:
                stack_of_positions.append((current_position[0], current_position[1] + 1))
                distances[(current_position[0], current_position[1] + 1)] = distances[current_position] + 1
        elif current_pipe == "7":
            if (current_position[0] + 1, current_position[1]) not in distances:
                stack_of_positions.append((current_position[0] + 1, current_position[1]))
                distances[(current_position[0] + 1, current_position[1])] = distances[current_position] + 1
            if (current_position[0], current_position[1] - 1) not in distances:
                stack_of_positions.append((current_position[0], current_position[1] - 1))
                distances[(current_position[0], current_position[1] - 1)] = distances[current_position] + 1
    count: int = 0
    start_of_lines: set[tuple[int,int]] = {"F", "L"}
    end_of_lines: set[tuple[int,int]] = {"J", "7"}
    for i, line in enumerate(map):
        in_loop: bool = False
        start_of_line: Optional[str] = None
        for j, character in enumerate(line):
            if (i,j) in distances:
                if not start_of_line and character in start_of_lines:
                    start_of_line = character
                elif start_of_line and character in end_of_lines:
                    if character == "J" and start_of_line == "F" or character == "7" and start_of_line == "L":
                        in_loop = not in_loop
                    start_of_line = None
                elif not start_of_line:
                    in_loop = not in_loop
                last_pipe_distance = distances[(i,j)]
            else:
                last_pipe_distance = None
                if in_loop:
                    count += 1
    print(count)
