#!/usr/bin/python3

def main():
    movies = ["Fellowship of the Ring"]

    movies.append("Two Towers")

    print(movies)


    movies.extend(["Ghostbusters 2", "Lion King", "suitcase", "StAr TrEk 2: Wrath of KAHN", "Teenage Mutant Ninja Turtles", 3.14159])

    print(movies)

    ## exploring how list.remove() works
    #print(movies.remove('suitcase')) # this will cause an error if suitcase is NOT present!
    #print(movies)
    #movies.remove('suitcase')

    ## exploring how list.pop() works
    #print(movies.pop(4))  ## .pop() returns the value it removes!

    ## exploring how del works
    # del movies[4]  # removes suitcase by position


    if 'suitcase' in movies:
        movies.remove('suitcase')
    
    if 'suitcase' in movies:
        movies.remove('suitcase')

    print(movies)


    ## fix "wrath of kahn"
    print(movies[4])

    print(movies[4].title())


    webster = {}
    merriam = {"console": "PS5", "handheld": "Nintendo Switch"}
    print(merriam["console"])

    #print(merriam["PS5"]) # Error!! PS5 is a VALUE, not a KEY!!
    #print(merriam["gameboy"]) # Error!!! THERE IS NO KEY CALLED GAMEBOY! (same as above)
    print(merriam.get("gameboy")) # No error! Returns "None" if not found
    print(merriam.get("blanket", "That value is not within the dict")) # if not found pass back our custom string
    
    print(merriam["handheld"])
    
    merriam["old console"] = "sega genesis"

    print(merriam)


if __name__ == "__main__":
    main()
