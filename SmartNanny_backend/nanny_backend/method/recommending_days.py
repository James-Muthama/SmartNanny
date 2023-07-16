from SmartNanny_backend.nanny_backend.method.getting_nanny_details import dates
from SmartNanny_backend.nanny_backend.classes.class_nanny_collection import NannyCollection
from SmartNanny_backend.nanny_backend.method.checking_if_nanny_free_on_the_days import available_nannies

nanny_collection = NannyCollection("SmartNanny", "Nanny")

if available_nannies == 0:
    dates = nanny_collection.recommending_days(dates)
