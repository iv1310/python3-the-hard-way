from sys import argv; from os.path import exists; script, from_file, to_file = argv

print(f"Copying from {from_file} to {to_file}.\nThe input file is {len(from_file)} bytes long.\nDoes the output file exist? {exists(to_file)}.")

with open(from_file, "r") as in_file, open(to_file, "w") as out_file:
    content = in_file.read(); out_file.write(content); print("Alright, all done!")

# By not closing files you are possibly wasting system resources. Also, other processes that want to to access the file after the code was executed might not be able to do so due to still being opened by the code.

# Using something like this indata=open(filename).read() means, we dont need to close the file in_file.close() because when you reach the end of the script, it should already closed by Python once that one line runs.
