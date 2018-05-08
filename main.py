import argparse
import sys
from CGame import *
from test import *


def parser_args():
    parser = argparse.ArgumentParser()
    parser.add_argument('--inputfile', action='store')
    parser.add_argument('--outputfile', action='store')
    parser.add_argument('--runtest', action='store_true')
    return parser.parse_args()


def solution():
    args = parser_args()

    if args.runtest:
        custom_tests()
    else:
        if args.inputfile is not None:
            sys.stdin = open(args.inputfile, "r")

        ls = input().split()
        HEIGHT = int(ls[0])
        WEIGHT = int(ls[1])
        k = int(ls[2])
        first_world = [['n'] * WEIGHT for _ in range(HEIGHT)]
        read_world(first_world, HEIGHT)
        world = Game(HEIGHT, WEIGHT)
        world.set_world(first_world)
        world.make_steps(k)

        if args.outputfile is not None:
            sys.stdout = open(args.outputfile, "w")

        world.print_world()


if __name__ == "__main__":
    solution()
