import subprocess
import sys
import io
import random

MATCHING_BASES = [["A", "T"], ["G", "C"]]

HELP_TEXT = """
Flags:
	-part 		
Commands:
	proofread 	Proofread. Specification of .txt file that is to be proofread is needed.
	createtest 	Create a test file. Specification of percentage of error is needed.
"""

def create_test_file(percentage):
	with open("./proofreader_test.txt", "w") as obj:
		for _ in range(0, 150):
			random_value = random.random()
			# write an error to the file
			if random_value < percentage:
				base1 = MATCHING_BASES[0][random.randint(0, 1)]
				base2 = MATCHING_BASES[1][random.randint(0, 1)]
				if random.randint(0, 1) == 1:
					obj.write(f"{base1},{base2}\n")
				else:
					obj.write(f"{base2},{base1}\n")
			# write a pair that does not cause error
			else:
				random_index = random.randint(0, 1)
				base1 = MATCHING_BASES[random_index][0]
				base2 = MATCHING_BASES[random_index][1]
				if random.randint(0, 1) == 1:
					obj.write(f"{base1},{base2}\n")
				else:
					obj.write(f"{base2},{base1}\n")

def proofread(file_name):
	error_lines = []
	with open(file_name, "r") as obj:
		lines = obj.readlines()
		line_counter = 0
		for line in lines:
			line_counter += 1
			bases = line.split(",")
			try:
				base1 = bases[0].upper().strip()
				base2 = bases[1].upper().strip()
			except IndexError:
				raise RuntimeError("Please make sure the specified file conforms the format.")

			# base1 = A and base2 = T
			if base1 == MATCHING_BASES[0][0] and base2 == MATCHING_BASES[0][1]:
				print(".", flush=True, end="")
			# base1 = T and base2 = A
			elif base1 == MATCHING_BASES[0][1] and base2 == MATCHING_BASES[0][0]:
				print(".", flush=True, end="")
			# base1 = G and base2 = C
			elif base1 == MATCHING_BASES[1][0] and base2 == MATCHING_BASES[1][1]:
				print(".", flush=True, end="")
			# base1 = C and base2 = G
			elif base1 == MATCHING_BASES[1][1] and base2 == MATCHING_BASES[1][0]:
				print(".", flush=True, end="")
			else:
				print("E", flush=True, end="")
				error_lines.append(f"Error on {line_counter} line")
	# for separating the results
	print("\n")
	print("-"*30)
	if len(error_lines) > 0:
		for error in error_lines:
			print(error)
	else:
		print("No errors detected.")

def file_check(file_name, partially=False):
	if partially:
		output = subprocess.check_output(["find", ".", "-iname", f"{file_name}*.txt"])
	else:
		output = subprocess.check_output(["find", ".", "-iname", f"{file_name}"])
	files = output.decode("utf-8").strip().splitlines()
	if len(files) == 0:
		raise FileNotFoundError("Specified file cannot be found. '-part' flag? Forgot .txt extension?")
	elif len(files) >= 1:
		proper_file_name = files[0]
		proofread(proper_file_name)

def show_help():
	print(HELP_TEXT)

def main():
	if len(sys.argv) > 1:
		# proofread
		if sys.argv[1] == "proofread":
			try:
				arg = sys.argv[2]
			except IndexError:
				raise RuntimeError("Please specify a file name.")
			if arg == "-part":
				try:
					file_check(sys.argv[3], True)
				except IndexError:
					raise RuntimeError("Please specify a file name.")
			else:
				file_check(sys.argv[2])
		# createtest
		elif sys.argv[1] == "createtest":
			try:
				percentage = float(sys.argv[2])
			except IndexError:
				raise RuntimeError("Please specify the percentage.")
			except ValueError:
				raise TypeError("Please specify the percentage as a float: ex. 0.3")
			create_test_file(percentage)
			print("A test file created successfully.")
		else:
			show_help()
	else:
		show_help()

if __name__ == "__main__":
	main()