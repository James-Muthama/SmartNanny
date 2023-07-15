from SmartNanny_backend.nanny_backend.method.checking_if_nanny_free_on_the_days import dates
from SmartNanny_backend.customer_backend.methods.insert_customer import customer_id
from SmartNanny_backend.nanny_backend.method.getting_available_nanny import nanny_id
from SmartNanny_backend.nanny_backend.classes.class_nanny_collection import NannyCollection

nanny_collection = NannyCollection("SmartNanny", "Nanny")

nanny_collection.connecting_customer_to_nanny(nanny_id, dates, customer_id)

