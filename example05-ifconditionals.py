#!/usr/bin/python3
"""RZFeeser | Alta3 Research
   A script to show how to make decisions with conditionals"""


def main(): 
    """decision making"""

    userinput = input("What is your name? ")

    if userinput[0].isupper():
        print("Your name begins with a capital letter.")

   

    if userinput[0].lower() in ["a", "e", "i", "o", "u"]:
        print("Your name begins with a vowel.")

    # in an if / else conditional, only ONE condition can be true

    if userinput[0].isdigit():
        print("Your name begins with a digit.")
    else:
        print("Your name does not begin with a digit.")


    # in all cases this runs
    print("thanks for running this program!")

if __name__ == "__main__":
    main()
