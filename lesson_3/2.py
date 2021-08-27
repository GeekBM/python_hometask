first_name = input("Enter your first name ")
last_name = input('Enter your last name ')
year = input('Enter your year of birth ')
city = input('Enter your city ')
email = input('Enter your email ')
phone = input('Enter your phone number ')


def personal_data (first_name, last_name, year, city, email, phone):
    return ' '.join([first_name, last_name, year, city, email, phone])


print(personal_data(first_name, last_name, year, city, email, phone))
