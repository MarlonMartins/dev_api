from flask import Flask, jsonify, request
import json

app = Flask(__name__)


developers = [
	{'id':'0','name':'Elliot','skills':['Python','Hacking']},
	{'id':'1','name':'Darlene','skills':['Pentest','Hacking']}
]

@app.route('/')
def welcome():
	return "Welcome to my First API!"

@app.route('/dev/<int:id>/',methods=['GET','PUT','DELETE'])
def developer(id):
	if request.method =='GET':
		try:
			response = developers[id]
		except IndexError:
			message = 'Developer with ID {} does not exist.'.format(id)
			response = {'status':'Error','message':message}
		except Exception:
			message = 'Unknown Error. Search for the API developer.'
			response = {'status':'Error','message':message}
		return jsonify(response)

	elif request.method == 'PUT':
		data = json.loads(request.data)
		developers[id] = data
		return jsonify(data)

	elif request.method == 'DELETE':
		try:
			response = developers.pop(id)
		except IndexError:
			message = 'Developer with ID {} does not exist.'.format(id)
			response = {'status':'Error','message':message}
		except Exception:
			message = 'Unknown Error. Search for the API developer.'
			response = {'status':'Error','message':message}
		
		return jsonify({'status':'success','message':'deleted record'})

@app.route('/dev/',methods=['POST','GET'])
def list_developers():
	if request.method == 'POST':
		data = json.loads(request.data)
		position = len(developers)
		data['id']= position
		developers.append(data)
		return jsonify({'status':'success','message':'inserted record'})

	elif request.method =="GET":
		return jsonify(developers)

if __name__ == '__main__':
	app.run(debug=True)

