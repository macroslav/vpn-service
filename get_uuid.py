from uuid import uuid4


def get_uuid() -> str:
    uuid = uuid4()
    uuid = str(uuid)
    return uuid

# for i in range(10):
#     b = get_uuid()
#     sep_index = b.find("-")
#     print(b[:sep_index])

# for i in range(10):
#     b = get_uuid()
#     if b[0].isalpha():
#         print(b)
#     else:
#         print("UUID начинается с цифры")

# def uuid_revers() -> str:
#     row = get_uuid()
#     reverse_row= row[::-1]
#     print(f"перевернутая строка {reverse_row}")
#     print(f"обычная строка {row}")
# uuid_revers()

def solve_tusk_1() -> str:
    N = int(input('Введите количество ключей UUID:'))
    for i in range(N):
        b = get_uuid()
        print('Исходный код UUID',b)
        if b[0].isalpha():
            sep_index = b.find("-")
            print('Коды с первым символом - буквой',b[:sep_index])
        elif b[0].isalnum():
            razbiv = b.split('-')
            print('Коды с первым символом - буквой',razbiv[-1])

solve_tusk_1()
