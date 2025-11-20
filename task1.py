x = input("Enter any string: ")
y = ""
for i in x:
    if i.islower():
        y += i
if not y:
    print("No lowercase letters found")
else:
    print(y)
    ascii = [ord(c) for c in y]
    print("ASCII values of lowercase letters:", ascii)