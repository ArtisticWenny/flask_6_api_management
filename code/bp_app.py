import pandas as pd
import numpy as np 

systolic = 120
diastolic = 80

request_args = request.args

    if request_args and "systolic" in request_args:
        systolic_value = request_args["systolic"]
    else:
        systolic_value = 120

    if request_args and "diastolic" in request_args:
        diastolic_value = request_args["diastolic"]
    else:
        diastolic_value = 70
