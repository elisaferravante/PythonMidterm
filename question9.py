def calculate_days_since_birth(birthday):
    """
    Calculate  number of days that have passed since the birth year of a person,
    excluding birth year and current year.

    :param birthday: birthday in the format "DD-MM-YYYY"
    :return: amount of days (whole years only).
    """
    # 1: Extract the birth year from the input string
    birth_year = int(birthday.split("-")[2])

    # 2: Get the current year
    current_year = 2024  # Assume this is the current year

    # 3: Calculate number of whole years between birth and current year
    years_passed = current_year - birth_year - 1  # Exclude birth and current year

    # 4: Convert the years to number of days (365 days x year)
    days_passed = years_passed * 365

    # Return the result
    return days_passed

# Example of use
print(calculate_days_since_birth("11-06-2004"))  # Example of birthday (my own)