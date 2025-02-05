def charcount(Input):
    vowelnum = 0
    consnum = 0
    spacecount = 0
    noletnum = 0
    
    vowel = "aeiouAEIOU"
    consonant = "bcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZ"

    for character in Input:
        if character in vowel:
            vowelnum += 1
        elif character in consonant:
            consnum += 1
        elif character == ' ':
            spacecount += 1
        else:
            noletnum += 1
        
    print("Number of vowels: ", vowelnum)
    print("Number of consonant letters: ", consnum)
    print("Number of spaces: ", spacecount)
    print("Number of non-letter characters: ", noletnum)
    
text = input("Enter the string: ")
charcount(text)