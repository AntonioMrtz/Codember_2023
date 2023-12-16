from typing import List
import re

email_pattern = re.compile(r"\w+@\w+\.[a-zA-Z]+")  # Matches user@dominio.com


def check_id(id: str):
    return id and id.isalnum()


def check_username(username: str):
    return username and username.isalnum()


def check_email(email: str):
    cosas = re.match(email_pattern, email)
    return re.match(email_pattern, email)


def check_age(age: str):
    if not age:
        return True

    return age.isnumeric()


def check_location(location: str):
    if not location:
        return True

    for char in location:
        # Check if the character is alphanumeric or a space
        if not (char.isalpha() or char.isspace()):
            return False
    # If all characters are alphanumeric or spaces, return True
    return True


def solution(file: str):
    merged_first_username_letter_invalid_row = ""

    with open(file, "r", encoding="utf-8") as file:
        while True:
            line = file.readline()
            if not line:
                break

            line = line.strip().strip("\n")

            fields: List[str] = line.split(",")

            id_user = fields[0]
            username = fields[1]
            email = fields[2]
            age = fields[3]
            location = fields[4]

            if not (
                check_id(id_user)
                and check_username(username)
                and check_email(email)
                and check_age(age)
                and check_location(location)
            ):
                merged_first_username_letter_invalid_row += username[0]

    return merged_first_username_letter_invalid_row


if __name__ == "__main__":
    INPUT_FILE = "05/input_05.txt"
    print(solution(INPUT_FILE))
