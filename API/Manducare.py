from flask import Flask, jsonify, request as req
from pymongo import MongoClient
import datetime
import pandas as pd
from pymongo import MongoClient
import json 
import random
client = MongoClient()




app = Flask(__name__)

client = MongoClient()

client = MongoClient('localhost', 27017)
db = client.Manducare
Orderscollection = db.orders 

orderproductscollection = db.order_products





@app.route("/AñadirTicket/", methods=["POST"])
def cargaDatos():
    user = req.form["user"]
    productos = req.form["productos"]
    order_id = random.randrange(100000)
    #ticket = jsonify({"ticket": ticket })
    Orderscollection.insert_one({"user_id": user, "order_id": order_id})
    productos = [{"nombre": "manzana","media":15},{"nombre": "pera","media":15}]
    print("------------>",productos,"--------------------------")
    #productos = json.loads({"productos": productos })
    for product in productos:
        
        orderproductscollection.insert_one({"nombre":product['nombre'],"media":product['media'],"order_id": order_id})

    return user

    
    












 