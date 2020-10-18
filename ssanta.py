"""
This program takes a list of lists and returns secret santa matchups 
for each person. People in the same inner list cannot be matched. 
"""
import json
import random

from functools import reduce


def flatten(_list):
    """
    Takes a list of lists and returns a songle list containing all items

    :_list list: The list to flatten

    :return list: The flat list
    """
    return reduce(
        lambda x, y: y + x,
        _list,
        []
    )


def valid(exclusions, flat_list):
    """
    Determines if the flat list meets the couples requirements

    :exclusions list: The list of lists used to invalidate the shuffle
    :flast_list list: The current shuffle to validate

    :return bool: Is or is not a valid shuffle
    """
    flag = False
    for ix, name in enumerate(flat_list):
        pair = {name, flat_list[(ix + 1) % len(flat_list)]}
        for group in exclusions:
            flag |= pair <= set(group)
    return not flag  # result


def randomize(exclusions: list):
    """
    Does the randomizing
    """
    flat_list = flatten(exclusions)
    while not valid(exclusions, flat_list):
        random.shuffle(
            flat_list
        )
    return flat_list


if __name__ == '__main__':
    import argparse

    parser = argparse.ArgumentParser()

    parser.add_argument(
        'list_file',
        help="The JSON string containing the list"
    )
    args = parser.parse_args()

    with open(args.list_file) as _f:
        couples = json.load(_f)

        # Print the result of the randomization to the shell
        print(
            randomize(couples)
        )
