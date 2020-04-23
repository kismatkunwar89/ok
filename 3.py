
print("Welcome to this ATM")
print("Please swipe your card")
selection=[1,2,3,4]
pin=int(input("Enter your account pin:"))
if pin==1234:
    print("Choose your transaction")
    print("1.View Balance")
    print("2.Withdraw Balance")
    print("3.Deposit")
    print("4.Exit")
    sel=input("Enter your selection:")
    balance="250"
    balance=int(balance)
    if sel=="1":
        sl=input("do you want any slip:")
        if sl=="yes":
            print("You have Rs.",balance)
            print("Thanks for using our service")
        else:
            print("Thankyou .You have Rs.",balance)
    elif sel=="3":
        amount=int(input("Enter your deposit:"))
        ask=(input("Is this the correct amount, Yes or no ?"))
        if amount>0 :
            if  ask=="yes":
                print("Updated Balance is",amount+balance)
                print("Thanks for using our service")
        else:
            print("please check the deposit")
    elif sel=="2":
        amo=int(input("Enter amount to withdraw:"))
        Ask=input("Is this the correct amount, Yes or no ?")
        if amo<=balance:
            if Ask=="yes":
                print("Updated balance is ",balance-amo)
                print("Thanks for using our service")
            else:
                print("enter valid amount to proceed")
    elif sel=="4":
        ask=input("Do you want to exit?")
        if ask=="yes":
            print("Transaction is completed")
            print("Transaction number: 56789")
            print("Current Intrest Rate : 4 ")
            print("Monthly Intrest Rate: 0.3")
            print("Thanks for choosing our bank")
        else:
            print("Choose any transaction:")
else:
    print("Wrong pin")

    