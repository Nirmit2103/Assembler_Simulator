# Simulator Grader class

from colors import bcolors

from Grader import Grader
import os

class SimGrader(Grader):

	# 0.2 x 10
	SIMPLE_MARKS = 2    #4/6 #0.2
	# 0.8 x 5
	HARD_MARKS = 1

	BIN_HARD_DIR = "hard"
	BIN_SIMPLE_DIR = "simple"

	TRACE_HARD_DIR = "hard"
	TRACE_SIMPLE_DIR = "simple"


	def __init__(self, verb, enable,operating_system):
		super().__init__(verb, enable,operating_system)
		self.enable = enable
		self.operating_system = operating_system
		
		if self.operating_system == 'linux':
			self.SIM_RUN_DIR = "../SimpleSimulator/"
		elif self.operating_system == 'windows':
			self.SIM_RUN_DIR = "..\\SimpleSimulator\\"

	def handleBin(self, genDir, expDir):
		
		passCount = 0
		totalCount = 0
		
		curDir = os.getcwd()
		if self.operating_system == 'linux':
			tests = self.listFiles("tests/bin/" + genDir)
		elif self.operating_system == 'windows':
			tests = self.listFiles("tests\\bin\\" + genDir)
		tests.sort()
		os.chdir(self.SIM_RUN_DIR)
		
		for test in tests:
			
			python_command = 'python3 Simulator.py'
			if self.operating_system == 'linux':
				machine_code_file = ' ' + '../automatedTesting/tests/bin/' + genDir + '/' + test
				output_trace_file = ' ' + '../automatedTesting/tests/user_traces/' + genDir + '/' + test
				output_read_trace_file = ' ' + '../automatedTesting/tests/user_traces/' + genDir + '/' + test.split(".")[0]+"_r.txt"
				os.remove(output_trace_file) if os.path.exists(output_trace_file) else None; 
				os.remove(output_read_trace_file) if os.path.exists(output_read_trace_file) else None;
			elif self.operating_system == 'windows':
				machine_code_file = ' ' + '..\\automatedTesting\\tests\\bin\\' + genDir + '\\' + test
				output_trace_file = ' ' + '..\\automatedTesting\\tests\\user_traces\\' + genDir + '\\' + test
				output_read_trace_file = ' ' + '../automatedTesting/tests/user_traces/' + genDir + '/' + test.split(".")[0]+"_r.txt"
				os.remove(output_trace_file) if os.path.exists(output_trace_file) else None; 
				os.remove(output_read_trace_file) if os.path.exists(output_read_trace_file) else None;
			command = python_command + machine_code_file + output_trace_file + output_read_trace_file
			os.system(command)
			
			
			generatedTrace = open(output_trace_file.strip(),'r').readlines()

			if self.operating_system == 'linux':
				exact_trace_file = "../automatedTesting/tests/traces/" + expDir + "/" + test
			elif self.operating_system == 'windows':
				exact_trace_file = "..\\automatedTesting\\tests\\traces\\" + expDir + "\\" + test
				
			try:
				expectedTrace = open(exact_trace_file,'r').readlines()
			except FileNotFoundError:
				self.printSev(self.HIGH, bcolors.WARNING + "[Golden Binary Trace File Not Found]\n" + exact_trace_file)
				expectedTrace = " "
			

			if self.diff(generatedTrace, expectedTrace):
				self.printSev(self.HIGH, bcolors.OKGREEN + "[PASSED]" + bcolors.ENDC + " " + test)
				passCount += 1
			else:
				self.printSev(self.HIGH, bcolors.FAIL + "[FAILED]" + bcolors.ENDC + " " + test)
			totalCount += 1

		os.chdir(curDir)
		return passCount, totalCount
	
	def grade(self):
		res = None
		if(self.enable):
			self.printSev(self.HIGH, bcolors.WARNING + bcolors.BOLD + "==================================================" + bcolors.ENDC)
			self.printSev(self.HIGH, bcolors.WARNING + bcolors.BOLD + "================ TESTING SIMULATOR ===============" + bcolors.ENDC)
			self.printSev(self.HIGH, bcolors.WARNING + bcolors.BOLD + "==================================================" + bcolors.ENDC)
			self.printSev(self.HIGH, "")
			
			self.printSev(self.HIGH, bcolors.OKBLUE + bcolors.BOLD + "Runing simple tests" + bcolors.ENDC)
			simplePass, simpleTotal = self.handleBin(self.BIN_SIMPLE_DIR, self.TRACE_SIMPLE_DIR)

			self.printSev(self.HIGH, bcolors.OKBLUE + bcolors.BOLD + "\nRunning hard tests" + bcolors.ENDC)
			hardPass, hardTotal = self.handleBin(self.BIN_HARD_DIR, self.TRACE_HARD_DIR)
			
			res = [
					["Simple", simplePass, simpleTotal, self.SIMPLE_MARKS],
					["Hard", hardPass, hardTotal, self.HARD_MARKS],
				]
		
		return res
