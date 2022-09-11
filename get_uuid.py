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
def uuid_revers() -> str:
    row = get_uuid()
    reverse_row= row[::-1]
    print(f"перевернутая строка {reverse_row}")
    print(f"обычная строка {row}")
uuid_revers()
