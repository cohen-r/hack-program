#!/usr/bin/env python

"""

Command line interface to compliment_me and plant_me

"""

import argparse
from compliments import compliment_me, plant_me

def parse_command_line():
    "parses args for the compliment_me funtion"

    # init parser and add arguments
    parser = argparse.ArgumentParser()

    # add long args
    parser.add_argument(
        "--sad",
        help="returns a compliment for when you're feeling sad",
        action="store_true")

    # add long args
    parser.add_argument(
        "--happy",
        help="returns a statement relevant to feeling happy",
        action="store_true")

    parser.add_argument(
        "--angry",
        help="returns a compliment for when you're angry",
        action="store_true")

    # parse args
    args = parser.parse_args()
    return args

def main():
    "run main function on parsed args"

    # get arguments from command line as a dict-like object
    args = parse_command_line()

    # pass argument to call compliments function
    if args.sad:
        compliment_me("sad")
        plant_me()
    elif args.happy:
        compliment_me("happy")
        plant_me()
    elif args.angry:
        compliment_me("angry")
        plant_me()


if __name__ == "__main__":
    compliment_me("angry")
