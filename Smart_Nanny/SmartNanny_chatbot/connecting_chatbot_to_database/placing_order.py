from Smart_Nanny.SmartNanny_backend.nanny_backend.classes.class_nanny_collection import NannyCollection

nanny_collection = NannyCollection("SmartNanny", "Nanny")


def checking_nanny_availability(sentence):
    days = []
    days_of_week = ["monday", "tuesday", "wednesday", "thursday", "friday", "saturday"]

    sentence.lower()

    words = sentence.split()

    for word in words:
        # Check if the word is a day of the week
        if word in days_of_week:
            # Get the shortened version of the day
            shortened_day = word[:3]  # Using the first three letters as the shortened version
            days.append(shortened_day)

    # checking for available nannies with
    available_nannies = nanny_collection.checking_if_nanny_free_on_the_days(days)

    if available_nannies > 0:
        return "We a househelp available on specified days"
    else:
        dates = nanny_collection.recommending_days(days)

        if isinstance(dates, list):
            siku = []
            number_of_days_recommended = len(dates)

            abbrev_to_full = {
                "mon": "Monday",
                "tue": "Tuesday",
                "wed": "Wednesday",
                "thur": "Thursday",
                "fri": "Friday",
                "sat": "Saturday",
            }

            for date in dates:
                siku.append(abbrev_to_full.get(date))

            if number_of_days_recommended == 1:
                return "Unfortunately we don't have househelps available on that day. But we have a househelp " \
                       "available on {day}.".format(day=siku)
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
