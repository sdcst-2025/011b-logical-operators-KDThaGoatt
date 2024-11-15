#! python3

"""
Problem 2
Factors are positive integers that divide evenly into another integer.
The user will enter in two numbers. Determine if the smaller is a factor of the larger

You can use an if statement to determine which is larger, or use the
max() function to determine the larger of the two
(2 marks)

inputs:
an integer
an integer

outputs:
xx is a factor of yy
xx is not a factor of yy

examples:
Enter a number: 10
Enter another number: 2
2 is a factor of 10

Enter a number: 4
Enter another number: 25
4 is not a factor of 25
"""

x = float(input("Enter a number"))
y = float(input("Enter another number"))

smallNum = min(x, y)
largeNum = max(x, y)

if largeNum % smallNum == 0:
    print(f"{smallNum} is a factor of {largeNum}")

else:
    print(f"{smallNum} is not a factor of {largeNum}")