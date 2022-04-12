#Simplified Sudoku
#Creator: Diego Sebastian Cobos A.
#11320699
#Date created: April 10th, 2022
#Instructor: Jeff Long
#Description: Check if a simplified sudoku(file) is valid or not

#Read the file
filename = input("Enter file name: ")
f = open(filename,'r') #open file in read mode

#Create a nested list for the numbers in our sudoku
sudoku = []
for line in f:
    line = line.rstrip().split()
    line = [int(i) for i in line]
    sudoku.append(line)
#Take the sudoku size from the list
N = sudoku.pop(0)
multiples = N[0]/3
#Create a list with all the numbers in the nested list
nums = []
flag=0
for i in range(0, len(sudoku)):
    for j in range(0, len(sudoku)):
        nums.append(sudoku[i][j])

#Count the number of times a number is present on the list
for i in nums:
    if i in range(1,10):               #Check if the numbers are from 1 to 9
        if nums.count(i) > multiples:  #Check for repetition
            flag=0
        else:
            flag=1
    else:
       flag=0
#If the count is equal to one, the sudoku is valid
if flag==1:
    print('True')
else:
    print('False')
