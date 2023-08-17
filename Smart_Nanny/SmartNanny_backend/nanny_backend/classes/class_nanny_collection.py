from Smart_Nanny.SmartNanny_backend.connection import client


class NannyCollection:
    def __init__(self, db_name, collection_name):
        self.client = client
        self.db = self.client[db_name]
        self.collection = self.db[collection_name]

    # Function for inserting a new nanny
    def insert_nanny(self, nanny):
        nanny_data = {
            "name": nanny.name,
            "id_number": nanny.id_number,
            "date_of_birth": nanny.date_of_birth,
            "phone_no": nanny.phone_no,
            "address": nanny.address,
            "employment_start_date": nanny.employment_start_date,
            "Mon": nanny.mon,
            "Tue": nanny.tue,
            "Wed": nanny.wed,
            "Thur": nanny.thur,
            "Fri": nanny.fri,
            "Sat": nanny.sat,
            "salary": nanny.salary,
            "payment_number": nanny.payment_number
        }
        self.collection.insert_one(nanny_data)

    # Function for deleting a nanny, the function takes in their id and deletes them from the database
    def delete_nanny(self, _id):
        # converting id to type objectId

        from bson.objectid import ObjectId
        _id = ObjectId(_id)

        # deletes the nanny with the matching id

        self.collection.delete_one({"_id": _id})

    # Function for deleting a customer who is connected to a nanny, the function takes in the id of the customer and
    # the days the customer had the requested the nanny
    def deleting_customer_from_nanny_collection(self, _id, days):
        # converting id to type objectId

        from bson.objectid import ObjectId
        _id = ObjectId(_id)

        # checks the days inputted that have match with the id and converts the id to null

        for day in days:
            query = {
                '$and': [
                    {day: _id}
                ]
            }
            results = self.collection.find_one(query)

            if results:
                day = next((key for key, value in results.items() if value == _id), None)

                self.collection.update(
                    {day: _id},
                    {"$set":
                        {
                            day: "null"
                        }
                    }
                )

    # Function that increases the amount of a nanny's salary, the function takes the nanny_id and the amount of money
    # to be increased to the salary i.e 1000 will increase the salary by 1000
    def salary_increment(self, _id, salary_increment):
        # converting id to type objectId

        from bson.objectid import ObjectId
        _id = ObjectId(_id)

        # passing the $inc operator that increases the value on "salary" and equating it to salary_change
        salary_change = {
            "$inc": {
                "salary": salary_increment
            }
        }

        # updating the nanny with the id above and passing the salary_change
        self.collection.update_one({"_id": _id}, salary_change)

    # Function checks if there are any free nanny's on the days that the customer is requesting for
    def checking_if_nanny_free_on_the_days(self, dates):
        available_nannies = 0

        # checks the days if any nanny is free
        for date in dates:
            # Checking if a date is equal to null
            availability = self.collection.find({date: "null"}).count()

            available_nannies += availability

        return available_nannies

    # Function takes in the dates the customer would like to have the nanny and finds one nanny free on the said days
    # and returns the nanny_id, name, phone number and date
    def getting_nanny_details(self, dates):
        for date in dates:
            results = self.collection.find_one({date: "null"})

            nanny_id, nanny_name, nanny_phone_number = results['_id'], results['name'], results['phone_no']

            return nanny_id, nanny_name, nanny_phone_number, dates

    # Function updates the days on the nanny from null to the customer id
    def connecting_customer_to_nanny(self, dates, _id, nanny_id):
        # converting id to type objectId

        from bson import ObjectId
        _id = ObjectId(_id)

        # updates each date from null to the customer_id
        for date in dates:
            self.collection.update_one(
                {"_id": nanny_id},
                {"$set":
                    {
                        date: _id
                    }
                }
            )

    # Function recommends days if there's no nanny available on the days suggested by the customer
    def recommending_days(self, dates):
        # gets the number of days suggested by the customer

        number_of_days = len(dates)

        # if one day was suggested give back any other one day when a nanny is free
        if number_of_days == 1:

            # uses the or operator to choose between days and equates it to query

            query = {
                '$or': [
                    {'Mon': "null"},
                    {'Tue': "null"},
                    {'Wed': "null"},
                    {'Thur': "null"},
                    {'Fri': "null"},
                    {'Sat': "null"}
                ]
            }

            # finds one nanny that satisfies query and returns here whole table
            results = self.collection.find_one(query)

            # once a result ia found it is searched for a key with a value null and returns it
            if results:
                day = next((key for key, value in results.items() if value == "null"), None)
                if day:
                    return day

            # if no result is found they return no available Nanny's at the moment
            else:
                return "No available Nanny's at the moment"

        elif number_of_days == 2:
            date = []
            query = {
                '$or': [
                    {"$and": [{"Mon": "null"}, {"Thur": "null"}]},
                    {"$and": [{"Tue": "null"}, {"Fri": "null"}]},
                    {"$and": [{"Wed": "null"}, {"Sat": "null"}]}
                ]
            }

            results = self.collection.find_one(query)

            if results:
                for clause in query['$or']:
                    if '$and' in clause:
                        and_clause = clause['$and']
                        for field in and_clause:
                            days = field.items()
                            for field_name, value in days:
                                if results[field_name] == value:
                                    date.append(field_name)
            else:
                return "No available Nanny's at the moment"

            return date

        elif number_of_days == 3:
            date = []
            query = {
                '$or': [
                    {"$and": [{"Mon": "null"}, {"Wed": "null"}, {"Fri": "null"}]},
                    {"$and": [{"Tue": "null"}, {"Thur": "null"}, {"Sat": "null"}]}
                ]
            }

            results = self.collection.find_one(query)

            if results:
                for clause in query['$or']:
                    if '$and' in clause:
                        and_clause = clause['$and']
                        for field in and_clause:
                            days = field.items()
                            for field_name, value in days:
                                if results[field_name] == value:
                                    date.append(field_name)

                return date

            else:
                return "No available Nanny's at the moment"

