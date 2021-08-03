#!/usr/bin/python3
"""learning about looping"""

def main():
    """runtime code"""

    mylist = ["ford", "chevy", "nissan"]

    for company in mylist:
        print(company)   # this run 3 times...
        print("bottom of the loop")


    zfile = open("example.txt", "w")  # open a file

    for company in mylist:  # loop across our list of car companies
        print(company, file=zfile)  # normally file points to std out

    zfile.close()  # close your open file

    userinput = input("What is your guess? ").lower()  # force all input to be lowercase

    #userinput = userinput.lower() # this would ALSO ensure that userinput is made lowercase

    print(userinput)

    print(userinput.capitalize())

if __name__ == "__main__":
    main()
