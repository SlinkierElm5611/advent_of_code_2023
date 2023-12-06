def day5_part_1():
    input_file = open("day5.txt", "r")
    previous_map: str = ""
    current_map: str = ""
    maps_and_values: dict[str, set[int]] = {"seeds": set()}
    working_set: set[int] = set()
    lines = input_file.readlines()
    lines.append("")
    for line in lines:
        line = line.strip()
        if line.startswith("seeds:"):
            for num in line.split(":")[1].strip().split(" "):
                maps_and_values["seeds"].add(int(num))
        elif line.endswith("map:"):
            if previous_map =="":
                previous_map = "seeds"
            else:
                previous_map = current_map
            current_map = line.split(" ")[0]
            maps_and_values[current_map] = set()
        elif line == "":
            if current_map != "":
                for num in working_set:
                    maps_and_values[current_map].add(num)
                working_set = set(maps_and_values[current_map])
            else:
                working_set = set(maps_and_values["seeds"])
        else:
            destination_start, source_start, range_len = tuple([int(num) for num in line.split(" ")])
            for num in list(working_set):
                if num >= source_start and num < source_start + range_len:
                    maps_and_values[current_map].add(num - source_start + destination_start)
                    working_set.discard(num)
    print(min(maps_and_values["humidity-to-location"]))

def day5_part_2():
    input_file = open("day5.txt", "r")
    previous_map: str = ""
    current_map: str = ""
    maps_and_values: dict[str, set[tuple[int, int]]] = {"seeds": set()}
    working_list: list[tuple[int, int]] = []
    lines = input_file.readlines()
    lines.append("")
    for line in lines:
        line = line.strip()
        if line.startswith("seeds:"):
            source_start: int|None = None 
            for num in line.split(":")[1].strip().split(" "):
                if source_start == None:
                    source_start = int(num)
                else:
                    maps_and_values["seeds"].add((source_start, int(num)))
                    source_start = None
        elif line.endswith("map:"):
            if previous_map =="":
                previous_map = "seeds"
            else:
                previous_map = current_map
            current_map = line.split(" ")[0]
            maps_and_values[current_map] = set()
        elif line == "":
            if current_map != "":
                for num in working_list:
                    maps_and_values[current_map].add(num)
                working_list = list(maps_and_values[current_map])
            else:
                working_list = list(maps_and_values["seeds"])
        else:
            destination_start, source_start, range_len = tuple([int(num) for num in line.split(" ")])
            numbers_to_remove: list[tuple[int, int]] = []
            temp_list = []
            while working_list:
                num = working_list.pop()
                # no overflow for both front and end
                if num[0] >= source_start and num[0] + num[1] <= source_start + range_len:
                    maps_and_values[current_map].add((num[0] - source_start + destination_start, num[1]))
                # overflow on end
                elif num[0] >= source_start and num[0] < source_start + range_len and num[0] + num[1] > source_start + range_len:
                    maps_and_values[current_map].add((num[0] - source_start + destination_start, source_start + range_len - num[0]))
                    temp_list.append((source_start + range_len, num[0] + num[1] - source_start - range_len))
                # overflow on front
                elif num[0] < source_start and num[0] + num[1] > source_start and num[0] + num[1] <= source_start + range_len:
                    maps_and_values[current_map].add((destination_start, num[0] + num[1] - source_start))
                    temp_list.append((num[0], source_start - num[0]))
                # overflow on both front and end
                elif num[0] < source_start and num[0] + num[1] > source_start + range_len:
                    maps_and_values[current_map].add((destination_start, range_len))
                    temp_list.append((source_start + range_len, num[0] + num[1] - source_start - range_len))
                    temp_list.append((num[0], source_start - num[0]))
                else:
                    temp_list.append(num)
            working_list = temp_list
    list_of_tuples = list(maps_and_values["humidity-to-location"])
    current_min: int = list_of_tuples[0][0]
    for num in list_of_tuples:
        if num[0] < current_min:
            current_min = num[0]
    print(current_min)
