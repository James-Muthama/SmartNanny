from SmartNanny_backend.connection import client


class CustomerCollection:
    def __init__(self, db_name, collection_name):
        self.client = client
        self.db = self.client[db_name]
        self.collection = self.db[collection_name]

    def insert_customer(self, customer):
        customer_data = {
            "name": customer.name,
            "phone_no": customer.phone_no,
            "address": customer.address,
            "subscription_start_date": customer.subscription_start_date,
            "days_in_a_week": customer.days_in_a_week,
            "days_of_the_week": customer.days_of_the_week,
            "nanny_id": customer.nanny_id,
            "discount_id": customer.discount_id,
            "payment_amount": customer.payment_amount
        }
        inserted_id = self.collection.insert_one(customer_data).inserted_id
        return inserted_id

    def delete_customer(self, _id):
        from bson.objectid import ObjectId
        _id = ObjectId(_id)

        self.collection.delete_one({"_id": _id})

        return 1

    def deleting_nanny_from_customer_collection(self, _id):
        query = {
            '$or': [
                {'Mon': _id},
                {'Tue': _id},
                {'Wed': _id},
                {'Thur': _id},
                {'Fri': _id},
                {'Sat': _id}
            ]
        }
        results = self.collection.find_one(query)

        matched_field = None

        for condition in query['$or']:
            if condition in results:
                matched_field = list(condition.keys())[0]
                break

        results.update(
            {"$set":
                {
                    matched_field: "null"
                }
             }
        )

    def getting_dates(self, _id):
        document = self.collection.find_one({"_id": _id})

        dates = document["days_of_the_week"]

        return dates

    def connecting_nanny_to_customer(self, customer_id, nanny_id):
        from bson import ObjectId
        _id = ObjectId(nanny_id)

        self.collection.update_one(
            {"_id": customer_id},
            {"$set":
                {
                    "nanny_id": _id
                }
            }
        )
