nanny_validator = {
    "$jsonSchema": {
        "bsonType": "object",
        "required": ["name", "id_number", "date_of_birth", "phone_no", "address", "employment_start_date", "Mon", "Tue",
                     "Wed", "Thur", "Fri", "Sat", "salary", "payment_number"],
        "properties": {
            "name": {
                "bsonType": "string",
                "description": "Enter a string for the name"
            },
            "id_number": {
                "bsonType": "int",
                "minLength": 8,
                "description": "Enter a minimum of 8 integers for the National ID"
            },
            "date_of_birth": {
                "bsonType": ["string"],
                "description": "Enter Date of Birth in the format DD-MM-YYYY"
            },
            "phone_no": {
                "bsonType": "int",
                "minLength": 10,
                "description": "Enter a int of length 10 for the phone number"
            },
            "address": {
                "bsonType": "string",
                "description": "Enter a string for the address"
            },
            "employment_start_date": {
                "bsonType": "date",
                "description": "Enter a string for the day they started employment"
            },
            "mon": {
                "anyOf": [
                    {"bsonType": "null"},
                    {"bsonType": "objectId"},
                    {"bsonType": "string"}
                ],
                "description": "This is the customer_id they are meant to work for on Monday"
            },
            "tue": {
                "anyOf": [
                    {"bsonType": "null"},
                    {"bsonType": "objectId"},
                    {"bsonType": "string"}
                ],
                "description": "This is the customer_id they are meant to work for on Tuesday"
            },
            "wed": {
                "anyOf": [
                    {"bsonType": "null"},
                    {"bsonType": "objectId"},
                    {"bsonType": "string"}
                ],
                "description": "This is the customer_id they are meant to work for on Wednesday"
            },
            "thur": {
                "anyOf": [
                    {"bsonType": "null"},
                    {"bsonType": "objectId"},
                    {"bsonType": "string"}
                ],
                "description": "This is the customer_id they are meant to work for on Thursday"
            },
            "fri": {
                "anyOf": [
                    {"bsonType": "null"},
                    {"bsonType": "objectId"},
                    {"bsonType": "string"}
                ],
                "description": "This is the customer_id they are meant to work for on Friday"
            },
            "sat": {
                "anyOf": [
                    {"bsonType": "null"},
                    {"bsonType": "objectId"},
                    {"bsonType": "string"}
                ],
                "description": "This is the customer_id they are meant to work for on Saturday"
            },
            "salary": {
                "bsonType": "int",
                "description": "Enter a int for the amount of money to be paid to this nanny"
            },
            "payment_number": {
                "bsonType": "int",
                "description": "Enter a number that will be used for m-pesa payment"
            }
        }
    }
}
