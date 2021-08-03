#!/usr/bin/python3
"""RZFeeser | Alta3 Research
   A script to show how to make decisions with conditionals"""


def main(): 
    """decision making"""

    userinput = input("What is your name? ")

    # use the if / elif / else block to "choose one"
    if userinput[0].isupper():
        print("Your name begins with a capital letter.")
    elif userinput[0].isdigit():
        print("Your name begins with a digit.")
    elif userinput[0].islower():
        print("Your name begins with a lowercased letter.")
    else:
        print("I believe your name begins with a special character!")

if __name__ == "__main__":
    main()
