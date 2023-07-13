from SmartNanny_backend.customer_backend.classes.class_customer_collection import CustomerCollection
from SmartNanny_backend.customer_backend.classes.class_customer import Customer
import datetime

customer_collection = CustomerCollection("SmartNanny", "Customer")

new_customer = Customer(
    input("Name: "),
    int(input("Phone number: ")),
    (input("Address: ").split("-")),
    datetime.datetime.now(),
    int(input("How many days of the week do they want a Nanny: ")),
    input("Days of the week they want the nanny to come: ").split(","),
    "null",
    "null",
    int(input("Payable amount: "))
)

customer_id = customer_collection.insert_customer(new_customer)



