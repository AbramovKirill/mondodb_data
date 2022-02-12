import pymongo
from itertools import count
import datetime

# client = pymongo.MongoClient("mongodb://127.0.0.1:27017/?compressors=disabled&gssapiServiceName=mongodb")
# mongodb://127.0.0.1:27017/?directConnection=true&serverSelectionTimeoutMS=2000&appName=mongosh+1.1.9
client = pymongo.MongoClient("mongodb+srv://12345:12345@cluster0.htukn.mongodb.net/myFirstDatabase?retryWrites=true&w=majority")
db = client.uprav_comp#присв db нашу бд(uprav_comp)
#db = client["uprav_comp"]
coll = db.advertisment#присв coll нашу колекц(advertisment)



#-----Колекция advertisment
#(ПУНКТ1(НАЕВРН))заполн колекц мусором, создаем 10 значений
def create_doc10():
	for i in range(10):
		data = {
			"_id": i,
			"text": "ВІдключення води білвлвл",
			"status": True,
			"time": datetime.datetime.now()
		}
		coll.insert_one(data)
		print(f"{i}: данные записаны!")

#уваляем всё из колекции
def delete_all():
	res = coll.delete_many({})
	print("deleted:", res.deleted_count)

##(ПУНКТ4)удаляем значение с _id:1
def delete_one():#МОЖЕТ НЕ РАБОТАТЬ, ПРОВЕРИТЬ
	coll.delete_one({"_id": 1})

# #(ПУНКТ3(недодел))вставляем значение значение с _id:1 и новыми данными
def insert_one():
	coll.insert_one({"_id": 1, "text": "лампочка пропала", "status": True, "time": datetime.datetime.now()})

# #(ПУНКТ2)выводит всё знач из колекц
def output_all():
	for value in coll.find():
		print(value)
		print("отработало")	

#выводит 3 (первые) знач из колекц	
def output_3():
	for value in coll.find().limit(3):#вывод 3 знач
		print(value)
		print("отработало")	

#выводит все знач - 1 сорт по увел, -1 по убыванию	
def output_sort1():
	for value in coll.find().sort("_id", 1):#1 сорт по увел, -1 по убыванию
		print(value)
		print("отработало")	

#выводит все знач - 1 сорт по увел, -1 по убыванию	
def output_sort_1():
	for value in coll.find().sort("_id", -1):#1 сорт по увел, -1 по убыванию
		print(value)
		print("отработало")	

#выведет всю информацию об оголош у которого _id: 2
#может заменить на i, чтобы можно было задать какой _id через def
def output_id():
	query = {"_id": 2}
	for value in coll.find(query):
		print(value)
		print("отработало")

# #выведет информацию об всех оголош, но без значения "status", "time"
def output_all2():
	query = {"status": True}
	for value in coll.find(query, {"_id": 1, "text": 1}):#показываем только _id и text всех оголош
		print(value)
		print("отработало")

def update_one():
	current = {"_id": 2}#значения котор нужно найти
	new_data = {"$set": {"_id": 15}}#знач котор нужно указать, мы на них замен, использ модификатор "$set"
	coll.update_one(current, new_data)#и заменяем