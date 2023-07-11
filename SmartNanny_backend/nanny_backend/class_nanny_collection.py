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
        for date in dates:
            # Checking if a date is equal to null
            availability = self.collection.find_one({date: {'$ne': "null"}}).count()

            return availability

    def recommending_days(self, dates):
        date = []
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
        for _ in dates:
            results = self.collection.find_one(query)

            # Iterate over the results and extract the specific value
            matching_value = None

            for document in results:
                if 'Mon' in document:
                    matching_value = document['Mon']
                    break
                elif 'Tue' in document:
                    matching_value = document['Tue']
                    break
                elif 'Wed' in document:
                    matching_value = document['Wed']
                    break
                elif 'Thur' in document:
                    matching_value = document['Thur']
                    break
                elif 'Fri' in document:
                    matching_value = document['Fri']
                    break
                elif 'Sat' in document:
                    matching_value = document['Sat']
                    break

            print(matching_value)









