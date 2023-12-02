class Game:
    game_id: int
    max_red: int = 0
    max_blue: int = 0
    max_green: int = 0
    def __init__(self, input: str):
        split_input = input.split(":")
        self.game_id = int(split_input[0].split(" ")[1])
        each_draw = split_input[1].split(";")
        for draw in each_draw:
            colours = draw.split(",")
            for colour in colours:
                split_colour = colour.strip().split(" ")
                if split_colour[1] == "red":
                    if self.max_red < int(split_colour[0]):
                        self.max_red = int(split_colour[0])
                elif split_colour[1] == "blue":
                    if self.max_blue < int(split_colour[0]):
                        self.max_blue = int(split_colour[0])
                elif split_colour[1] == "green":
                    if self.max_green < int(split_colour[0]):
                        self.max_green = int(split_colour[0])

def day_2_parser(input: str) -> list[Game]:
    return [Game(line) for line in input.splitlines()]

def day2_part_1():
    games = day_2_parser(open("day2.txt", "r").read())
    sum: int = 0
    for game in games:
        sum += game.game_id if game.max_red <= 12 and game.max_blue <= 14 and game.max_green <= 13 else 0
    print(sum)

def day2_part_2():
    games = day_2_parser(open("day2.txt", "r").read())
    sum: int = 0
    for game in games:
        sum += game.max_red * game.max_blue * game.max_green
    print(sum)
