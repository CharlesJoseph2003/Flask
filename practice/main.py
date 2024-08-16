from flask import Flask
from flask_restful import Api, Resource

app = Flask(__name__)
api = Api(app)

# hello

# list of names
names = {"tim": {"age": 19, "gender": "male"},
         "bill": {"age": 70, "gender": "male"}}

class HelloWorld(Resource):
    # Resource represents collection of entities that can be accessed and manipulated using GET POST PUT and DELETE requests
    def get(self, name):
        return names[name]

    # Iterating through the dict of names and getting the values associated with the key
    # Changed from set to dictionary
    # Information have to be serializable, in json format
    # want to return json serializable objects so have to return dictionaries in general

api.add_resource(HelloWorld, "/helloworld/<string:name>")

if __name__ == "__main__":
    app.run(debug=True)