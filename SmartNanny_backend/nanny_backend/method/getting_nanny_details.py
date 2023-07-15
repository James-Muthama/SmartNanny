from SmartNanny_backend.customer_backend.methods.getting_dates import dates
from SmartNanny_backend.nanny_backend.classes.class_nanny_collection import NannyCollection

nanny_collection = NannyCollection("SmartNanny", "Nanny")

nanny_id, nanny_name, nanny_phone_number, dates = nanny_collection.getting_nanny_details(dates)