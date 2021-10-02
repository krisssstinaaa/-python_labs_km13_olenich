# This programm is used for printing information about recepient of the letter.

# This function is used for checking whether input is correct.
def check_int(x):
    try:
        int(x)
    except ValueError:
        return False
    return True

# This block of commands is used for entering information from the user.
user_first_name = input("Please, enter your first name: ")
while user_first_name.isalpha() == False :
    user_first_name = input("Invalid input. Please, try again: ")
user_last_name = input("Enter your last name: ")
while user_last_name.isalpha() == False :
    user_last_name = input("Invalid input. Please, try again: ")
user_number = input("Now enter your phone number: ")
while check_int(user_number) == False:
    user_number = input("Invalid input. Please, try again: ")
int(user_number)
user_street = input("Enter your street name: ")
while user_street.isalpha() == False :
    user_street = input("Invalid input. Please, try again: ")
user_house_number = input("Enter your house number: ")
while check_int(user_house_number) == False:
    user_house_number = input("Invalid input. Please, try again: ")
int(user_house_number)
user_flat_number = input("Enter your flat number: ")
while check_int(user_flat_number) == False:
    user_flat_number = input("Inval0id input. Please, try again: ")
int(user_flat_number)
user_city = input("Please, enter your city: ")
while user_city.isalpha() == False :
    user_city = input("Invalid input. Please, try again: ")
user_zip_code = input("Now enter your ZIP code: ")
while check_int(user_zip_code) == False:
    user_zip_code = input("Invalid input. Please, try again: ")
int(user_zip_code)
user_country = input("Finally, enter your country: ")
while user_country.isalpha() == False :
    user_country = input("Invalid input. Please, try again: ")


# This block of commands is used for outputing entered information on the screen.
print("There is enough information about recepient to send a letter. Check it out:")
print(user_first_name, user_last_name)
print(user_number)
print("Str.", user_street, user_house_number, ", ap.", user_flat_number,",", user_city)
print(user_zip_code)
print(user_country)

