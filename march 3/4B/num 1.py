A= {"a", "g", "b","c","d","f"}
B= {"l", "m", "o","b","c","h"}
C= {"k", "i", "j","d","f","c","h"}

print("How many elements are there in set A", len(A))
print("How many elements are there in set B", len(A))

Graph = B - (A | C)

print("How many elements are there in B that is not part of A and C:", len (Graph))
print("i", (C - (A | B)) | (B & C) - (A & B & C))
print("ii", A & C)
print("iii", (B & C) | (B & C))
print("iv", A & C - B)
print("v", A & B & C)
print("vi", B - (A | C))