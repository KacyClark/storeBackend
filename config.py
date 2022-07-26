import pymongo
import certifi

con_str = "mongodb+srv://kwytaqt:54w4n333@cluster0.whsmi02.mongodb.net/?retryWrites=true&w=majority"


client = pymongo.MongoClient(con_str, tlsCAFile=certifi.where())

db = client.get_database("Chiwowwows")
