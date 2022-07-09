from flask import Flask
from about import me
from data import mock_data
import json


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


    # get /api/products
    # return mock_data as a json string
    @app.get("/api/products")
    def get_products():
        return json.dumps(mock_data)


@app.get("api/products/<id>")
def get_product_by_id(id): 
    for prod in mock_data:
       if prod["id"] == id:
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
        results = []
        category = category.lower()
        for prod in mock_data:
            if prod["category"].lower() == category:
                results.append(prod) 
    return json.dumps(results)


    # GET /api/product_cheapest
@app.get("/api/product_cheapest")
def get_cheapest():
    solution = mock_data[0]
    for prod in mock_data:
        if prod[price] < solution[price]:
            solution = prod
    return json.dumps(solution)


    

      

# GET /api/categories
# # return list of categories
# 1 return OK
# 2 travel mock_data and print the category of every product
# 3 put the category in a list and at the end of the for loop, return the list as json

@app.get("/api/categories")
def get_categories():
    categories = []
    for product in mock_data:
       if not cat in categories:
        categories.append(product["category"])
    return json.dumps(categories)


app.run(debug=True)
