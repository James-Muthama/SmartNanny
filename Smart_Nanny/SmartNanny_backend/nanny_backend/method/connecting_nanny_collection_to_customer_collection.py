from Smart_Nanny.SmartNanny_backend.customer_backend.methods.getting_dates import dates
from Smart_Nanny.SmartNanny_backend.nanny_backend.classes.class_nanny_collection import NannyCollection
from Smart_Nanny.SmartNanny_backend.customer_backend.methods.insert_customer import customer_id
from Smart_Nanny.SmartNanny_backend.customer_backend.classes.class_customer_collection import CustomerCollection


nanny_collection = NannyCollection("SmartNanny", "Nanny")
customer_collection = CustomerCollection("SmartNanny", "Customer")

# checking for available nannies with
available_nannies = nanny_collection.checking_if_nanny_free_on_the_days(dates)

# connecting nannies to customers if nanny is available
if available_nannies > 0:
    nanny_id, nanny_name, nanny_phone_number, dates = nanny_collection.getting_nanny_details(dates)
    
    # updating dates in Nanny Collection with the customer_id
    nanny_collection.connecting_customer_to_nanny(dates, customer_id, nanny_id)

    customer_collection.connecting_nanny_to_customer(customer_id, nanny_id)

# if there are no available nannies on the dates requested by customers recommend a day
else:
    dates = nanny_collection.recommending_days(dates)
    