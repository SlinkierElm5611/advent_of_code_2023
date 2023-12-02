from typing import Optional

def day1_parser(input: str)-> list[str]:
    return input.splitlines()

def day1_part_1():
    parsed_input: list[str] = day1_parser(open("day1.txt", "r").read())
    sum: int = 0
    for line in parsed_input:
        firstNumber: Optional[int] = None 
        secondNumber: Optional[int] = None
        for char in line:
            try:
                currentNum = int(char)
                if firstNumber == None:
                    firstNumber = currentNum
                secondNumber = currentNum
            except:
                pass
        sum += firstNumber * 10 + secondNumber
    print(sum)

def day1_part_2():
    numberWords: dict[str, int] = {
        "one": 1,
        "two": 2,
        "three": 3,
        "four": 4,
        "five":5,
        "six": 6,
        "seven": 7,
        "eight": 8,
        "nine": 9
    }
    initial_input: str = open("day1.txt", "r").read()
    for word in numberWords.keys():
        initial_input = initial_input.replace(word, word[0] + word + word[-1])
    for word in numberWords.keys():
        initial_input = initial_input.replace(word, str(numberWords[word]))
    parsed_input: list[str] = day1_parser(initial_input)
    sum: int = 0
    for line in parsed_input:
        if line == "":
            continue
        firstNumber: Optional[int] = None 
        secondNumber: Optional[int] = None
        for i in range(len(line)):
            currentNum: Optional[int] = None
            try:
                currentNum = int(line[i])
                if firstNumber == None:
                    firstNumber = currentNum
                secondNumber = currentNum
            except:
                pass
        sum += firstNumber * 10 + secondNumber
    print(sum)
