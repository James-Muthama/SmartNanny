from Smart_Nanny.SmartNanny_backend.customer_backend.classes.class_customer_collection import CustomerCollection
from Smart_Nanny.SmartNanny_backend.nanny_backend.classes.class_nanny_collection import NannyCollection

nanny_collection = NannyCollection("SmartNanny", "Nanny")
customer_collection = CustomerCollection("SmartNanny", "Customer")

def cancelling_subscription(name):
    customer_id, days = customer_collection.delete_customer(name)
    nanny_collection.deleting_customer_from_nanny_collection(customer_id, days)

    return "It's so unfortunate to see you, name go. We appreciate your time spent with us."