#!/usr/bin/env python
# HW03_ex06
# (1) Please comment your code.
# (2) Please be thoughtful when naming your variables.
# (3) Please remove development code before submitting.
################################################################################
# Exercise 1
# When you submit only include your final function: compare





################################################################################
# Exercise 2
# When you submit only include your final function: hypotenuse
# Do develop incrementally. Do not share here.





################################################################################
# Exercise 3
# When you submit only include your final function: is_between





################################################################################
# Exercise 6
# When you submit only include your final function: is_palindrome





################################################################################
# Exercise 7
# When you submit only include your final function: is_power





################################################################################
def main():
    """Your functions will be called within this function."""
    ############################################################################
    # Use this space temporarily to call functions in development:
    print("Hello World!")







    ############################################################################
    # Uncomment the below to test and before commiting:
    # Exercise 1
    print compare(1,1)
    print compare(1,2)
    print compare(2,1)
    # # Exercise 2
    print hypotenuse(1,1)
    print hypotenuse(3,4)
    print hypotenuse(1.2,12)
    # # Exercise 3
    print is_between(1,2,3)
    print is_between(2,1,3)
    print is_between(3,1,2)
    print is_between(1,1,2)
    # # Exercise 6
    print is_palindrome("Python")
    print is_palindrome("evitative")
    print is_palindrome("sememes")
    print is_palindrome("oooooooooooo")
    # # Exercise 7
    print is_power(28,3)
    print is_power(27,3)
    print is_power(248832,12)
    print is_power(248844,12)


if __name__ == "__main__":
    main()