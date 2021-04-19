from flask import Flask, jsonify, make_response

import os
import time
import json
import requests
import json,sys,yaml
from Utilities.Services.Utils.utils import  list as filter
from Utilities.Services.Utils.utils import  convert_to_table_data as to_table_data
from Utilities.Services.Utils.utils import  convert_to_yaml as to_yaml_data
from Utilities.Services.Errors.errors import  custom_error as error
    
app = Flask(__name__)
URL = 'https://cat-fact.herokuapp.com/'

# get all the facts about cat.
@app.route('/facts', methods=['GET'])
def facts():
    data = requests.get(URL+'facts')
    return jsonify(data.json())

# Get facts about cat for specific user.
@app.route('/facts/<name>', methods=['GET'])
def get_facts_name(name):
    data = requests.get(URL+'facts/%s'% name)
    first_name = data.json()['user']['name']['first']
    print('first name %s'% first_name)
    if first_name[0].lower() in filter() :
        return data.json()
    else:
        return error("Cat %s not found !!"% name, '404')

# This method is not supported by cat-facts on rest api, or may be i couldnt find.
@app.route('/facts/<name>', methods=['PUT'])
def put_fact_name(name):
    data = requests.put(URL+'facts/%s'% name, data ={'key':'value'})

# This method is not supported by cat-facts on rest api, or may be i couldnt find.
@app.route('/facts/<name>', methods=['DELETE'])
def delete_fact_name(name):
    data = requests.delete(URL+'facts/%s'% name, data ={'key':'value'})


if __name__ == '__main__':
    app.run(host="0.0.0.0", port="5000", debug=True, use_reloader=False)