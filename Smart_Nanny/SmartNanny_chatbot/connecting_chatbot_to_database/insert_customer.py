# Import necessary classes and modules
from Smart_Nanny.SmartNanny_backend.customer_backend.classes.class_customer_collection import CustomerCollection
from Smart_Nanny.SmartNanny_backend.customer_backend.classes.class_customer import Customer
from Smart_Nanny.SmartNanny_backend.nanny_backend.classes.class_nanny_collection import NannyCollection
import datetime
import re

nanny_collection = NannyCollection("SmartNanny", "Nanny")
customer_collection = CustomerCollection("SmartNanny", "Customer")


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
               "of [ ] for example James Muthama, 0712345678, S90 - Lata Aparatments - Lata Rd,[on Monday and Thursday]"


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


def matching_nanny_and_customer(customer_id, days):
    # checking for available nannies with
    available_nannies = nanny_collection.checking_if_nanny_free_on_the_days(days)

    # connecting nannies to customers if nanny is available
    if available_nannies > 0:
        nanny_id, nanny_name, nanny_phone_number, dates = nanny_collection.getting_nanny_details(days)

        # updating dates in Nanny Collection with the customer_id
        nanny_collection.connecting_customer_to_nanny(dates, customer_id, nanny_id)

        customer_collection.connecting_nanny_to_customer(customer_id, nanny_id)

        return f"We have successfully connected you to one of our nannies. Her name is (nanny_name) and if you'd like to" \
               f" reach her, her number is (nanny_phone_number). She will be getting back to you in the course of the " \
               f"week and will begin work on the coming week on the specified days. Thank you for working with us."

    else:
        dates = nanny_collection.recommending_days(days)

        if isinstance(dates, list):
            siku = []
            number_of_days_recommended = len(dates)

            abbrev_to_full = {
                "Mon": "Monday",
                "Tue": "Tuesday",
                "Wed": "Wednesday",
                "Thur": "Thursday",
                "Fri": "Friday",
                "Sat": "Saturday",
            }

            for date in dates:
                siku.append(abbrev_to_full.get(date))

            if number_of_days_recommended == 1:
                return "Unfortunately we don't have househelps available on that day. But we have a househelp " \
                       "available on {day}.".format(day=siku[0])
            elif number_of_days_recommended == 2:
                return "Unfortunately we don't have househelps available on that day. But we have a househelp " \
                       "available on {day1} and {day2}.".format(day1=siku[0], day2=siku[1])
            elif number_of_days_recommended == 3:
                return "Unfortunately we don't have househelps available on that day. But we have a househelp " \
                       "available on {day1}, {day2} and {day3}.".format(day1=siku[0], day2=siku[1], day3=siku[2])
            elif number_of_days_recommended == 4:
                return "Unfortunately we don't have househelps available on that day. But we have a househelp " \
                       "available on {day1}, {day2}, {day3} and {day4}.".format(day1=siku[0], day2=siku[1],
                                                                                day3=siku[2], day4=siku[3])
            elif number_of_days_recommended == 5:
                return "Unfortunately we don't have househelps available on that day. But we have a househelp " \
                       "available on {day1}, {day2}, {day3}, {day4} and {day5}.".format(day1=siku[0], day2=siku[1],
                                                                                        day3=siku[2], day4=siku[3],
                                                                                        day5=siku[4])
        else:
            return dates


def inserting_customer_to_db(name, phone_number, address, days):
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

    response = matching_nanny_and_customer(customer_id, days)

    return response


def inserting_customer_to_database(sentence):
    answer = extract_customer_info(sentence)

    if answer == "Please add your name again in the format of your name, your phone-number, your address as house " \
                 "number- apartments or estat name - Closest road to your house, days you will need a househelp inside " \
                 "of [ ] for example James Muthama, 0712345678, S90 - Lata Aparatments - Lata Rd,[on Monday and " \
                 "Thursday]":
        return answer
    else:
        name, phone_number, address, days = extract_customer_info(sentence)

        response = inserting_customer_to_db(name, phone_number, address, days)

        return response
