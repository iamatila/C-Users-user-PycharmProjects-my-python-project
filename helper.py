calculationMinutes = 24 * 60
calculationSeconds = 24 * 60 * 60
calculationHours = 24

unitName1 = "minutes"
unitName2 = "seconds"
unitName3 = "hours"
print("20 days  are " + str(20 * calculationMinutes) + " minutes")
print(f"15 days are {15 * calculationMinutes} {unitName1}")
print(f"35 days are {35 * calculationMinutes} {unitName1}")
print(f"85 days are {85 * calculationSeconds} {unitName2}")
print(f"7 days are {7 * calculationSeconds} {unitName2}")


def days_to_units(numOfDays):
    print(f"{numOfDays} days are {numOfDays * calculationMinutes} {unitName1}")


days_to_units(15)
days_to_units(35)
days_to_units(85)
days_to_units(7)


def days_to_units2(numOfDays2, conversion_units):
    if conversion_units == "hours":
        return f"{numOfDays2} days are {numOfDays2 * calculationHours} {unitName3}"
    elif conversion_units == "minutes":
        return f"{numOfDays2} days are {numOfDays2 * calculationMinutes} {unitName1}"
    elif conversion_units == "seconds":
        return f"{numOfDays2} days are {numOfDays2 * calculationSeconds} {unitName2}"
    else:
        return "Unsupported Unit"


def validate_and_execute(days_and_unit_dictionary):
    try:
        user_input_int = int(days_and_unit_dictionary["days"])
        # we are converting only for positive numbers
        if user_input_int > 0:
            calculated_value = days_to_units2(user_input_int, days_and_unit_dictionary["unit"])
            print(calculated_value)
        elif user_input_int == 0:
            print( f"You entered {user_input_int}, please enter a valid positive number.")
        else:
            print( "You entered a Negative number, so try again with a positive number")
    except ValueError:
        print(f"Please enter a digit, not {user_input_int}")

user_input_message = "Hey user, enter the number of days and the conversion unit: \n"