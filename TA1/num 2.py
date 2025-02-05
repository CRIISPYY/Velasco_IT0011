string = input("Enter here: ")
num = 0

for i in string:
    if i.isdigit():
        num += int(i)
print(num)        