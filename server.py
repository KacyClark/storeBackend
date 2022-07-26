from flask import Flask, request
from about import me
from data import mock_data
import random 
import json
from config import db 


print("hello from server")
app = Flask("server")

@app.get('/')
def home():
    return "Hello from flask server"

@app.get("/test")
def test():
    return "This is just a test"

    # GET /about
    #show your name
@app.get("/about")
def about():
    return "Kacy Clark"





#######################################################
##########  API ENDPOINTS = PRODUCTS  #################
#######################################################



@app.get("/api/version")
def version():
    return "1.0"


#get /api/about
#return first lastname
@app.get("/api/about")
def about_json():
    return json.dumps(me)   # parse the dict into a json string

def fix_mongo_id(obj):
    obj["id"] = str(obj["_id"])
    del obj["_id"]
    return obj

@app.get("/api/products")
def get_products():
    cursor = db.products.find({})
    results = []     #a list
    for prod in cursor:
        fix_mongo_id(prod)
        results.append(prod)
    return json.dumps(results)

@app.post("/api/products")
def save_product():
    product=request.get_json()    

    db.products.insert_one(product)
    fix_mongo_id(product)
    
    return json.dumps(product)

@app.get("api/products/<id>")
def get_product_by_id(id): 
    for prod in mock_data:
       if str(prod["id"]) == id:
          return json.dumps(prod)
    return "Not Found"


    # travel mock_data list
    # compare product id with the id
    # if they match, return the product as json 
    

    # GET /api/products_category/accessories
    # return all the products in that category

    # travel the list, get every prod
    # if prod -> category is equal to the category variable
    # add prod to the results list
    # outside the for loop, return the results list as json

@app.get("/api/products_category/accessories")
def get_prods_category(accessories):
    print("your category: ", accessories)
    category = category.lower()
    cursor = db.products.find({})
    results = []
    for prod in cursor:
        fix_mongo_id(prod)
        if prod["category"].lower() == category:
            results.append(prod) 
    return json.dumps(results)


@app.get("/api/product_cheapest")
def get_cheapest():
    cursor = db.products.find({})
    solution = cursor[0]
    for prod in cursor:
        if prod["price"] < solution["price"]:
            solution = prod
    fix_mongo_id(solution)    
    return json.dumps(solution)

@app.get("/api/categories")
def get_categories():
    cursor = db.products.find({})
    categories = []
    for product in cursor:
       cat = product["category"]
       if not cat in categories:
           categories.append(cat)
    return json.dumps(categories)

@app.get("/api/count_products")
def get_products_count():
    cursor = db.products.find({})
    count = 0
    for product in cursor:  
        count = count +=1
    return json.dumps({"count": count})\

@app.get("api/search/<text>")
def search_products(text):
    results = []
    text = text.lower()   
    for prod in mock_data:
        if text in prod["title"].lower():
            results.append(prod) 




    

      



app.run(debug=True)
    

