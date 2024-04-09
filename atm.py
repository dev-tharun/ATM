money = 1000
total = 0
card = input("Enter card: ")
password = input("Enter password: ")
for x in range(1, 4):
    print("No of count -", x)
    if card == "tharun" and password == "1234":
        if x == 1:
            while total < money:
                total += 100
                print("Count -", total)
            print("Total amount -", total)
            total = 0
        else:
            print("Only one attempt is possible")
    elif card == "tharun" or password == "1234":
        print("Either card or password is wrong")
    else:
        print("Both card and password are wrong")

print("Thank you for using")


