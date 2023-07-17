from SmartNanny_backend.customer_backend.classes.class_customer_collection import CustomerCollection
from SmartNanny_backend.nanny_backend.classes.class_nanny_collection import NannyCollection

nanny_collection = NannyCollection("SmartNanny", "Nanny")
customer_collection = CustomerCollection("SmartNanny", "Customer")
customer_id = input("Id: ")

days = customer_collection.delete_customer(customer_id)
nanny_collection.deleting_customer_from_nanny_collection(customer_id, days)
