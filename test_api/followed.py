import json
import os

FILE_NAME = "followed.storage"


def follow(following, followed):
    with open(FILE_NAME, 'w') as output_file:
        json.dump({"following": following, "followed": followed}, output_file)


def delete_all():
    with open(FILE_NAME, 'w') as output_file:
        json.dump({}, output_file)


def does_alice_follow_bob():
    with open(FILE_NAME, 'r') as input_file:
        json_obj = json.load(input_file)

        return 'following' in json_obj
