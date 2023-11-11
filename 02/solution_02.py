def solution(file: str):

    current_number = 0
    printed_numbers = ""

    with open(file, 'r', encoding='utf-8') as file:
        content = file.read()

    for letter in content:

        if letter == "#":
            current_number += 1

        elif letter == "@":
            current_number -= 1

        elif letter == "*":
            current_number *= current_number

        elif letter == "&":
            printed_numbers+=str(current_number)

    return printed_numbers
if __name__ == "__main__":

    INPUT_FILE = '02/input_02.txt'
    print(solution(INPUT_FILE))
