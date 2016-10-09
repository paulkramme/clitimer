#!/usr/bin/python3
import time
import sys

cliinput = ""

def config():
	if "--silent", "-s" in cliinput:
		print("WHEEEEE")
	elif "--count" in sys.argv:
		print("Counting something")
	elif "--count" in cliinput:
		print("ur mam")
	else:
		print("Command not found")
def main():
	if len(sys.argv) < 2:
		print("CLI Counter")
		while True:
			print(">", end='')
			cliinput = input()
			config()
	else:
		config()
	

if __name__ == __name__:
	main()
else:
	print("This is not a lib")
