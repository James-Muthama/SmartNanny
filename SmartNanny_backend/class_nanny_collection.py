from connection import client


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
        inserted_id = self.collection.insert_one(nanny_data).inserted_id
        print(inserted_id)

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
