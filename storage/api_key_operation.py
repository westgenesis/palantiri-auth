from flask import request, jsonify
import os.path
import json


def save_api_key(usr, token):
    file = open("./storage/api_key.txt", 'a')
    file.write(token)
    file.write("\n")
    file.close()

    # # separate usr
    # new_key = usr
    # new_value = token

    # # read json
    # with open("./storage/api_key.json", "r") as file:
    #     data = json.load(file)
    #
    #     # check key is in the dict or not
    # if new_key in data:
    #     # if key exist，add new value into list
    #     data[new_key].append(new_value)
    # else:
    #     # if key not exist，create a new key into it
    #     data[new_key] = [new_value]
    #
    #     # write down modify json
    # with open("./storage/api_key.json", "w") as file:
    #     json.dump(data, file)

    return 0


def compare_api_key(key):
    flag = False
    # file_path = "./storage/api_key.txt"
    # with open(file_path, 'r') as file:
    #     lines = file.readlines()
    #     print(lines)
    #
    # for i in range(len(lines) - 1):
    #     if lines[i] == key:
    #         flag = True
    with open("./storage/api_key.txt", 'r') as f:
        for line in f:
            print(line.strip())
            print(key)
            print(flag)
            if line.strip() == key:
                print(1)
                flag = True

    return flag

#
# if __name__ == '__main__':
#     api_key = {}
#     usr = "WICV"
#     key = "7ee18b730c127ff156a338190b0b0bed"
#     api_key.setdefault(usr, []).append(key)
#     # key_dict = {usr: key}
#     for i in range(10):
#         with open("api_key.pkl", 'ab') as tf:
#             pickle.dump(api_key, tf)
#     with open("api_key.pkl", 'rb') as f:
#         data = pickle.load(f)
#         print(data)
