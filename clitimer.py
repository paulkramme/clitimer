#!/usr/bin/env python3

import time
import sys
import os


silent = None
timeinput = None
unit = None


def help():
    print("Usage: " + sys.argv[0] + "time unit [args]")
    print("--silent or -s for silent mode")
    print("--help or -h for help")
    print("Happy timing...")


def timer():
    global timeinput
    print("Your Settings:", timeinput, "Seconds")
    #time.sleep(float(timeinput))
    while timeinput:
        print("Time left in seconds:", timeinput)
        time.sleep(1)
        #print(timeinput)
        timeinput = timeinput - 1
    print("COMPLETED!")


def setup():
    global timeinput
    global unit
    if unit == "Seconds":
        timer()
    elif unit == "Minutes":
        timeinput *= 60
        timer()
    elif unit == "Hours":
        timeinput *= (60 * 60)
        timer()
    elif unit == "Days":
        timeinput *= (60 * 60 * 24)
        timer()
    else:
        print("Something went wrong in setup function.")
        print("Timeinput", timeinput)
        print("unit", unit)


def config():
    global timeinput
    global unit
    if "--silent" in sys.argv:
        silent = True
        print("Silent Activated")
    elif "-s" in sys.argv:
        silent = True
    if sys.argv[1] == "-h":
        help()
    else:
        timeinput = int(sys.argv[1])
        unit = sys.argv[2]
        #print(timeinput, unit)
        setup()


def winconfig():
    global timeinput
    global unit
    timeinput = int(input("Time to count to: "))
    unit = input("Minutes/Seconds/Days/Hours: ")
    setup()


def main():
    print("Timer by Paul Kramme")
    config()


def winmain():
    print("Launching Windows Console...")
    winconfig()


if __name__ == __name__:
    if os.name == "posix":
        main()
    else:
        winmain()
