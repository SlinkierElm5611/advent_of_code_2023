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

def check_if_num_in_string(string: str) -> Optional[int]:
    numberDict: dict[str,int] = {
            "one": 1,
            "two": 2,
            "three": 3,
            "four": 4,
            "five":5,
            "six": 6,
            "seven": 7,
            "eight": 8,
            "nine": 9,
            }
    if len(string) >=3:
        if string[0:3] in numberDict:
            return numberDict[string[0:3]]
        if string[0:4] in numberDict:
            return numberDict[string[0:4]]
        if string[0:5] in numberDict:
            return numberDict[string[0:5]]

    return None

def day1_part_2():
    parsed_input: list[str] = day1_parser(open("day1.txt", "r").read())
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
                currentNum: Optional[int] = check_if_num_in_string(line[i:min(i+5, len(line))])
                if currentNum:
                    if firstNumber == None:
                        firstNumber = currentNum
                    secondNumber = currentNum
                pass
        sum += firstNumber * 10 + secondNumber
    print(sum)
