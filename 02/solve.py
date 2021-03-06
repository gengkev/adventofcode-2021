#!/usr/bin/env python3

import copy
import operator
import re
import sys
from collections import Counter, defaultdict, deque
from itertools import permutations, combinations, product
import itertools
import aocd

flatten = itertools.chain.from_iterable


is_sample = False
DAY = 2
YEAR = 2021


DIRS = {
    0: (1, 0),
    1: (0, 1),
    2: (-1, 0),
    3: (0, -1),
}

DDIRS = {
    0: (1, 0),
    1: (1, 1),
    2: (0, 1),
    3: (-1, 1),
    4: (-1, 0),
    5: (-1, -1),
    6: (0, -1),
    7: (1, -1),
}

def vec_add(*args):
    return tuple(map(sum, zip(*args)))

def vec_mul(vec, k):
    return tuple(map(lambda x: x * k, vec))

def bfs(graph, start):
    visited = set()
    order = []
    q = deque([start])

    while q:
        cur = q.popleft()

        if cur in visited:
            continue
        visited.add(cur)
        order.append(cur)

        for nbr in graph[cur]:
            q.append(nbr)

    return order


##########################################################################


def main(A):
    # Solve part 1
    def part1():
        pos = (0, 0)
        for line in A:
            if line[0] == 'forward':
                pos = vec_add(pos, (line[1], 0))
            elif line[0] == 'down':
                pos = vec_add(pos, (0, -line[1]))
            elif line[0] == 'up':
                pos = vec_add(pos, (0, line[1]))
            else:
                assert False
            #print(pos)
        #print('done', pos)
        return -pos[0] * pos[1]

    res = part1()
    submit_1(res)

    # Solve part 2
    def part2():
        pos = (0, 0)
        aim = 0
        for line in A:
            if line[0] == 'forward':
                pos = vec_add(pos, (line[1], 0))
                pos = vec_add(pos, (0, aim * line[1]))
            elif line[0] == 'down':
                aim += line[1]
            elif line[0] == 'up':
                aim -= line[1]
            else:
                assert False
        #print('done', pos)
        return pos[0] * pos[1]

    res = part2()
    submit_2(res)


##########################################################################


def parse_token(x):
    #x = int(x)
    return x


def parse_line(line):
    line = line.split()
    #line = re.findall(r'\d+', line)
    #line = re.findall(r'[-+]?\d+', line)
    #m = re.fullmatch(r"<(.*), (.*), (.*)>", line)
    #line = [parse_token(x) for x in line]

    # One token per line
    #line = line[0]

    line[1] = int(line[1])

    return line


def parse_input(A):
    A = A.strip()
    A = A.splitlines()
    A = [parse_line(line) for line in A]

    # One line per input
    #A = A[0]

    return A


##########################################################################


def submit_1(res):
    print('Part 1', res)
    if not is_sample and not input("skip? "):
        puzzle.answer_a = res


def submit_2(res):
    print('Part 2', res)
    if not is_sample and not input("skip? "):
        puzzle.answer_b = res


##########################################################################


if __name__ == '__main__':
    if len(sys.argv) >= 2 and sys.argv[1].startswith('s'):
        A = open('sample.txt').read()
        is_sample = True
    else:
        puzzle = aocd.models.Puzzle(day=DAY, year=YEAR)
        A = puzzle.input_data
    main(parse_input(A))
