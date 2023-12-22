import json
import csv
from csv import DictReader
import os.path
import math

FILES_DIR = os.path.dirname(__file__)


def get_path(filename: str):
    return os.path.join(FILES_DIR, filename)


JSON_FILE_PATH = get_path(filename="users.json")
CSV_FILE_PATH = get_path(filename="books.csv")


with open(CSV_FILE_PATH, newline="") as f:
    reader = csv.reader(f)

    # Извлечение заголовка
    header = next(reader)

    # Итерируемся по данным делая из них словари
    books_list = []

    for row in reader:
        # print(dict(zip(header, row)))
        books_list.append(dict(zip(header, row)))


with open(JSON_FILE_PATH, "r") as f:
    users_list = json.loads(f.read())

# print(users_list)
# print(books_list)

users_len = len(users_list)
# print(users_len)
books_len = len(books_list)
# print(books_len)

difference = math.floor(books_len / users_len)
# print(difference)

user = 0
for i in range(0, books_len + difference - 1, difference):
    # print("ind: ", i, "user: ", user)
    if user == users_len:
        break
    users_list[user]["BOOKS"] = []
    for book in range(i, i + difference):
        # print(book, books_list[i])
        # if book < books_len:
        # print(book, books_list[book])
        users_list[user]["BOOKS"].append(books_list[book])
    user += 1


# for i in range(0, users_len):
#     # print(user, users_list[user])
#     # print(users_list[i], users_list[i]["_id"])


#     users_list[i]["books"] = []
#     users_list[i]["books"].append(books_list[i])

# print(users_list[0], len(users_list[0]["BOOKS"]))
# print()
# print(users_list[1], len(users_list[1]["BOOKS"]))
# print()
# print(users_list[14], len(users_list[14]["BOOKS"]))
# print()
# print(users_list[len(users_list) - 5], len(users_list[len(users_list) - 5]["BOOKS"]))
# print()
# print(users_list[len(users_list) - 4], len(users_list[len(users_list) - 4]["BOOKS"]))
# print()
# print(users_list[len(users_list) - 3], len(users_list[len(users_list) - 3]["BOOKS"]))
# print()
# print(users_list[len(users_list) - 2], len(users_list[len(users_list) - 2]["BOOKS"]))
# print()
# print(users_list[len(users_list) - 1], len(users_list[len(users_list) - 1]["BOOKS"]))


# print(user, user * difference, books_list[user * difference])


for i in range(0, users_len):
    if user * difference + i < books_len:
        users_list[i]["BOOKS"].append(books_list[user * difference + i])

# print()
# print()
# print()


# print(users_list[0], len(users_list[0]["BOOKS"]))
# print()
# print(users_list[1], len(users_list[1]["BOOKS"]))
# print()
# print(users_list[14], len(users_list[14]["BOOKS"]))
# print()
# print(users_list[len(users_list) - 5], len(users_list[len(users_list) - 5]["BOOKS"]))
# print()
# print(users_list[len(users_list) - 4], len(users_list[len(users_list) - 4]["BOOKS"]))
# print()
# print(users_list[len(users_list) - 3], len(users_list[len(users_list) - 3]["BOOKS"]))
# print()
# print(users_list[len(users_list) - 2], len(users_list[len(users_list) - 2]["BOOKS"]))
# print()
# print(users_list[len(users_list) - 1], len(users_list[len(users_list) - 1]["BOOKS"]))


# res = 0
# for i in users_list[0]:
#     print(i)
#     res += 1

# res2 = 0
# for i in users_list[len(users_list) - 1]:
#     print(i)
#     res2 += 1

# print(res)
# print(res2)


with open("result.json", "w") as f:
    s = json.dumps(users_list, indent=4)
    f.write(s)
