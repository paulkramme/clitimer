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
