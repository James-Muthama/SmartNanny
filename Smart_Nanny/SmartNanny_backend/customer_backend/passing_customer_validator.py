from Smart_Nanny.SmartNanny_backend.customer_backend.customer_validator import customer_validator
from Smart_Nanny.SmartNanny_backend.connection import client

client.SmartNanny.command("collMod", "Customer", validator=customer_validator)