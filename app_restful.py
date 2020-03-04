from flask import Flask, request
from flask_restful import Resource, Api
import json
from skill import Skills,Skills_mod

app = Flask(__name__)
api = Api(app)

developers = [
	{'id':'0','name':'Elliot','skills':['Python','Hacking']},
	{'id':'1','name':'Darlene','skills':['Pentest','Hacking']}
]

class Developer(Resource):

    def get(self, id):

        try:
            response = developers[id]
        except IndexError:
            message = 'Developer with ID {} does not exist.'.format(id)
            response = {'status':'Error','message':message}
        except Exception:
            message = 'Unknown Error. Search for the API developer.'
            response = {'status':'Error','message':message}
        return response

    def put(self,id):
        data = json.loads(request.data)
        developers[id] = data
        return data

    def delete(self,id):
        try:
            response = developers.pop(id)
        except IndexError:
            message = 'Developer with ID {} does not exist.'.format(id)
            response = {'status':'Error','message':message}
        except Exception:
            message = 'Unknown Error. Search for the API developer.'
            response = {'status':'Error','message':message}
        return {'status':'success','message':'deleted record'}

class Welcome(Resource):
    def get(self):
        return "Welcome to my first API!"

class Developers_list(Resource):
    def get(self):
        return developers

    def post(self):
        data = json.loads(request.data)
        position = len(developers)
        data['id']= position
        developers.append(data)
        return {'status':'success','message':'inserted record'}

api.add_resource(Developer,'/dev/<int:id>/')
api.add_resource(Welcome,'/')
api.add_resource(Developers_list, '/dev/')
api.add_resource(Skills,'/skills/')
api.add_resource(Skills_mod,'/skills/<int:id>/')

if __name__ == "__main__":
    app.run(debug=True)