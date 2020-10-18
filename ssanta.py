"""
This program takes a list of lists and returns secret santa matchups 
for each person. People in the same inner list cannot be matched. 
"""
import json
import random

def randomize(couples: list):
    """
    Does the randomizing
    """
    random.shuffle(
        couples
    )
    return couples


if __name__ == '__main__':
    import argparse

    parser = argparse.ArgumentParser()

    parser.add_argument(
        'list_file',
        help="The JSON string containing the list"
    )
    args = parser.parse_args()

    print(args.list_file)

    with open(args.list_file) as _f:
        couples = json.load(_f)
        print(
            randomize(couples)
        )