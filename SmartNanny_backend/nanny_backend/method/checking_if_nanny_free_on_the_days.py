from SmartNanny_backend.customer_backend.methods.insert_customer import dates
from SmartNanny_backend.nanny_backend.classes.class_nanny_collection import NannyCollection

nanny_collection = NannyCollection("SmartNanny", "Nanny")

availability = nanny_collection.checking_if_nanny_free_on_the_days(dates)

print(availability)


