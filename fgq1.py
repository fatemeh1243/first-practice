print("welcome")
x = input("Enter anything: ")
if x[0:] in "0123456789" :
    print("integer")
elif x[0:] == ',':
    print("list")
else:
    print("string")