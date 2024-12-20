from bson.json_util import dumps
from bson import json_util
import json
from pymongo import MongoClient

def data_store(add_card_data):
    uspass = 'rohit8982'
    connect = f"mongodb+srv://rohit8982:{uspass}@cluster0.lyn00.mongodb.net/"
    client = MongoClient(connect)
    db = client['Card_Detail']  # Replace with your database name
    # check is vehicle already registred or not
    collection = db['user_detail']
    collection.insert_one(add_card_data)
    print(add_card_data)
    return ''

def data_retrive():
    uspass = 'rohit8982'
    connect = f"mongodb+srv://rohit8982:{uspass}@cluster0.lyn00.mongodb.net/"
    client = MongoClient(connect)
    db = client['Card_Detail']  # Replace with your database name
    # check is vehicle already registred or not
    collection = db['user_detail']
    data_DB = collection.find()
    data_str = json_util.dumps(data_DB)
    data_str = json.loads(data_str)
    print(data_str)
    return data_str