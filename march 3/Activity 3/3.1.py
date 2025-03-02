FN = input ("Enter your First Name: ")
LN = input ("Enter your last name: ")
age = input ("Enter your age: ")

fullname = FN + " " + LN
Slice = FN[:4]

print ("Full Name: ", fullname)
print ("Sliced Name: ", Slice)

greet = ("hello, {Slice}! Welcome. You are ", age, " years old")
print = (greet)