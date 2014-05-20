def LinearSearch():
        string = input("Please enter a string: ")
        characterfind = input("Please enter a character to find in the string: ")
        found = False
#make an underscore where there is no letter
        output = ""
        for eachChar in string:
            if eachChar == characterfind:
                output = output + characterfind
            found = True
        else:
            output = output + "_"
        if not found:
            print("The character {0} is not in the string {1}".format(characterfind,string))
            print()
            print(output)
