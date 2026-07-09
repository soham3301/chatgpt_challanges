countries = {
    "India":{
        "Capital":"New Delhi",
        "Currency":"INR",
        "Population":"1.4B"
    },
    "Brazil":{
        "Capital":"Brasilia",
        "Currency":"BRL",
        "Population":"213M"
    }
}

def display_board():
    try:
        user_input = int(input('''
1. Add Country
2. Display Country Details
3. Edit Information
4. Exit
'''))
        if user_input == 4:
            print("Thanks for using country database.")
            return False, None
        else:
            return True, user_input
    except ValueError:
        print("This input not allowed | Program Closing")
        return False, None

def add_country():
    country_name = input("Enter the Country Name: ").title()
    country_capital = input("Enter the Capital's Name: ").title()
    country_currency = input("Enter the Currency Name: ").upper()
    country_population = input("Enter total Population: ").upper()
    countries[country_name] = {
        "Capital":country_capital,
        "Currency":country_currency,
        "Population":country_population,
    }
    print("Country Added.")

def country_details():
    country_name = input("Enter the Country Name: ").title()
    if country_name in countries:
        for details in countries[country_name]:
            print(f"{details}: {countries[country_name][details]}")
    else:
        helper_country_addition()

def details_correction():
    country_name = input("Enter the Country Name: ").title()
    if country_name in countries:
        country_details = list(countries[country_name])
        for details in country_details:
            print(f"{details}")
        detail_for_correction = input(f"What do you want to edit? Choose from Above\n").title()
        if detail_for_correction in country_details:
            if detail_for_correction == "Capital":
                countries[country_name][detail_for_correction] = input("Enter the corrected value: ").title()
                print(f"{detail_for_correction} corrected.")
            else:
                countries[country_name][detail_for_correction] = input("Enter the correct value: ").upper()
                print(f"{detail_for_correction} corrected.")
        else:
            print("Wront Input.")
    else:
        helper_country_addition()

def helper_country_addition():
    user_consent = input("This country is not in the database. Want to add? Y / N ").lower()
    if user_consent == "y":
        add_country()
    else:
        return True

def function_mapper(user_input):
    saved_functions = {
        1: add_country,
        2: country_details,
        3: details_correction,
    }
    if user_input != None:
        if user_input in saved_functions:
            saved_functions[user_input]()
        else:
            print("Invalid Input")
    else:
        return None

def main():
    program_running = True
    while program_running:
        program_running, user_choice = display_board()
        function_mapper(user_choice)

main()