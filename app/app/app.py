import os
import json
from flask import Flask, redirect, url_for, request, make_response
import time
from flask import render_template
from loguru import logger
import logging
import sys
import db_functions
import task
import requests 
from dto import *

app = Flask(__name__)

@app.route('/app/app',methods=['POST'])
def get_form_settings():
    response = {}
    if request.method == 'POST':
        content = request.get_json()
        abc = content["aaa"]
        abc = content["aad"]
        response["abc"] = abc
    return json.dumps(response,indent=True,ensure_ascii=False)

 
@app.route('/app/api/healthcheck', methods=['GET'])
@app.route('/api/healthcheck', methods=['GET'])
def healthcheck():
    response = {}
    try:    
        result,message = db_functions.health_check()
        if result:
            return json.dumps({'result': str(result)}), 200, {'ContentType': 'application/json'}
        else:
            return json.dumps({'result': 'False'}), 501, {'ContentType': 'application/json'}
    except Exception as e:
        logger.exception("healthcheck error")
        return json.dumps({'result': 'False'}), 502, {'ContentType': 'application/json'}


if __name__ == "__main__":
    app.run(debug=False,host='0.0.0.0', port=5000)
