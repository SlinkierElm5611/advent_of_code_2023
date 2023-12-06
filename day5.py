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
    working_set: set[tuple[int, int]] = set()
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
                for num in working_set:
                    maps_and_values[current_map].add(num)
                working_set = set(maps_and_values[current_map])
            else:
                working_set = set(maps_and_values["seeds"])
        else:
            destination_start, source_start, range_len = tuple([int(num) for num in line.split(" ")])
            for num in list(working_set):
                if destination_start == 0 and source_start == 528596530 and range_len==524016820:
                    print(num)
                    print(source_start)
                    print(range_len)
                if num[0] >= source_start and num[0] < source_start + range_len:
                    overflow: bool = num[0] + num[1] > source_start + range_len
                    interior_start = num[0] - source_start + destination_start
                    if not overflow:
                        maps_and_values[current_map].add((interior_start, num[1]))
                        working_set.discard(num)
                    else:
                        maps_and_values[current_map].add((interior_start, range_len - (interior_start - destination_start)))
                        new_start = source_start + range_len
                        new_len = num[0] + num[1] - new_start
                        working_set.discard(num)
                        working_set.add((new_start, new_len))
                elif num[0]+ num[1] >= source_start and num[0]+num[1] < source_start + range_len and num[0] < source_start:
                    maps_and_values[current_map].add((destination_start, source_start - num[0] + num[1]))
                    new_start = num[0] 
                    new_len = source_start - new_start
                    working_set.discard(num)
                    working_set.add((new_start, new_len))
                elif num[0] < source_start and num[0] + num[1] >= source_start + range_len:
                    maps_and_values[current_map].add((destination_start, range_len))
                    new_start_1 = num[0]
                    new_len_1 = source_start - new_start_1
                    new_start_2 = source_start + range_len
                    new_len_2 = num[1] - new_start_2 + num[0]
                    working_set.discard(num)
                    working_set.add((new_start_1, new_len_1))
                    working_set.add((new_start_2, new_len_2))
    list_of_tuples = list(maps_and_values["humidity-to-location"])
    current_min: int = list_of_tuples[0][0]
    for num in list_of_tuples:
        if num[0] < current_min:
            current_min = num[0]
    print(current_min)
    #print(maps_and_values["humidity-to-location"])
