#!/usr/bin/env python3
##
## EPITECH PROJECT, 2020
## bombyx.h
## File description:
## 
##

from sys import argv
from math import sin, cos, pi, sqrt, tan, radians

def err_gest(argv):
    test = 0
    k = 0

    if len(argv) == 2 and argv[1] == '-h':
        print("USAGE\n    ./106bombyx n [k | i0 i1]\n\nDESCRIPTION\n    n    number of first generation individuals\n    k    growth rate from 1 to 4\n    i0   initial generation (included)\n    i1   final generation (included)")
        exit(0)
    if len(argv) != 3 and len(argv) != 4:
        exit(84)
    if len(argv) == 3:
        try:
            int(argv[1])
            float(argv[2])
        except ValueError:
            exit(84)
        if test == 2:
            k = int(argv[2])
        else:
            k = float(argv[2])
        if k < 1 or k > 4 or int(argv[1]) < 0:
            exit(84)
    else:
        try:
            int(argv[1])
            int(argv[2])
            int(argv[3])
        except ValueError:
            exit(84)
        if int(argv[1]) < 0 or int(argv[3]) <= 0 or int(argv[2]) < 0 or int(argv[2]) > int(argv[3]):
            exit(84)
    return (k)
    

def seq(argv):
    x = int(argv[1])
    mem = x
    k = 1
    i0 = int(argv[2])
    i1 = int(argv[3])
    i = 1

    while k <= 4:
        while i < i0:
            x = k * x * (1000 - x) / 1000
            i = i + 1
            if x < 0:
                x = 0
        while i <= i1:
            print("%.2f %.2f" % (k, x))
            x = k * x * (1000 - x) / 1000
            i = i + 1
            if x < 0:
                x = 0
        k = k + 0.01
        i = 1
        x = mem

def growth(k, argv):
    x = int(argv[1])
    i = 1

    while i <= 100:
        print("%i %.2f" % (i, x))
        x = k * x * (1000 - x) / 1000
        if x < 0:
            x = 0
        i = i + 1

if __name__=='__main__':
    k = err_gest(argv)

    if len(argv) == 3:
        growth(k, argv)
    else:
        seq(argv)      