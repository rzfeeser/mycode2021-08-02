#!/usr/bin/env python3
# create a list of strings

def main():

    farms = [{"name": "NE Farm", "agriculture": ["sheep", "cows", "pigs", "chickens", "llamas", "cats"]},
     {"name": "W Farm", "agriculture": ["pigs", "chickens", "llamas"]},
     {"name": "SE Farm", "agriculture": ["chickens", "carrots", "celery"]}]

    for x in farms:
        print("\nThe farm is " + x.get("name"), end="")
        #print("\nThe farm " + x.get("name"), "has the following agriculture" + x.get("agriculture"), end="")
        #print(f"\nThe farm {x.get('name')} has the following agriculture {x.get('agriculture')}", end="")
        print("\nThe farm is", x.get("name"), "has the following agriculture", x.get("agriculture"), end="")
        if x not in farms:
            print(" - NOT AN APPROVED AGRICULTURAL FARM", end="")
    print("\nOur loop has ended.") # print when loop has finished
if __name__ == "__main__":
    main()



#print( "Fourth test - .keys()" )
#print( switch.keys() )

#print( "Fifth test - .values()" )
#print( switch.values() )
