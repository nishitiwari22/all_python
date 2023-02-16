# Q2) python program to merge two files into a third file in hindi

# Solution:
# Creating a list of filenames
filenames = ['file1.txt', 'file2.txt']

# Open file3 in write mode
with open('file3.txt', 'w') as outfile:

    # Iterate through list
    for names in filenames:

        # Open each file in read mode
        with open(names) as infile:

            # read the data from file1 and file2 and write it in file3
            outfile.write(infile.read())

        # Add '\n' to enter data of file2 from next line
        outfile.write("\n")