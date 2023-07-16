from SmartNanny_backend.customer_backend.methods.insert_customer import customer_id
from SmartNanny_backend.nanny_backend.method.getting_nanny_details import nanny_id
from SmartNanny_backend.customer_backend.classes.class_customer_collection import CustomerCollection

customer_collection = CustomerCollection("SmartNanny", "Customer")
dates = customer_collection.getting_dates(customer_id, nanny_id)
