def solution(file: str):

    number_current_bad_password = 0
    RESULT_NUMBER_OCCURENCES = 42

    with open(file, 'r', encoding='utf-8') as file:
        line = file.readline()
        # 8-10 r: ozrcdfnug

        while line:

            password = line.split(":")[1].strip()
            policy = line.split(":")[0].strip()
            letter = policy.split(" ")[1].strip()
            min_number_occurrencess = int(policy.split(" ")[0].split("-")[0].strip())
            max_number_occurrences = int(policy.split(" ")[0].split("-")[1].strip())

            if password.count(letter) < min_number_occurrencess or password.count(letter)>max_number_occurrences:
                number_current_bad_password+=1

            if number_current_bad_password==RESULT_NUMBER_OCCURENCES:
                return password

            line = file.readline()

if __name__ == "__main__":

    INPUT_FILE = '03/input_03.txt'
    print(solution(INPUT_FILE))
