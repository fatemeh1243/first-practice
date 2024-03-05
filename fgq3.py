x = float(input("Enter the first num x :"))
y = float(input("Enter the second num y :"))
answer=(float)
selectnum = input("Enter smth: \n1. Sum\n2. Difference\n3. Multiple\n4. Divide\n")
while True:
    if selectnum == "1" :
        answer = x + y
        print(answer)
    elif selectnum == "2":
        answer = x - y
        print(answer)
    elif selectnum == "3":
        answer = x * y
        print(answer)
    elif selectnum == "4":
        answer = x / y
        print(answer)
    else:
        print("wrong!try again.")
        break
