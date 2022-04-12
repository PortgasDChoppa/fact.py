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
while len(sudoku)>=3 and flag==0:
    r = 0
    while r+3<=int(N[0]) and flag==0:
        nums = []
        for i in range(0, 3):
            for j in range(0+r, r+3):
                nums.append(sudoku[i][j])
        for i in nums:
            if i in range(1, 10):
                if (i in set(nums)) and len(nums) == len(set(nums)) and flag==0:
                    flag = 0
                else:
                    flag = 1
            else:
                flag = 1
        r=r+3
    del sudoku[0:3]

if flag==0:
    print('True')
else:
    print('False')

