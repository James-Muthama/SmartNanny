from SmartNanny_backend.connection import client


class NannyCollection:
    def __init__(self, db_name, collection_name):
        self.client = client
        self.db = self.client[db_name]
        self.collection = self.db[collection_name]

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

    def delete_nanny(self, _id):
        from bson.objectid import ObjectId
        _id = ObjectId(_id)
        self.collection.delete_one({"_id": _id})

    def deleting_customer_from_nanny_collection(self, _id, days):
        from bson.objectid import ObjectId
        _id = ObjectId(_id)

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

    def salary_increment(self, _id, salary_increment):
        from bson.objectid import ObjectId
        _id = ObjectId(_id)

        salary_change = {
            "$inc": {
                "salary": salary_increment
            }
        }

        self.collection.update_one({"_id": _id}, salary_change)

    def checking_if_nanny_free_on_the_days(self, dates):
        available_nannies = 0

        for date in dates:
            # Checking if a date is equal to null
            availability = self.collection.find({date: "null"}).count()

            available_nannies += availability

        return available_nannies

    def getting_nanny_details(self, dates):
        for date in dates:
            results = self.collection.find_one({date: "null"})

            nanny_id, nanny_name, nanny_phone_number = results['_id'], results['name'], results['phone_no']

            return nanny_id, nanny_name, nanny_phone_number, dates

    def connecting_customer_to_nanny(self, dates, _id, nanny_id):
        from bson import ObjectId
        _id = ObjectId(_id)

        for date in dates:
            self.collection.update_one(
                {"_id": nanny_id},
                {"$set":
                    {
                        date: _id
                    }
                }
            )

    def recommending_days(self, dates):
        number_of_days = len(dates)

        if number_of_days == 1:
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

            results = self.collection.find_one(query)

            if results:
                day = next((key for key, value in results.items() if value == "null"), None)
                if day:
                    return day
            else:
                print("No available Nanny's at the moment")

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
                print("No available Nanny's at the moment")

            print(date)

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

                print(date)

            else:
                print("No available Nanny's at the moment")

            print(date)