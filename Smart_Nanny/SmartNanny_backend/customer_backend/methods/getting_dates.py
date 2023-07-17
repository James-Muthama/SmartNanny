from Smart_Nanny.SmartNanny_backend.customer_backend.classes.class_customer_collection import CustomerCollection
from Smart_Nanny.SmartNanny_backend.customer_backend.methods.insert_customer import customer_id

customer_collection = CustomerCollection("SmartNanny", "Customer")
dates = customer_collection.getting_dates(customer_id)

