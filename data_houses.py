import pymongo
from itertools import count
import datetime

client = pymongo.MongoClient("mongodb+srv://12345:12345@cluster0.htukn.mongodb.net/myFirstDatabase?retryWrites=true&w=majority")
db = client.uprav_comp
coll2 = db.houses


#-----Колекция houses
def create_doc10():
	for i in range(10):
		data = {
			"_id": i,
			"text": "пропала вода",
			"status": True,
			"time": datetime.datetime.now()
		}
		coll2.insert_one(data)
		print(f"{i}: данные записаны!")

def delete_all():
	res = coll2.delete_many({})
	print("deleted:", res.deleted_count)

def delete_one():
	coll2.delete_one({"_id": 1})

def insert_one():
	coll2.insert_one({"_id": 1, "text": "лампочка пропала", "status": True, "time": datetime.datetime.now()})

def output_all():
	for value in coll2.find():
		print(value)
		print("отработало")	
	
def output_3():
	for value in coll2.find().limit(3):
		print(value)
		print("отработало")	

def output_sort1():
	for value in coll2.find().sort("_id", 1):
		print(value)
		print("отработало")	
	
def output_sort_1():
	for value in coll2.find().sort("_id", -1):
		print(value)
		print("отработало")	

def output_id():
	query = {"_id": 2}
	for value in coll2.find(query):
		print(value)
		print("отработало")

def output_all2():
	query = {"status": True}
	for value in coll2.find(query, {"_id": 1, "text": 1}):
		print(value)
		print("отработало")

def update_one():
	current = {"_id": 2}
	new_data = {"$set": {"_id": 15}}
	coll2.update_one(current, new_data)