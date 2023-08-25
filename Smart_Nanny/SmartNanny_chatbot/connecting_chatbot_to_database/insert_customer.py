# Import necessary classes and modules
from Smart_Nanny.SmartNanny_backend.customer_backend.classes.class_customer_collection import CustomerCollection
from Smart_Nanny.SmartNanny_backend.customer_backend.classes.class_customer import Customer
import datetime
import re


# Function to extract customer information from the input line
def extract_customer_info(sentence):
    # Define a regular expression pattern to match the expected input format
    pattern = r"^(.*), (\d{10,12}), ([\w\s-]+), \[([\w\s,]+)\]$"
    match = re.match(pattern, sentence)

    if match:
        # Extract customer information from the captured groups
        name = match.group(1)
        phone_number = match.group(2)
        address = match.group(3)
        days_string = match.group(4)

        # Use the checking_nanny_availability function to convert days string into an array of abbreviated days
        days = getting_shortname_for_days(days_string)
        return name, phone_number, address, days
    else:
        return "Please add your name again in the format of your name, your phone-number, your address as house " \
               "number- apartments or estat name - Closest road to your house, days you will need a househelp inside " \
               "of [ ] for example James Muthama, 0712345678, S90 - Lata Aparatments - Lata Rd,[Monday, Thursday]"


# Function to convert days string into an array of abbreviated days
def getting_shortname_for_days(siku):
    days = []
    days_of_the_week = {
        "monday": "Monday",
        "tuesday": "Tuesday",
        "wednesday": "Wednesday",
        "thursday": "Thursday",
        "friday": "Friday",
        "saturday": "Saturday",
        "sunday": "Sunday"
    }

    siku = siku.lower()

    words = siku.split()

    for word in words:
        # Check if the word is a day of the week
        day = days_of_the_week.get(word)

        if day:
            # Get the shortened version of the day
            shortened_day = day[:3]  # Using the first three letters as the shortened version
            days.append(shortened_day)

    return days


def inserting_customer_to_db(name, phone_number, address, days):
    # Create an instance of CustomerCollection
    customer_collection = CustomerCollection("SmartNanny", "Customer")

    # Prompt the user to enter customer information
    input_line = input("Enter customer information: ")

    # Extract customer information using the extract_customer_info function
    name, phone_number, address, days = extract_customer_info(input_line)

    # Create a new Customer object with the extracted information
    new_customer = Customer(
        name,
        int(phone_number),
        address.split("-"),
        datetime.datetime.now(),
        len(days),
        days,
        "null",
        "null",
        int(len(days) * 1000)
    )

    # Insert the new customer into the database
    customer_id = customer_collection.insert_customer(new_customer)
    return "Customer inserted with ID:, customer_id"


def inserting_customer_to_database(sentence):
    answer = extract_customer_info(sentence)

    if answer == "Please add your name again in the format of your name, your phone-number, your address as house " \
                 "number- apartments or estat name - Closest road to your house, days you will need a househelp inside " \
                 "of [ ] for example James Muthama, 0712345678, S90 - Lata Aparatments - Lata Rd,[Monday, Thursday]":
        return answer
    else:
        name, phone_number, address, days = extract_customer_info(sentence)

        response = inserting_customer_to_db(name, phone_number, address, days)

        return response
