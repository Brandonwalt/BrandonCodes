"""Function to get an integer from the user. 

The user is asked to enter an integer in the range a to b, inclusive.
If the number is incorrect, the function re-asks until the conditions
are met, or the user quits with CTRL-C.
If the user quits with CTRL-C, the function raises SystemExit. The
caller should catch it for a graceful exit.
"""

import sys

def get_integer(a, b):
    """Prompt the user for an integer in the range a to b, inclusive."""
    number = False
    while not number :
        try:
            try:
                Test_number = input("Number ( {} to {} inclusive)? ".format(a,b))
                Int_number = int(Test_number)
                if Int_number <= a and Int_number >= b or Int_number >= a and Int_number <= b  :
                    return Int_number
                else:
                    raise ValueError()
            except ValueError:
                print ("The number must be in the range {} to {} inclusive".format(a,b))
                continue
            else:
                break
        except KeyboardInterrupt:
            print(" ok goodbye")
            exit()


# DEFINE THE FUNCTION HERE!


# DO NOT MAKE ANY CHANGES TO THE TESTING CODE IN MAIN
if __name__ == "__main__":
    # List of pairs to be tested
    testlist = [(1,99), (99,1), (0,1), (2,2), (-10,-5), (0,0), (-(2**32),2**32)]
    passed = True  # optimistic
    for pair in testlist:
        print("\nTesting range {} to {}".format(pair[0], pair[1]))
        try:
            number = get_integer(pair[0], pair[1])
            if isinstance(number, int) and number >= min(pair) and number <= max(pair):
                print("The number {} is correct".format(number))
            else:
                print("The number {} is NOT correct".format(number))
                passed = False
        except SystemExit:
            print("The function returned SystemExit...\n"
                "type any key to proceed to the next test, "
                "or type CTRL-C to exit testing.")
            try:
                input("")  # dummy input, proceed or stop
            except KeyboardInterrupt:
                break  # break out of for loop
    if passed:
        print("Function tests passed!")
    else:
        print("Function tests failed!")
