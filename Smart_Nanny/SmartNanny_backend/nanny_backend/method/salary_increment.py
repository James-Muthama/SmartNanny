from Smart_Nanny.SmartNanny_backend.nanny_backend.classes.class_nanny_collection import NannyCollection

nanny_collection = NannyCollection("SmartNanny", "Nanny")
nanny_collection.salary_increment(input("Id: "), int(input("Salary Increases by: ")))