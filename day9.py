def day9_part_1():
    input_file = open("day9.txt", "r")
    predicted_values: list[int] = []
    sum: int = 0
    for line in input_file.readlines():
        line: str = line.strip()
        working_values: list[list[int]] = [[int(value) for value in line.split(" ")]]
        for values in working_values:
            current_values: list[int] = [values[i]-values[i-1] for i in range(1, len(values))] 
            working_values.append(current_values)
            if len(set(current_values)) == 1 and current_values[0] == 0:
                break
        while len(working_values) > 1:
            last_values: list[int] = working_values.pop()
            working_values[-1].append(working_values[-1][-1] + last_values[-1])
        sum += working_values[0][-1]
    print(sum)

def day9_part_2():
    input_file = open("day9.txt", "r")
    predicted_values: list[int] = []
    sum: int = 0
    for line in input_file.readlines():
        line: str = line.strip()
        working_values: list[list[int]] = [[int(value) for value in line.split(" ")]]
        for values in working_values:
            current_values: list[int] = [values[i]-values[i-1] for i in range(1, len(values))] 
            working_values.append(current_values)
            if len(set(current_values)) == 1 and current_values[0] == 0:
                break
        while len(working_values) > 1:
            last_values: list[int] = working_values.pop()
            working_values[-1].insert(0, working_values[-1][0] - last_values[0])
        sum += working_values[0][0]
    print(sum)
