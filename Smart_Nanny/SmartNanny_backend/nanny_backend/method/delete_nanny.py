from Smart_Nanny.SmartNanny_backend.nanny_backend.classes.class_nanny_collection import NannyCollection
from Smart_Nanny.SmartNanny_backend.customer_backend.classes.class_customer_collection import CustomerCollection

customer_collection = CustomerCollection("SmartNanny", "Customer")
nanny_collection = NannyCollection("SmartNanny", "Nanny")

nanny_id = input("Id: ")

nanny_collection.delete_nanny(nanny_id)
customer_collection.deleting_nanny_from_customer_collection(nanny_id)

