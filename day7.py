def add_hand_to_rank(hand: tuple[str, int] , hand_ranking_list: dict[list[tuple[str,int]]], hand_type:str):
    if hand_ranking_list[hand_type] == []:
        hand_ranking_list[hand_type].append(hand)
    else:
        for index, card in enumerate(hand_ranking_list[hand_type]):
            if hand < card:
                hand_ranking_list[hand_type].insert(index, hand)
                break
        else:
            hand_ranking_list[hand_type].append(hand)

def day7_part_1():
    input_file = open("day7.txt", "r")
    hand_ranking_list: dict[list[tuple[str,int]]] = {
        "high_card": [],
        "one_pair": [],
        "two_pairs": [],
        "three_of_a_kind": [],
        "full_house": [],
        "four_of_a_kind": [],
        "five_of_a_kind": [],
            }
    for line in input_file.readlines():
        line = line.replace("T", ":")
        line = line.replace("J", ";")
        line = line.replace("Q", "<")
        line = line.replace("K", "=")
        line = line.replace("A", ">")
        split_line = line.strip().split(" ")
        set_of_cards = set(split_line[0])
        number_of_unique_cards = len(set_of_cards)
        split_line = (split_line[0], int(split_line[1]))
        if number_of_unique_cards == 5:
            add_hand_to_rank(hand=split_line, hand_ranking_list=hand_ranking_list, hand_type="high_card")
        elif number_of_unique_cards == 4:
            add_hand_to_rank(hand=split_line, hand_ranking_list=hand_ranking_list, hand_type="one_pair")
        elif number_of_unique_cards == 3:
            counts: set[int] = set()
            for card in set_of_cards:
                counts.add(split_line[0].count(card))
            if 2 in counts:
                add_hand_to_rank(hand=split_line, hand_ranking_list=hand_ranking_list, hand_type="two_pairs")
            else:
                add_hand_to_rank(hand=split_line, hand_ranking_list=hand_ranking_list, hand_type="three_of_a_kind")
        elif number_of_unique_cards == 2:
            counts: set[int] = set()
            for card in set_of_cards:
                counts.add(split_line[0].count(card))
            if 2 in counts:
                add_hand_to_rank(hand=split_line, hand_ranking_list=hand_ranking_list, hand_type="full_house")
            else:
                add_hand_to_rank(hand=split_line, hand_ranking_list=hand_ranking_list, hand_type="four_of_a_kind")
        else:
            add_hand_to_rank(hand=split_line, hand_ranking_list=hand_ranking_list, hand_type="five_of_a_kind")
    card_types: list[str] = ["high_card", "one_pair", "two_pairs", "three_of_a_kind", "full_house", "four_of_a_kind", "five_of_a_kind"]
    ranked_cards: list[tuple[str,int]] = []
    for card_type in card_types:
        ranked_cards.extend(hand_ranking_list[card_type])
    sum = 0
    for index, card in enumerate(ranked_cards):
        sum += card[1] * (index + 1)
    print(sum)

def day7_part_2():
    input_file = open("day7.txt", "r")
    hand_ranking_list: dict[list[tuple[str,int]]] = {
        "high_card": [],
        "one_pair": [],
        "two_pairs": [],
        "three_of_a_kind": [],
        "full_house": [],
        "four_of_a_kind": [],
        "five_of_a_kind": [],
            }
    for line in input_file.readlines():
        line = line.replace("T", ":")
        line = line.replace("J", "0")
        line = line.replace("Q", "<")
        line = line.replace("K", "=")
        line = line.replace("A", ">")
        split_line = line.strip().split(" ")
        set_of_cards = set(split_line[0])
        number_of_unique_cards = len(set_of_cards)
        split_line = (split_line[0], int(split_line[1]))
        counts: set[int] = set()
        for card in set_of_cards:
            counts.add(split_line[0].count(card))
        if number_of_unique_cards == 5:
            if "0" in set_of_cards:
                add_hand_to_rank(hand=split_line, hand_ranking_list=hand_ranking_list, hand_type="one_pair")
            else:
                add_hand_to_rank(hand=split_line, hand_ranking_list=hand_ranking_list, hand_type="high_card")
        elif number_of_unique_cards == 4:
            if "0" in set_of_cards:
                add_hand_to_rank(hand=split_line, hand_ranking_list=hand_ranking_list, hand_type="three_of_a_kind")
            else:
                add_hand_to_rank(hand=split_line, hand_ranking_list=hand_ranking_list, hand_type="one_pair")
        elif number_of_unique_cards == 3:
            if 2 in counts:
                if "0" in set_of_cards:
                    if split_line[0].count("0") == 2:
                        add_hand_to_rank(hand=split_line, hand_ranking_list=hand_ranking_list, hand_type="four_of_a_kind")
                    else:
                        add_hand_to_rank(hand=split_line, hand_ranking_list=hand_ranking_list, hand_type="full_house")
                else:
                    add_hand_to_rank(hand=split_line, hand_ranking_list=hand_ranking_list, hand_type="two_pairs")
            else:
                if "0" in set_of_cards:
                    add_hand_to_rank(hand=split_line, hand_ranking_list=hand_ranking_list, hand_type="four_of_a_kind")
                else:
                    add_hand_to_rank(hand=split_line, hand_ranking_list=hand_ranking_list, hand_type="three_of_a_kind")
        elif number_of_unique_cards == 2:
            if "0" in set_of_cards:
                add_hand_to_rank(hand=split_line, hand_ranking_list=hand_ranking_list, hand_type="five_of_a_kind")
            else:
                if 2 in counts:
                    add_hand_to_rank(hand=split_line, hand_ranking_list=hand_ranking_list, hand_type="full_house")
                else:
                    add_hand_to_rank(hand=split_line, hand_ranking_list=hand_ranking_list, hand_type="four_of_a_kind")
        else:
            add_hand_to_rank(hand=split_line, hand_ranking_list=hand_ranking_list, hand_type="five_of_a_kind")
    card_types: list[str] = ["high_card", "one_pair","two_pairs", "three_of_a_kind", "full_house", "four_of_a_kind", "five_of_a_kind"]
    ranked_cards: list[tuple[str,int]] = []
    for card_type in card_types:
        ranked_cards.extend(hand_ranking_list[card_type])
    sum = 0
    for index, card in enumerate(ranked_cards):
        sum += card[1] * (index + 1)
    print(sum)
