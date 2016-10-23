#!/usr/bin/env python3

#MIT License
#
#Copyright (c) 2016 Paul Kramme
#
#Permission is hereby granted, free of charge, to any person obtaining a copy
#of this software and associated documentation files (the "Software"), to deal
#in the Software without restriction, including without limitation the rights
#to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
#copies of the Software, and to permit persons to whom the Software is
#furnished to do so, subject to the following conditions:
#
#The above copyright notice and this permission notice shall be included in all
#copies or substantial portions of the Software.
#
#THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
#IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
#FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
#AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
#LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
#OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
#SOFTWARE.


import time
import sys


silent = None
timeinput = 0
unit = ''


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


def main():
    print("Timer by Paul Kramme")
    config()

def winmain():
    print("WIP")

if __name__ == __name__:
    if os.name == "posix":
        main()
    else:
        winmain()
else:
    print("Not a lib yet.")
