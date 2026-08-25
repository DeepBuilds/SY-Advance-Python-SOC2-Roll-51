# Ask the user to enter the input file name
input_file = input("Enter the input file name: ")

# Read the input file
with open(input_file, "r") as file:
    lines = file.readlines()

# Count the number of lines
line_count = len(lines)

# Extract the first two lines
first_two_lines = lines[:2]

# Create a new output file
output_file = "output.txt"

with open(output_file, "w") as file:
    file.writelines(first_two_lines)

# Display the results
print("Total number of lines:", line_count)
print("First two lines:")
print("".join(first_two_lines))
print("Extracted data has been written to", output_file)
'''

Example:-
 input.txt
Python is easy to learn.
File handling is important.
This is the third line.
This is the fourth line.

output:-
Total number of lines: 4
First two lines:
Python is easy to learn.
File handling is important.
Extracted data written to output.txt

'''