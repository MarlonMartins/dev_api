from flask import Flask, request
from flask_restful import Resource
import json

skills_list = ['Python','Java','PHP','C++','R']

class Skills(Resource):
    def get(self):
        return skills_list

    def post(self):
        try:
            data = json.loads(request.data)
            skills_list.append(data)
        except Exception:
            return 'Unknown Error. Search for the API developer.'
            
        return {'status':'success','message':'inserted record'}
    
class Skills_mod(Resource):
    def put(self,id):
        data = json.loads(request.data)
        skills_list[id] = data
        return {'status':'success','message':'inserted record'}

    def delete(self,id):
        try:
            response = skills_list.pop(id)
        except IndexError:
            message = 'Developer with ID {} does not exist.'.format(id)
            response = {'status':'Error','message':message}
        except Exception:
            message = 'Unknown Error. Search for the API developer.'
            response = {'status':'Error','message':message}
        return {'status':'success','message':'deleted record'}
