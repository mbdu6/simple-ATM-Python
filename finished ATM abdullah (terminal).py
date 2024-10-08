import os

accountName = ["john doe", "jane doe", "Abdullah", "Muhammad"]
accountNumber = ["9090", "8080", "7070", "5050"]
pinCode = ["1020", "2080", "3070", "4060"]
balance = [1000, 1000, 1000, 2000]

while True:
    print(" ~Welcome to MA Banking Group~ ")
    InputName = input("Please Enter Your Account Name: ").lower()
    if InputName in [name.lower() for name in accountName]:
        index = [name.lower() for name in accountName].index(InputName)
        InputPin = input("Please enter your Pin Number " + InputName + ": ").strip()
        if InputPin != pinCode[index]:
            print("Wrong pin!")
        else:
            print(" ~Welcome", InputName + "~")
            print("Your account number is: ", accountNumber[index])
            print("Your savings account balance is: £" + str(balance[index]))

            while True:
                w_or_d = input("Would you like to withdraw or deposit? (Type 'exit' to quit): ").lower()
                if w_or_d == "withdraw":
                    print(" ~Choose from the Following Denominations or type 'other' to specify a different amount:~")
                    print("1. £20\n2. £40\n3. £60\n4. £80\n5. £100")
                    choose_withdraw = input("Please enter your choice: ").lower()

                    denominations = {"1": 20, "2": 40, "3": 60, "4": 80, "5": 100}
                    amount_withdrawn = denominations.get(choose_withdraw)

                    if amount_withdrawn:
                        if amount_withdrawn <= balance[index]:
                            balance[index] -= amount_withdrawn
                            print(f"Withdrawal successful! Your new Balance is: £{balance[index]}")
                        else:
                            print("Insufficient Funds! You cannot withdraw an amount greater than your balance!")

                    elif choose_withdraw == "other":
                        other_choice = float(input("Please enter the amount you wish to withdraw!: £"))
                        if other_choice <= balance[index]:
                            balance[index] -= other_choice
                            print(f"Withdraw Successful! Your new Balance is: £{balance[index]}")
                        else:
                            print("Insufficient Funds! You cannot withdraw an amount greater than your balance!")
                    else:
                        print("Invalid Choice! Please select a valid option.")

                elif w_or_d == "deposit":
                    amount_deposited = float(input("Enter the amount you wish to Deposit!: £"))
                    balance[index] += amount_deposited
                    print(f"Deposit Successful! Your new Balance is: £{balance[index]}")

                elif w_or_d == "exit":
                    print("Thank you for using MA Banking Group! Have a Lovely Day!")
                    exit()

                else:
                    print("Invalid Option! Please select from the following:\n1. withdraw\n2. deposit\n3. exit")

    else:
        print("Account not found! Please try Again!")