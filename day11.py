def day11_part_1():
    space_image: list[list[str]]= [[ char for char in line.strip()] for line in open("day11.txt").readlines()]
    empty_rows: set[int] = {i for i in range(len(space_image))} 
    empty_cols: set[int] = {i for i in range(len(space_image[0]))}
    for i in range(len(space_image)):
        for j in range(len(space_image[0])):
            if space_image[i][j] == "#":
                empty_rows.discard(i)
                empty_cols.discard(j)
    for empty_col in sorted(empty_cols, reverse=True):
        for i in range(len(space_image)):
            space_image[i].insert(empty_col, ".")
    for empty_row in sorted(empty_rows, reverse=True):
        space_image.insert(empty_row, ["." for i in range(len(space_image[0]))])
    galaxy_id_and_location: dict[int, tuple[int, int]] = {}
    id: int = 0
    for i in range(len(space_image)):
        for j in range(len(space_image[0])):
            if space_image[i][j] == "#":
                id += 1
                galaxy_id_and_location[id] = (i, j)
    all_combinations: set[tuple[int, int]] = {(min(i,j),max(i,j)) for i in galaxy_id_and_location.keys() for j in galaxy_id_and_location.keys() if i != j} 
    sum_of_distances: int = 0
    for combination in all_combinations:
        sum_of_distances += abs(galaxy_id_and_location[combination[0]][0] - galaxy_id_and_location[combination[1]][0]) + abs(galaxy_id_and_location[combination[0]][1] - galaxy_id_and_location[combination[1]][1])
    print(sum_of_distances)
