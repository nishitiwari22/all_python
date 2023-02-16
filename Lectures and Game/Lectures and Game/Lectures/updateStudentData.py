'''
Consider the directory ./StudentData
It contains /Marks and /Name
/Marks conatins a text file marks.txt which contains "studentRollnumber studentMark" followed by a newline
/Name conatins a text file name.txt which contains "studentRollnumber studentName" followed by a newline
You have to write a program that creates the a few file "newData.txt" in ./StudentData
which contains "studentRollnumber studentMark studentName" followed by a new line for every student

'''

try:
	#opens and reads the file if they exist (default mode is read)
	marks = open("./StudentData/Marks/marks.txt")
	name = open("./StudentData/Name/name.txt")

	#will be used for mapping the rollnumber(key) and list of mark and name(value)
	rollNumberMapping = {}


	#iterates through every line of the file marks and adds marks as the value for the rollnumber in rollNumberMaping
	for line in marks:
		studentRollNumber, studentMarks = line.split(' ')[0], line.split(' ')[1].split('\n')[0]
		rollNumberMapping[studentRollNumber] = [studentMarks]

	#iterates through every line of the file name and appends name to the value of the rollnumber in rollNumberMaping
	for line in name:
		studentRollNumber, studentName = line.split(' ')[0], line.split(' ')[1].split('\n')[0]
		rollNumberMapping[studentRollNumber].append(studentName)

	#creates new file in write mode, it will create file if it doesn't already exist
	newFile = open("./StudentData/newData.txt", "w+")
	for rollNumber, Data in rollNumberMapping.items():
		#write the roll number, marks and name to the new file
		newFile.write(rollNumber + " " + Data[0] + " " + Data[1] + "\n")
except IOError:
	print("File does not appear to exist")	
