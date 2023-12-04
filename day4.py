def day4_part_1():
    input_text= open("day4.txt", "r")
    sum = 0
    for line in input_text.readlines():
        card_score = 0
        card = line.strip().split(":")[1]
        split_card = card.strip(" ").split("|")
        your_numbers = set(split_card[0].strip(" ").split(" "))
        winning_numbers = set(split_card[1].strip(" ").split(" "))
        your_numbers.discard("")
        winning_numbers.discard("")
        for num in your_numbers:
            if num in winning_numbers:
                if card_score == 0:
                    card_score = 1
                else:
                    card_score *= 2
        sum += card_score
    print(sum)

def day4_part_2():
    input_text= open("day4.txt", "r")
    lines = input_text.readlines()
    cards: dict[int, int] = {}
    for i in range(0, len(lines)):
        cards[i] = 1
    for i, line in enumerate(lines):
        card_score = 0
        split_line = line.strip().split(":")
        card = split_line[1].strip()
        split_card = card.strip(" ").split("|")
        your_numbers = set(split_card[0].strip(" ").split(" "))
        winning_numbers = set(split_card[1].strip(" ").split(" "))
        your_numbers.discard("")
        winning_numbers.discard("")
        for num in your_numbers:
            if num in winning_numbers:
                card_score += 1
        for j in range(i+1, min(i+1+card_score, len(lines))):
            cards[j] += cards[i]
    sum = 0
    for card_key in cards.keys():
        sum += cards[card_key] 
    print(sum)
