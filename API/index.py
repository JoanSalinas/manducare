from flask import Flask, jsonify, request as req
from pymongo import MongoClient
import pandas as pd
import json 
import random
from bson.json_util import dumps, loads
import numpy as np

app = Flask(__name__)
client = MongoClient('localhost', 27017)

db = client.Manducare
ordersCollection = db.orders 
orderProductsCollection = db.order_products

print("carregant dades...")
corrMatrix = pd.read_csv('MatrixBigger3.txt', sep=',', encoding="ISO-8859-1")
productsQuantity = pd.read_csv('productsQuantity.csv', sep=',', encoding="ISO-8859-1")
print("dades carregades")

corrMatrix.index = corrMatrix["product_id"]
corrMatrix.drop(columns="product_id", inplace=True)
print(corrMatrix)
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
	data = req.get_json()
	#data = json.loads(data)
	print(data)
	
	products = data["products"]
	myRatings = products
	user = data["user"]
	#myRatings = {196: 10}
	print(myRatings)
	print(user, "------------>",products,"--------------------------")
	for product in products:
		#myRatings.append({product['id']: product['value']})
		print(product)
	print(myRatings)


	#myRatings = {196: 10}
	simCandidates = pd.Series()
	for key in myRatings:
		print(key)
		print(corrMatrix.columns, str(key['id']))
		sims = corrMatrix[str(key['id'])].dropna()
		sims = sims.map(lambda x: x * key['value'])
		simCandidates = simCandidates.append(sims)

	simCandidates.sort_values(inplace = True, ascending = False)
	simCandidates = simCandidates.groupby(simCandidates.index).sum()
	print(simCandidates)
	dfAuxCount = productsQuantity[productsQuantity['product_id'].isin(list(simCandidates.index))]
	simCandidates = simCandidates.to_frame('puntuacio')
	simCandidates["product_id"] = simCandidates.index
	dfFinal = pd.merge(simCandidates, dfAuxCount, on="product_id")
	dfFinal= dfFinal.astype({'puntuacio': 'int32'})
	dfFinal = dfFinal.sort_values(by=['puntuacio','cuantitat'], ascending=[False,False]).head()

	print('Final', dfFinal)
	return dfFinal.to_json(orient="index")

@app.route("/recibirTicket", methods=["GET"])
def recibir():
    user = req.form["user"]
    myquery = { "user_id": int(user) }
    print(user)
    mydoc = ordersCollection.find(myquery, { "order_id": 1})
    print(mydoc.count())

    return loads(dumps(list(mydoc)))




