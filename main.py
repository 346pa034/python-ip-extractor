import re
import sys
import argparse
import os.path

parser = argparse.ArgumentParser()
parser.add_argument("-i", metavar="/path/to/file", help="specify the input file from which to extract the IP addresses")
parser.add_argument("-o", metavar="/path/to/file", help="specify the ouput file in which to store the extracted IP addresses")
parser.add_argument("-u", metavar="default: true", help="when specified and/or set to True, will return only unique IP addresses", default=True)
args = parser.parse_args()

if __name__ == "__main__":
	input_file = args.i
	output_file = args.o
	unique = args.u


	# make sure to overwrite the existing file
	output_file_exists = os.path.isfile(output_file)
	if output_file_exists:
		print(f"Removing existing output file '{output_file}'")
		os.remove(output_file)


	# found pattern at https://www.geeksforgeeks.org/extract-ip-address-from-file-using-python/
	pattern = re.compile(r"(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})")
	with open(input_file, "r") as ifile:
		lines = ifile.readlines()

	# fill ips buffer. when the unique flag is set
	# also check for uniqueness of the ip address
	ips = []

	if unique:

		print(f"Checking for unique IP addresses")
		for line in lines:
			result = pattern.search(line)
			if result is not None and result[0] not in ips:
				ips.append(result[0])
		print(f"Found {len(ips)} unique IP addresses")

	else:

		print(f"Checking for non-unique IP addresses")
		for line in lines:
			result = pattern.search(line)
			if result is not None:
				ips.append(result[0])
		print(f"Found {len(ips)} non-unique IP addresses")

	# write ips buffer to file
	with open(output_file, "a+") as ofile:
		ofile.write(f"{ip}\n")

	print(f"SUCCESS! Wrote IP addresses to '{output_file}'")
