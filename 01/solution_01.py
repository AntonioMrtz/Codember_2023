def solution(file: str):

    word_counter = {}
    appearances_string = ""

    with open(file, 'r', encoding='utf-8') as file:
        content = file.read().split(" ")

    for word in content:

        word_lowercase = word.lower()
        if word_lowercase in word_counter:
            word_counter[word_lowercase] += 1
        else:
            word_counter[word_lowercase] = 1

    for word_entry in word_counter.items():
        appearances_string += f"{word_entry[0]}{word_entry[1]}"

    return appearances_string


if __name__ == "__main__":

    INPUT_FILE = '01/input_01.txt'
    print(solution(INPUT_FILE))
