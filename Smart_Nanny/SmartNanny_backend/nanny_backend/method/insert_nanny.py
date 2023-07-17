from Smart_Nanny.SmartNanny_backend.nanny_backend.classes.class_nanny_collection import NannyCollection
from Smart_Nanny.SmartNanny_backend.nanny_backend.classes.class_nanny import Nanny
import datetime

nanny_collection = NannyCollection("SmartNanny", "Nanny")

new_nanny = Nanny(
    input("Name: "),
    int(input("ID number: ")),
    input("Date of birth: "),
    int(input("Phone number: ")),
    input("Address: "),
    datetime.datetime.now(),
    "null",
    "null",
    "null",
    "null",
    "null",
    "null",
    int(input("Salary: ")),
    int(input("Phone number used to pay: "))
)

nanny_collection.insert_nanny(new_nanny)


