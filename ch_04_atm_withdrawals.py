withdrawal_ammount = int(input("How much money you want to withdrawal?\n"))

initial_balance = 5000

if (withdrawal_ammount < 0):
    print("Negative Amount Entered.")
elif (withdrawal_ammount > 5000):
    print("Insufficient Balance.")
else:
    print("Withdrawal Successful.")
    print("Remaining Balance:", (initial_balance - withdrawal_ammount))