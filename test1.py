
from flask import Flask
from about import me


def run_test():
    print("Test 1 - dictionaries")


    me = {
        "first": "Kacy",
        "last": "Clark",
        "age": 39,
        "hobbies": [],
        "address": {
            "number": "123",
            "street": "N Loop",
            "city": "Louisville",
            "state": "Kentucky",
            "zip": "40220"
        }
    }


    print(me)

    print(me["first"])

    print(me["first"] + " " + (me["last"]))

    # change values
    me["age"] = me["age"] + 1
    me["age"] = 99

    #add new keys
    me["preferred_color"] = "Black"
    print(me)

     # read if exists
    if "middle_name" in me:
      print(me["middle_name"])

   #print the full address on a single line
      print(me["number"] + " " + me["street"] + " " + me["city"] + " " + me["state"] + " " + me["zip"])
      address = me["address"]
      print(address)
      print(type(address))

      print(f'{address["number"]} #{address["street"]}, {address["city"]}, {address["state"]}, {address["zip"]}')







    run_test()
    app.run()