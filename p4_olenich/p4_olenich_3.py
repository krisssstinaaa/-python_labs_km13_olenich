# This programm is used for calculating total sum to pay for phone bill.

# This block of commands is used for checking input.
def check(x):
    try:
        float(x)
    except ValueError:
        return False
    return True



minutes = input("Please, enter how much minutes you used: ")
while check(minutes) == False or float(minutes) < 0 :
    minutes = input("Invalid input. Please, try again: ")
float(minutes)
if float(minutes) <= 50 :
    print("You have to pay 100 UAH.")
if 50 < float(minutes) <= 100 :
    print("You have to pay 150 UAH.")
if float(minutes) > 100 :
    total = (float(minutes) - 100)*2 + 150
    print("You have to pay", total, "UAH")

