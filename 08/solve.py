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
DAY = 8
YEAR = 2021

DIGITS = {
    0: 'abcefg',
    1: 'cf',
    2: 'acdeg',
    3: 'acdfg',
    4: 'bcdf',
    5: 'abdfg',
    6: 'abdefg',
    7: 'acf',
    8: 'abcdefg',
    9: 'abcdfg',
}
DIGIT_VALS = set(DIGITS.values())
DIGITS_REV = dict((b,a) for (a,b) in DIGITS.items())

def letter_to_num(l):
    return 'abcdefg'.index(l)

def num_to_letter(n):
    return 'abcdefg'[n]

##########################################################################


def main(A):
    # Solve part 1
    def part1():
        cnt = 0
        for line in A:
            for w in line[1]:
                if len(w) in {2,3,4,7}:
                    cnt += 1
        return cnt

    res = part1()
    submit_1(res)

    def trans_inp(perm, inp):
        out = set()
        for l in inp:
            out.add(perm[letter_to_num(l)])
        #print('for perm', perm, 'and inp', inp, 'got out', ''.join(sorted(out)))
        return ''.join(sorted(out))

    def rev_perm(perm):
        lst = list(map(letter_to_num, perm))
        rev = dict((b,a) for (a,b) in lst.items())
        return ''.join(num_to_letter(rev[k]) for k in range(7))

    def solve_line(all_inputs, out_digits):
        success = False
        for perm in permutations('abcdefg'):
            perm = ''.join(perm)
            #print('trying perm', perm)
            x = 0
            for inp in all_inputs:
                inp2 = trans_inp(perm, inp)
                x += 1
                if inp2 not in DIGIT_VALS:
                    #if x >= 3:
                    #    print('FAILEd on', inp2)
                    break
            else:
                #print('perm succeeded', perm)
                success = True
                break

        assert success
        out = ''
        for x in out_digits:
            x = trans_inp(perm, x)
            out += str(DIGITS_REV[x])
        return out

    # Solve part 2
    def part2():
        s = 0
        for ins, outs in A:
            out = solve_line(ins, outs)
            s += int(out)
        return s

    res = part2()
    submit_2(res)


##########################################################################


def parse_token(x):
    #x = int(x)
    return x


def parse_line(line):
    line = line.split()
    return (line[0:10], line[11:15])


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
