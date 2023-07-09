from validator import nanny_validator
from connection import client

client.SmartNanny.command("collMod", "Nanny", validator=nanny_validator)