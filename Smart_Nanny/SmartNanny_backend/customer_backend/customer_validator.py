customer_validator = {
    "$jsonSchema": {
        "bsonType": "object",
        "required": ["name", "phone_no", "address", "subscription_start_date", "days_in_a_week", "days_of_the_week",
                     "nanny_id", "discount_id", "payment_amount"],
        "properties": {
            "name": {
                "bsonType": "string",
                "description": "Enter a string for the name"
            },
            "phone_no": {
                "bsonType": "int",
                "minLength": 10,
                "description": "Enter a int of length 10 for the phone number"
            },
            "address": {
                "bsonType": "array",
                "description": "Enter a string for the address in the format HouseNumber, ApartmentsName, Road"
            },
            "subscription_start_date": {
                "bsonType": "date",
                "description": "Auto adds when the customer starts subscription"
            },
            "days_in_a_week": {
                "bsonType": "int",
                "description": "This is takes in the number of days they want a nanny"
            },
            "days_of_the_week": {
                "bsonType": "array",
                "description": "This is the days they want a nanny to come"
            },
            "nanny_id": {
                "anyOf": [
                    {"bsonType": "null"},
                    {"bsonType": "objectId"},
                    {"bsonType": "string"}
                ],
                "description": "This the nanny connected to the customer"
            },
            "discount_id": {
                "enum": ["null", "objectId"],
                "description": "This is there incase of any discounts"
            },
            "payment_amount": {
                "bsonType": "int",
                "description": "This is the amount payable"
            }
        }
    }
}
