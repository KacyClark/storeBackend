from flask import Flask

app = Flask("server")
me = {

    "first": "Kacy",
    "last": "Clark v2",
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


    # print(me)

    # print(me["first"])

    # print(me["first"] + " " + (me["last"]))

    # # change values
    # me["age"] = me["age"] + 1
    # me["age"] = 99

    # get /api/about
    # return first last name
