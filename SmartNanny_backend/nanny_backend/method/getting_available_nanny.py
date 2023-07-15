from SmartNanny_backend.nanny_backend.method.checking_if_nanny_free_on_the_days import available_nannies, dates
from SmartNanny_backend.nanny_backend.classes.class_nanny_collection import NannyCollection

nanny_collection = NannyCollection("SmartNanny", "Nanny")

if available_nannies > 0:
    nanny_id, nanny_name, nanny_number = nanny_collection.getting_available_nanny(dates)

