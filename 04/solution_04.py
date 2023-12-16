from typing import List


def solution(file: str):
    current_real_file_number = 0
    TRUE_FILE_NUMBER = 33
    MAX_OCURRENCES = 1

    with open(file, "r", encoding="utf-8") as file:
        line = file.readline()
        # 3n3E65A-nE65A

        while line:
            unique_chars_in_order: List[str] = []

            line = line.strip().strip("\n")

            file_name: str = line.split("-")[0]
            checksum: str = line.split("-")[1]

            for char in file_name:
                if file_name.count(char) == MAX_OCURRENCES:
                    unique_chars_in_order.append(char)

            unique_chars_string = "".join(unique_chars_in_order)

            if unique_chars_string != checksum:
                continue

            current_real_file_number += 1

            if current_real_file_number == TRUE_FILE_NUMBER:
                return checksum

            line = file.readline()


if __name__ == "__main__":
    INPUT_FILE = "04/input_04.txt"
    print(solution(INPUT_FILE))
