from SmartNanny_backend.nanny_backend.method.checking_if_nanny_free_on_the_days import available_nannies, dates
from SmartNanny_backend.customer_backend.methods.insert_customer import customer_id
from SmartNanny_backend.nanny_backend.classes.class_nanny_collection import NannyCollection

nanny_collection = NannyCollection("SmartNanny", "Nanny")

if available_nannies > 0:
    nanny_id, nanny_name, nanny_number = nanny_collection.connecting_customer_to_nanny(dates, customer_id)