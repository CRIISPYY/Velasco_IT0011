def print_pattern():
    
    num = 1

    while num <= 7:
        count = 1
        while count <= num:
            print(num, end="")
            count += 1
        print()
        print("")
        
        num += 2
print_pattern()