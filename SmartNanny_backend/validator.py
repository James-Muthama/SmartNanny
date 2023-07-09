nanny_validator = {
    "$jsonSchema": {
        "bsonType": "object",
        "required": ["name", "id_number", "date_of_birth", "phone_no", "address", "employment_start_date", "Mon", "Tue",
                     "Wed", "Thur", "Fri", "Sat", "salary", "employment_end_date"],
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
                "pattern": "^\\d{4}-\\d{2}-\\d{2}$",
                "description": "Enter Date of Birth in the format YYYY-MM-DD"
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
                "enum": ["string", "null"],
                "pattern": "^\\d{4}-\\d{2}-\\d{2}$",
                "description": "Enter a string for the day they started employment"
            },
            "Mon": {
                "enum": ["null", "objectId"],
                "description": "This is the customer_id they are meant to work for on Monday"
            },
            "Tue": {
                "enum": ["null", "objectId"],
                "description": "This is the customer_id they are meant to work for on Tuesday"
            },
            "Wed": {
                "enum": ["null", "objectId"],
                "description": "This is the customer_id they are meant to work for on Wednesday"
            },
            "Thur": {
                "enum": ["null", "objectId"],
                "description": "This is the customer_id they are meant to work for on Thursday"
            },
            "Fri": {
                "enum": ["null", "objectId"],
                "description": "This is the customer_id they are meant to work for on Friday"
            },
            "Sat": {
                "enum": ["null", "objectId"],
                "description": "This is the customer_id they are meant to work for on Saturday"
            },
            "salary": {
                "bsonType": "int",
                "description": "Enter a int for the amount of money to be paid to this nanny"
            },
            "employment_end_date": {
                "enum": ["string", "null"],
                "pattern": "^\\d{4}-\\d{2}-\\d{2}$",
                "description": "Enter a string for the day they started employment"
            }
        }
    }
}
