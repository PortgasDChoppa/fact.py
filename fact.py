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

#Iterate over the contents of the nested lists to create a new list with the sudoku block
flag = 0
nums = []
while len(sudoku)>=3 and flag==0:
    r = 0
    for i in sudoku:
    while i in range(0,3):
        for j in i:
            if j in range(r,r+3):
                nums.append([i][j])
    r=+3
    for i in nums:
        if len(nums)==len(set(nums))
            flag = 0
        else:
            flag = 1
