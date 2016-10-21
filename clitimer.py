#!/usr/bin/env python3.5
import time
import sys

silent = None
timeinput = 0
einheit = ""


def help():
    print("Usage: " + sys.argv[0] + "time einheit [args]")
    print("--silent or -s for silent mode")
    print("--help or -h for help")
    print("Happy timing...")


def timer():
    print(timeinput)
    time.sleep(float(timeinput))
    print("COMPLETED!")


def setup():
    if einheit == "Seconds":
        pass
    elif einheit == "Minutes":
        timeinput *= 60
    elif einheit == "Hours":
        timeinput *= (60 * 60)
    elif einheit == "Days":
        timeinput *= (60 * 60 * 24)
    else:
        print("Something went wrong.")
        timer()


def config():
    if "--silent" in sys.argv:
        silent = True
        print("Silent Activated")
    elif "-s" in sys.argv:
        silent = True
    if sys.argv[1] == "-h" or sys.argv[1] == "--help":
        help()
    else:
        timeinput = int(sys.argv[1])
        einheit = sys.argv[2]
        print(timeinput, einheit)
        setup()


def main():
    print(sys.argv)
    config()


if __name__ == __name__:
    main()
else:
    print("Not a lib yet...")
