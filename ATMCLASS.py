class bank:
    def __init__(self):
        self.closingBal=0
    def display(self):
        print("Enter your options:")
        print("1 for deposit\n2 for withdraw")
        getOption=input()
        if getOption == '1':
            self.deposite()
        elif getOption == '2':
            self.withdraw()
        elif getOption!=1 or getOption!=2:
            print("Thank")
            return
        print("Your closing balance is:",self.closingBal)
        print("Do you want to continue:")
        a=input()
        if a=="Y"or a=="y":
            self.display()
        else:
            print("Thank for visiting our bank")
    def deposite(self):
        depositeAmount=int(input("Enter you deposite amount:"))
        self.closingBal=self.closingBal+depositeAmount
        return self.closingBal
    def withdraw(self):
        withdrawAmount = int(input("Enter you withdraw amount:"))
        if self.closingBal>=withdrawAmount:
            self.closingBal = self.closingBal - withdrawAmount
            print("After withdraw your balance amount is:",self.closingBal)
        else:
            print("No sufficient balance")
        return self.closingBal
bankobj=bank()
bankobj.display()
