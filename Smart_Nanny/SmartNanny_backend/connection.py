from dotenv import load_dotenv, find_dotenv
import os
import pprint
from pymongo import MongoClient

load_dotenv(find_dotenv())

# Connecting to MongoDB
password = os.environ.get("MONGO_PWD")
connection_string = f"mongodb+srv://JamesMuthama:{password}@smartnanny.b8ztu49.mongodb.net/?retryWrites=true&w=majority&authSource=admin"

client = MongoClient(connection_string)

# Prints out our databases in MongoDB
dbs = client.list_database_names()
#print(dbs)

# Prints out our Collections in MongoDB
collections = client.SmartNanny.list_collection_names()
#print(collections)

