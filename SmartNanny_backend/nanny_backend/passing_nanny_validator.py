from nanny_validator import nanny_validator
from SmartNanny_backend.connection import client

client.SmartNanny.command("collMod", "Nanny", validator=nanny_validator)

