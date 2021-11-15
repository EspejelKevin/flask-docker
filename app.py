from flask import Flask, jsonify, request
from stores import stores


app = Flask(__name__)


@app.route("/")
def home():
    return "<h1>Welcome to my first REST API with flask</h1>"


# POST /store
@app.route("/store", methods=["POST"])
def create_store():
    name_store = request.json["store"]
    items = request.json["items"]
    new_store = {
        "store": name_store,
        "items":items
    }
    stores.append(new_store)
    return jsonify({"new store": new_store})


# GET /store/<string:name_store>
@app.route("/store/<string:name_store>")
def get_store(name_store):
    store = [store for store in stores if store["store"] == name_store ]
    if store:
        return jsonify({"store": store[0]})
    return jsonify({"message": "resource not found"})


# GET /store
@app.route("/store")
def get_stores():
    return jsonify({"stores":stores})


# POST /store/<string:name_store>/item {name_store: price:}
@app.route("/store/<string:name_store>/item", methods=["POST"])
def create_item(name_store):
    request_data = request.get_json()
    for store in stores:
        if store["store"] == name_store:
            new_item = {
                "name": request_data["name"],
                "price":request_data["price"]
            }
            store["items"].append(new_item)
            return jsonify({"new item": new_item})
    return jsonify({"message":"error, check the data"})


# GET /store/<string:name_store/item
@app.route("/store/<string:name_store>/item")
def get_item(name_store):
    store = [store for store in stores if store["store"] == name_store ]
    if store:
        return jsonify({"items":store[0]["items"]})
    return jsonify({"message": "resource not found"})


if __name__ == "__main__":
    app.run(port=5000)

