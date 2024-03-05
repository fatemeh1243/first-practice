accounts = []  # lets make a bankaccount yay! </3
selectnum = input("Enter your choice:\n '1' Deposit\n '2' Withdraw\n '3' Check Balance ")
acc_num = input("Enter account number: ")
amount = float(input("Enter amount to withdraw: "))
while True:
    if selectnum == "1" :
        amount = float(input("Enter amount to deposit: "))  
        if acc_num in accounts:
            accounts[acc_num] += amount
            print(f"Deposited {amount} into account {acc_num}")
        else:
            print("Account not found.")
    elif selectnum == "2" :
        if acc_num in accounts:
            if accounts[acc_num] >= amount:
                accounts[acc_num] -= amount
                print(f"Withdrew {amount} from account {acc_num}")
            else:
                print("Insufficient balance.")
        else:
            print("Account not found.")
    elif selectnum == "3" :
        if acc_num in accounts:
            print(f"Balance in account {acc_num}: {accounts[acc_num]}")
        else:
            print("acc not found.")
    else:
        print("Please try again.")
