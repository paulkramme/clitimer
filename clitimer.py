#!/usr/bin/python3
import time
import sys

silent = None
time = None
einheit = None


def help():
    print("Usage: " + sys.argv[0] + "time einheit [args]")
    print("--silent or -s for silentmode")
    print("--help or -h for help")
    print("Happy timing...")


def setup():
    print("setup")


def config():
    if "--silent" in sys.argv:
        silent = True
        print("Silent Activated")
    elif "-s" in sys.argv:
        silent = True
    if sys.argv[1] == "-h" or sys.argv[1] == "--help":
        help()
    else:
        time = sys.argv[1]
        einheit = sys.argv[2]
        print(time, einheit)


def main():
    config()
if __name__ == __name__:
    main()