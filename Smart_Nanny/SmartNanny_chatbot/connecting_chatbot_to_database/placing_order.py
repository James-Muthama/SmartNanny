from Smart_Nanny.SmartNanny_backend.nanny_backend.classes.class_nanny_collection import NannyCollection

nanny_collection = NannyCollection("SmartNanny", "Nanny")


def checking_nanny_availability(sentence):
    days = []
    days_of_week = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]

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

        number_of_days_recommended = len(dates)

        if number_of_days_recommended == 1:
            return "Unfortunately we don't have househelps available on that day. But we have a househelp available " \
                   "on {day}.".format(day=dates)
        elif number_of_days_recommended == 2:
            return "Unfortunately we don't have househelps available on that day. But we have a househelp available " \
                   "on {day1} and {day2}.".format(day1=dates[0], day2=dates[1])
        elif number_of_days_recommended == 3:
            return "Unfortunately we don't have househelps available on that day. But we have a househelp available " \
                   "on {day1}, {day2} and {day3}.".format(day1=dates[0], day2=dates[1], day3=dates[2])