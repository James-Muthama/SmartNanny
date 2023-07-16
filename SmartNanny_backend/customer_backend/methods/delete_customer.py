from SmartNanny_backend.customer_backend.classes.class_customer_collection import CustomerCollection

nanny_collection = CustomerCollection("SmartNanny", "Nanny")

customer_collection = CustomerCollection("SmartNanny", "Customer")
customer_id = input("Id: ")

customer_collection.delete_customer(customer_id)
nanny_collection.deleting_nanny_from_customer_collection(customer_id)
