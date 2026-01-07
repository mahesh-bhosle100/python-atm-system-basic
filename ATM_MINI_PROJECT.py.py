--------------- ATM PROGRAM ------------------

balance = 5000
attempt = 0
transactions = []

mobile = 9922125846
pan = "4307"

pin_code = 1234   

-------------- LOGIN ------------------

while True:

    while attempt < 3:
        pin = int(input("Enter PIN: "))

        if pin == pin_code:
            print("\nLogin successful\n")

            
            while True:
                print("\n1. Check Balance")
                print("2. Deposit")
                print("3. Withdraw")
                print("4. Transaction History")
                print("5. Exit")

                choice = input("Enter your choice: ")

                if choice == "1":
                    print(f"Your balance is: {balance}")

                elif choice == "2":
                    amount = int(input("Enter deposit amount: "))

                    if amount <= 0:
                        print("Invalid amount")
                    else:
                        balance += amount
                        transactions.append(f"Deposited: {amount}")
                        print(f"Balance after deposit: {balance}")

                elif choice == "3":
                    amount = int(input("Enter withdraw amount: "))

                    if amount <= 0:
                        print("Invalid amount")
                    elif amount > balance:
                        print("Insufficient balance")
                    else:
                        balance -= amount
                        transactions.append(f"Withdrawn: {amount}")
                        print(f"Balance after withdrawal: {balance}")

                elif choice == "4":
                    if not transactions:
                        print("No transactions yet")
                    else:
                        print("\n--- Transaction History ---")
                        for t in transactions:
                            print(t)

                elif choice == "5":
                    print("Thank you for using ATM")
                    break

                else:
                    print("Invalid choice")

            break  

        else:
            print("Wrong PIN")
            attempt += 1

   ------------ PIN RESET ------------------


    if attempt == 3:
        print("\nYour card is blocked")
        print("Start PIN reset process")

        enter_mobile = int(input("Enter registered mobile number: "))
        enter_pan = input("Enter PAN: ")

        if enter_mobile == mobile and enter_pan == pan:
            new_pin = int(input("Enter new PIN: "))
            confirm_pin = int(input("Confirm new PIN: "))

            if new_pin == confirm_pin:
                pin_code = new_pin
                attempt = 0
                print("\nPIN reset successful. Please login again.\n")
            else:
                print("PIN not matched")
        else:
            print("Wrong mobile number or PAN")

    else:
        break

    

                
