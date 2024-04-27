# Program to show how to output a grammatically correct error message
# Test 2 Review
#
# This program was broken by introducing two problems.
# For full marks:
# 1) determine what the problems were; 
# 2) explain why they were a problem,
# 3) and make the correction.

# Test cases:
# 0 ---> There were no errors
# 1 ---> There was one error
# >1 --> There were ___ errors

string1 = input("Please enter a test integer (0, 1 or greater than 1): ")
number1 = int(string1)
if number1 == 0:
    print("There were no errors")
elif number1 == 1:
    print("There was one error")
else:
    print("There were", number1, "errors")
# end of program
