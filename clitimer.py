#!/usr/bin/env python3.5

import time
import sys


silent = None
timeinput = 0
einheit = ''


def help():
    print("Usage: " + sys.argv[0] + "time einheit [args]")
    print("--silent or -s for silent mode")
    print("--help or -h for help")
    print("Happy timing...")


def timer():
    global timeinput
    print("Your Settings:", timeinput, einheit)
    time.sleep(float(timeinput))
    print("COMPLETED!")


def setup():
    global timeinput
    global einheit
    if einheit == "Seconds":
        timer()
    elif einheit == "Minutes":
        timeinput *= 60
        timer()
    elif einheit == "Hours":
        timeinput *= (60 * 60)
        timer()
    elif einheit == "Days":
        timeinput *= (60 * 60 * 24)
        timer()
    else:
        print("Something went wrong in setup function.")
        print("Timeinput", timeinput)
        print("Einheit", einheit)


def config():
    global timeinput
    global einheit
    if "--silent" in sys.argv:
        silent = True
        print("Silent Activated")
    elif "-s" in sys.argv:
        silent = True
    if sys.argv[1] == "-h":
        help()
    else:
        timeinput = int(sys.argv[1])
        einheit = sys.argv[2]
        #print(timeinput, einheit)
        setup()


def main():
    print("Timer by Paul Kramme")
    config()


if __name__ == __name__:
    main()
else:
    print("Not a lib yet.")
