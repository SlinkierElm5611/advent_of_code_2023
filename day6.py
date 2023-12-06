import math
def day6_part_1():
    input_file = open("day6.txt", "r")
    input_lines = input_file.readlines()
    input_file.close()
    times: list[int]= [int(time) for time in input_lines[0].split(":")[1].strip().split(" ") if time != ""]
    distances: list[int] = [int(distance) for distance in input_lines[1].split(":")[1].strip().split(" ") if distance != ""]
    product: int = 1
    for race_index in range(len(times)):
        distance = distances[race_index]
        time = times[race_index]
        discriminant = time * time - 4 * distance
        min_x = math.ceil((time - discriminant ** 0.5) / 2)
        max_x = math.floor((time + discriminant ** 0.5) / 2)
        min_x = min_x + 1 if time * min_x - min_x*min_x <= distance else min_x 
        max_x = max_x - 1 if time * max_x -max_x*max_x<= distance else max_x
        product *= max_x - min_x + 1
    print(product)

def day6_part_2():
    input_file = open("day6.txt", "r")
    input_lines = input_file.readlines()
    input_file.close()
    time: int= int("".join([time for time in input_lines[0].split(":")[1].strip().split(" ") if time != ""]))
    distance: int = int("".join([distance for distance in input_lines[1].split(":")[1].strip().split(" ") if distance != ""]))
    discriminant = time * time - 4 * distance
    min_x = math.ceil((time - discriminant ** 0.5) / 2)
    max_x = math.floor((time + discriminant ** 0.5) / 2)
    min_x = min_x + 1 if time * min_x - min_x*min_x <= distance else min_x 
    max_x = max_x - 1 if time * max_x -max_x*max_x<= distance else max_x
    print(max_x - min_x + 1)
