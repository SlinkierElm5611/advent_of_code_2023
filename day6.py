def day6_part_1():
    input_file = open("day6.txt", "r")
    input_lines = input_file.readlines()
    input_file.close()
    times: list[int]= [int(time) for time in input_lines[0].split(":")[1].strip().split(" ") if time != ""]
    distances: list[int] = [int(distance) for distance in input_lines[1].split(":")[1].strip().split(" ") if distance != ""]
    product: int = 1
    for race_index in range(len(times)):
        sum = 0
        for t in range(times[race_index]+1):
            if t*(times[race_index] - t) > distances[race_index]:
                sum += 1
        if sum >=1:
            product *= sum
    print(product)

def day6_part_2():
    input_file = open("day6.txt", "r")
    input_lines = input_file.readlines()
    input_file.close()
    time: int= int("".join([time for time in input_lines[0].split(":")[1].strip().split(" ") if time != ""]))
    distance: int = int("".join([distance for distance in input_lines[1].split(":")[1].strip().split(" ") if distance != ""]))
    sum = 0
    for t in range(time+1):
        if t*(time - t) > distance:
            sum += 1
    print(sum)
