from SmartNanny_backend.nanny_backend.method.getting_nanny_details import dates, nanny_id
from SmartNanny_backend.nanny_backend.classes.class_nanny_collection import NannyCollection
from SmartNanny_backend.customer_backend.methods.insert_customer import customer_id

nanny_collection = NannyCollection("SmartNanny", "Nanny")

nanny_collection.connecting_nanny_to_employee(dates, customer_id, nanny_id)