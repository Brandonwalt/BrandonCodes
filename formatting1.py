"""TPRG 1131 Test 1 Task B-1 Example (starter file).

Define a function format_greeting() that takes a list of two strings
representing a name and a greeting and returns a string that contains
a greeting. 
For example:
["Fred", "Hello"]
becomes
"Hello, Fred!"

If the function receives less than 2 strings in the list, it should return
an empty string "".

The main program is already given below, you must define the function.
"""

def format_greeting(words):
    """Return a personal greeting formatted as "<name>,<greeting>!".
    """
    if len(words) < 2:
        return ""
    else:
        return words[1] + ", jjj" + words[0] + "!"


if __name__ == "__main__":
    print("running doctest.")
    import doctest
    doctest.testmod()











