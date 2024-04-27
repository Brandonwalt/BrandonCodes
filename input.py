# Program to input two numbers and determine if one is divisible by the other
# TPRG 1131 W2016 Test 2 Review
#
# This program was broken by introducing two problems.
# For full marks:
# 1) determine what the problems were; 
# 2) explain why they were a problem,
# 3) and make the correction.
#
# Test all three cases:
# number1 number2
#  84      21
#   3      93
#   5       2

string1 = input("Please enter the first integer: ")
string2 = input("Please enter the second integer: ")
number1 = int(string1/string2)
number2 = int(string2/string1)
if number1 % number2 == 0:
    print(number1, "is divisible by", number2)
elif number2 % number1 == 0:
    print(number2, "is divisible by", number1)
else:
    print("numbers are not exact divisors")
# end of program
