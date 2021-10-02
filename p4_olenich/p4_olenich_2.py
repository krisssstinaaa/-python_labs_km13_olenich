# This programm is used for outputting information about level of danger of earthquake based on inputed information by user.

# This block of commands is used for checking input.
def check(x):
    try:
        float(x)
    except ValueError:
        return False 
    return True

magnitude = input("Please enter the magnitude:")
while check(magnitude) == False:
    magnitude = input("Invalid input. Please, try again: ")
float(magnitude)
while float(magnitude) < 0:
    magnitude = input("Invalid input. Please, try again.")
    while check(magnitude) == False:
        magnitude = input("Invalid input. Please, try again: ")
    float(magnitude)
if float(magnitude) < 2:
    print("Your level of danger is - micro.")
if 3 > float(magnitude) >= 2:
    print("Your level of danger is - very minor.")
if 4 > float(magnitude) >= 3:
    print("Your level of danger is - minor.")
if 5 > float(magnitude) >= 4:
    print("Your level of danger is - light.")
if 6 > float(magnitude) >= 5:
    print("Your level of danger is - moderate.")
if 7 > float(magnitude) >= 6:
    print("Your level of danger is - strong.")
if 8 > float(magnitude) >= 7:
    print("Your level of danger is - major.")
if 10 > float(magnitude) >= 8:
    print("Your level of danger is - great.")
if float(magnitude) >= 10:
    print("Your level of danger is - metheoric.")