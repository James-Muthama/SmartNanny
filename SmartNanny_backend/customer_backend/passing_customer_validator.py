from customer_validator import customer_validator
from SmartNanny_backend.connection import client

client.SmartNanny.command("collMod", "Customer", validator=customer_validator)