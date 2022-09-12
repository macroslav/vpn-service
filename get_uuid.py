from uuid import uuid4


def get_uuid() -> str:
    uuid = uuid4()
    uuid = str(uuid)
    return uuid


def uuid_revers() -> str:
    row = get_uuid()
    reverse_row = row[::-1]
    print(f"перевернутая строка {reverse_row}")
    print(f"обычная строка {row}")


def solve_tusk_1() -> str:
    N = int(input('Введите количество ключей UUID:'))
    for i in range(N):
        b = get_uuid()
        print('Исходный код UUID', b)
        if b[0].isalpha():
            sep_index = b.find("-")
            print('Коды с первым символом - буквой', b[:sep_index])
        elif b[0].isalnum():
            razbiv = b.split('-')
            print('Коды с первым символом - буквой', razbiv[-1])


def my_solve_task_1(number_of_uuids: int) -> None:
    for i in range(number_of_uuids):
        current_uuid = get_uuid()

        print(f'Исходный UUID {current_uuid}')
        splitted_uuid = current_uuid.split('-')
        if current_uuid[0].isalpha():
            print('Первый символ - буква: ', splitted_uuid[1])
        elif current_uuid[0].isalnum():
            print('Первый символ - цифра:', splitted_uuid[-1])


def main():
    N = int(input('Введите количество UUID:'))
    my_solve_task_1(number_of_uuids=N)


if __name__ == "__main__":
    main()
