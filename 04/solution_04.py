from typing import List


def solution(file: str):
    current_real_file_number = 0

    TRUE_FILE_NUMBER = 33
    MAX_OCURRENCES = 1

    with open(file, "r", encoding="utf-8") as file:
        while True:
            line = file.readline()
            if not line:
                break

            line = line.strip().strip("\n")

            file_name: str = line.split("-")[0]
            checksum: str = line.split("-")[1]

            current_checksum_char_index = 0

            for char in file_name:
                if (
                    file_name.count(char) == MAX_OCURRENCES
                    and char == checksum[current_checksum_char_index]
                ):
                    current_checksum_char_index += 1
                else:
                    continue

            current_real_file_number += 1

            if current_real_file_number == TRUE_FILE_NUMBER:
                return checksum


if __name__ == "__main__":
    INPUT_FILE = "04/input_04.txt"
    print(solution(INPUT_FILE))
