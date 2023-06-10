from flask import Flask, request
import json, dbhelpers, apihelpers
import uuid

app = Flask(__name__)

@app.post("/api/client")
def post_client():
    error = apihelpers.check_endpoint_info(request.json, ["username","password","email","image_url"])
    if(error != None):
        return error
    results = dbhelpers.run_procedure("call insert_client(?,?,?,?)", 
                                      [request.json.get('username'), request.json.get('email'), request.json.get('password'), request.json.get('image_url')])
    if(type(results) == list):
        return json.dumps(results, default=str)
    else:
        return "Sorry, something has gone wrong!"
    
@app.post("/api/login")
def post_login():
    error = apihelpers.check_endpoint_info(request.json, ["username","password"])
    if(error != None):
        return error
    token = uuid.uuid4().hex
    results = dbhelpers.run_procedure('call insert_login(?,?,?)', [request.json.get('username'), request.json.get('password'), token])
    if(type(results) == list):
        return json.dumps(results, default=str)
    else:
        return "Sorry, something has gone wrong!"
    
@app.delete("/api/login")
def delete_login():
    error = apihelpers.check_endpoint_info(request.json, ["token"])
    if(error != None):
        return error
    results = dbhelpers.run_procedure('call delete_login(?)', [request.json.get('token')])
    if(type(results) == list and results[0][0] == 1):
        return json.dumps(results, default=str)
    else:
        return "Sorry, something has gone wrong!"

app.run(debug=True)