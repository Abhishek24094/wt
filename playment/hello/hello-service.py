import json
from flask import Flask
from flask_restful import Api, Resource, reqparse
app = Flask(__name__)
api = Api(app)
class Output(Resource):
    def get(self):
        dic={"message":"hello"}
	dic=json.dumps(dic)
	return (dic)
class Version(Resource):
    def get(self):
        dic={"version" : "v1.0"}
	dic=json.dumps(dic)
	return (dic)
api.add_resource(Output, "/health")
api.add_resource(Version, "/version")
app.run(host='0.0.0.0',port=3000,debug=True)

