from class_customer_collection import CustomerCollection
from class_customer import Customer
import datetime
import pprint

customer_collection = CustomerCollection("SmartNanny", "Customer")

new_customer = Customer(
    input("Name: "),
    int(input("Phone number: ")),
    (input("Address: ").split("-")),
    datetime.datetime.now(),
    int(input("How many days of the week do they want a Nanny: ")),
    input("Days of the week they want the nanny to come: ").split(","),
    input("Nanny Id: "),
    input("Discount Id: "),
    int(input("Payable amount: "))
)

customer_id = customer_collection.insert_customer(new_customer)

dates = customer_collection.getting_dates(customer_id)

