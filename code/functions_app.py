from flask import escape
from flask import Flask, jsonify

import functions_framework
import azure.functions as func
import logging


app = Flask(__BloodPressureReading__)

@app.route("/", methods=["GET"])
def logging.info('Blood Pressure'):
    response = {
        logging.info('This Blood Glucose request HTTP triggered function executed successfully')

     bg = req.params.get('bg')

    }
    return jsonify(response)

    return func.HttpResponse(
             "This HTTP triggered function executed successfully. Pass a name in the query string or in the request body for a personalized response.",
             status_code=200
        )
