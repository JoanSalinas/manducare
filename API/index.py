from flask import Flask, jsonify, request as req
from pymongo import MongoClient
import pandas as pd
import json 
import random
from bson.json_util import dumps, loads

app = Flask(__name__)
client = MongoClient('localhost', 27017)

db = client.Manducare
ordersCollection = db.orders 
orderProductsCollection = db.order_products


@app.route("/addTicket", methods=["POST"])
def saveTicket():
	data = req.form["data"]
	data = json.loads(data)
	print(data)
	user =  data["user"]
	products =  data["products"]
	order_id = random.randrange(100000)

	ordersCollection.insert_one({"user_id": user, "order_id": order_id})

	print(user, "------------>",products,"--------------------------")
	for product in products:
		print(product)
		orderProductsCollection.insert_one({ "name" : product['name'], "mediaDias" : product['mediaDias'], "order_id" : order_id })
	return user

@app.route("/recomendations", methods=["GET"])
def getRecomendations():
	data = req.form["data"]
	data = json.loads(data)
	print(data)
	products = data["products"]

	print(user, "------------>",products,"--------------------------")
	for product in products:
		print(product)
	return products

@app.route("/recibirTicket", methods=["GET"])
def recibir():
    user = req.form["user"]
    myquery = { "user_id": int(user) }
    print(user)
    mydoc = ordersCollection.find(myquery, { "order_id": 1})
    print(mydoc.count())

    return loads(dumps(list(mydoc)))