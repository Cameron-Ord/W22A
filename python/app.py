#importing
import json
from flask import Flask,request, make_response, jsonify
import dbhelper, api_helper
app = Flask(__name__)

@app.post('/api/candy')
#function gets called on api request
def return_all():
   try:
      #calls the function in api_helper to loop through the information sent
         error=api_helper.check_endpoint_info(request.json, ['']) 
         if(error !=None):
            return make_response(jsonify(error), 400)
         #calls the procedure to insert sent information into the DB
         results = dbhelper.run_proceedure('CALL return_all(?)', [request.json.get('')])
         #returns results from db run_procedure
         if(type(results) == list):
            return make_response(jsonify(results), 200)
         else:
            return make_response(jsonify('something has gone wrong'), 500)

   except TypeError:
      print('Invalid entry, try again')
      
   except: 
      print('something went wrong')

#running @app
app.run(debug=True)
