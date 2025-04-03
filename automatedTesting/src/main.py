# Runs automated tests for assembler and simulator

import sys
from colors import bcolors
from AsmGrader import AsmGrader
from SimGrader import SimGrader
from Results import Results


VERBOSE = False
GRADE_ASSEMBLER = True
GRADE_SIMULATOR = True

def printHelp():
	print('----Please enter in correct format----')
	print("--verbose for verbose output")
	print("--no-asm to not grade assembler")
	print("--no-sim to not grade simulator")
	print("--linux for Linux operating system")
	print("--windows for windows operating system")
	print("Example_linux: $python3 src/main.py --linux --no-sim")
	print("Example_windows: >python3 src\main.py --windows --no-sim")

def setupArgs():
	global VERBOSE
	global GRADE_ASSEMBLER
	global GRADE_SIMULATOR
	global OPERATING_SYSTEM

	if len(sys.argv) < 3:
		printHelp()
		exit()

	for arg in sys.argv[1:]:
		if arg == "--verbose":
			VERBOSE = True
		elif arg == "--no-asm":
			GRADE_ASSEMBLER = False
		elif arg == "--no-sim":
			GRADE_SIMULATOR = False
		elif ((arg == "--linux") | (arg == "--windows")):
			OPERATING_SYSTEM = arg[2:]
		else:
			printHelp()
			exit()
			# break

def main():
	setupArgs()

	asmGrader = AsmGrader(VERBOSE, GRADE_ASSEMBLER,OPERATING_SYSTEM)
	simGrader = SimGrader(VERBOSE, GRADE_SIMULATOR,OPERATING_SYSTEM)

	asmRes = asmGrader.grade()
	simRes = simGrader.grade()	

	res = Results(VERBOSE, asmRes, simRes)
	res.declare()
	

if __name__ == '__main__':
	main()
