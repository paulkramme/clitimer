#!/usr/bin/python3
import time
import argparse

parser = argparse.ArgumentParser("Simple CLI Counter")
parser.add_argument("time", metavar="T", type=int, nargs=1, help="Time when the alarm will go off")

args = parser.parse_args()
print(args)

