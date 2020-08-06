from cipherz import decoder
from client import *
from cipherz import reset


def demand_rand_tmp():
    rand_tmp(1)
    start()


def start():
    v = int(input('Proceed to Decode Message (1 OR Any_key) : '))
    if v == 1:
        decoder.decode()
        clean()
    else:
        print('Invalid entry!')
        start()


def clean():
    s = int(input('For security, will you like to reset rand_tmp & fill_tmp? (1 OR Any_key) : '))
    if s == 1:
        reset.reset()
    else:
        ex()


def ex():
    return None


if __name__ == '__main__':
    demand_rand_tmp()