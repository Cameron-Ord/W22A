#importing
import json
from flask import Flask,request, make_response, jsonify
import dbhelper, api_helper, dbcreds
import flask_cors

app = Flask(__name__)

@app.get('/api/candy')
#function gets called on api request
def return_all():
   try:
      #calls the function in api_helper to loop through the information sent
         error=api_helper.check_endpoint_info(request.args, []) 
         if(error !=None):
            return make_response(jsonify(error), 400)
         #calls the procedure to return information from the DB
         results = dbhelper.run_proceedure('CALL return_all()', [])
         #returns results from db run_procedure
         if(type(results) == list):
            return make_response(jsonify(results), 200)
         else:
            return make_response(jsonify('something has gone wrong'), 500)

   except TypeError:
      print('Invalid entry, try again')
      
   except: 
      print('something went wrong')
      
@app.post('/api/candy')
#function gets called on api request
def create_candy():
   try:
      #calls the function in api_helper to loop through the information sent
         error=api_helper.check_endpoint_info(request.json, ['name','image_url', 'description']) 
         if(error !=None):
            return make_response(jsonify(error), 400)
         #calls the procedure to insert sent information into the DB
         results = dbhelper.run_proceedure('CALL new_candy(?,?,?)', [request.json.get('name'), request.json.get('image_url'), request.json.get('description')])
         #returns results from db run_procedure
         if(type(results) == list):
            return make_response(jsonify(results), 200)
         else:
            return make_response(jsonify('something has gone wrong'), 500)

   except TypeError:
      print('Invalid entry, try again')
      
   except: 
      print('something went wrong')
      
      
@app.delete('/api/candy')
#function gets called on api request
def delete_candy():
   try:
      #calls the function in api_helper to loop through the information sent
         error=api_helper.check_endpoint_info(request.json, ['id']) 
         if(error !=None):
            return make_response(jsonify(error), 400)
         #calls the procedure to delete information in the DB
         results = dbhelper.run_proceedure('CALL delete_candy(?)', [request.json.get('id')])
         #returns results from db run_procedure
         if(type(results) == list):
            return make_response(jsonify(results), 200)
         else:
            return make_response(jsonify('something has gone wrong'), 500)

   except TypeError:
      print('Invalid entry, try again')
      
   except: 
      print('something went wrong')




#running @app in either production or testing mode based on the variable in dbcreds
if(dbcreds.production_mode == True):
   print()
   print('----Running in Production Mode----')
   print()
   import bjoern #type: ignore
   bjoern.run(app,"0.0.0.0", 5002)
else:
   from flask_cors import CORS
   CORS(app)
   print()
   print('----Running in Testing Mode----')
   print()
   app.run(debug=True)