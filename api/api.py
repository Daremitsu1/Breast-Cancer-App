# Import Dependencies
from flask import Flask, request
import numpy as np
import pickle
import pandas as pd
from flasgger import Swagger, swag_from

app = Flask(__name__)
Swagger(app)

pickle_in = open("model/model.pkl", "rb")
model = pickle.load(pickle_in)
scaler = pickle.load(open("model/scaler.pkl", "rb"))

@app.route('/')
def welcome():
    return "Welcome All"

@app.route('/predict', methods=["GET"])
def predict_cancer_diagnosis():
    """
    Predicts the diagnosis of breast cancer.
    This is using docstrings for specifications.
    ---
    parameters:
      - name: radius_mean
        in: query
        type: number
        required: true
      - name: texture_mean
        in: query
        type: number
        required: true
      - name: perimeter_mean
        in: query
        type: number
        required: true
      - name: area_mean
        in: query
        type: number
        required: true
      - name: smoothness_mean
        in: query
        type: number
        required: true
      - name: compactness_mean
        in: query
        type: number
        required: true
      - name: concavity_mean
        in: query
        type: number
        required: true
      - name: concave_points_mean
        in: query
        type: number
        required: true
      - name: symmetry_mean
        in: query
        type: number
        required: true
      - name: fractal_dimension_mean
        in: query
        type: number
        required: true
      - name: radius_se
        in: query
        type: number
        required: true
      - name: texture_se
        in: query
        type: number
        required: true
      - name: perimeter_se
        in: query
        type: number
        required: true
      - name: area_se
        in: query
        type: number
        required: true
      - name: smoothness_se
        in: query
        type: number
        required: true
      - name: compactness_se
        in: query
        type: number
        required: true
      - name: concavity_se
        in: query
        type: number
        required: true
      - name: concave_points_se
        in: query
        type: number
        required: true
      - name: symmetry_se
        in: query
        type: number
        required: true
      - name: fractal_dimension_se
        in: query
        type: number
        required: true
      - name: radius_worst
        in: query
        type: number
        required: true
      - name: texture_worst
        in: query
        type: number
        required: true
      - name: perimeter_worst
        in: query
        type: number
        required: true
      - name: area_worst
        in: query
        type: number
        required: true
      - name: smoothness_worst
        in: query
        type: number
        required: true
      - name: compactness_worst
        in: query
        type: number
        required: true
      - name: concavity_worst
        in: query
        type: number
        required: true
      - name: concave_points_worst
        in: query
        type: number
        required: true
      - name: symmetry_worst
        in: query
        type: number
        required: true
      - name: fractal_dimension_worst
        in: query
        type: number
        required: true 
    responses:
        200:
            description: The diagnosis prediction
    """
    radius_mean = float(request.args.get("radius_mean"))
    texture_mean = float(request.args.get("texture_mean"))
    perimeter_mean = float(request.args.get("perimeter_mean"))
    area_mean = float(request.args.get("area_mean"))
    smoothness_mean = float(request.args.get("smoothness_mean"))
    compactness_mean = float(request.args.get("compactness_mean"))
    concavity_mean = float(request.args.get("concavity_mean"))
    concave_points_mean = float(request.args.get("concave_points_mean"))
    symmetry_mean = float(request.args.get("symmetry_mean"))
    fractal_dimension_mean = float(request.args.get("fractal_dimension_mean"))
    radius_se = float(request.args.get("radius_se"))
    texture_se = float(request.args.get("texture_se"))
    perimeter_se = float(request.args.get("perimeter_se"))
    area_se = float(request.args.get("area_se"))
    smoothness_se = float(request.args.get("smoothness_se"))
    compactness_se = float(request.args.get("compactness_se"))
    concavity_se = float(request.args.get("concavity_se"))
    concave_points_se = float(request.args.get("concave_points_se"))
    symmetry_se = float(request.args.get("symmetry_se"))
    fractal_dimension_se = float(request.args.get("fractal_dimension_se"))
    radius_worst = float(request.args.get("radius_worst"))
    texture_worst = float(request.args.get("texture_worst"))
    perimeter_worst = float(request.args.get("perimeter_worst"))
    area_worst = float(request.args.get("area_worst"))
    smoothness_worst = float(request.args.get("smoothness_worst"))
    compactness_worst = float(request.args.get("compactness_worst"))
    concavity_worst = float(request.args.get("concavity_worst"))
    concave_points_worst = float(request.args.get("concave_points_worst"))
    symmetry_worst = float(request.args.get("symmetry_worst"))
    fractal_dimension_worst = float(request.args.get("fractal_dimension_worst"))

    input_array = np.array([[radius_mean, texture_mean, perimeter_mean, area_mean, smoothness_mean, compactness_mean,
                            concavity_mean, concave_points_mean, symmetry_mean, fractal_dimension_mean,
                            radius_se, texture_se, perimeter_se, area_se, smoothness_se, compactness_se,
                            concavity_se, concave_points_se, symmetry_se, fractal_dimension_se,
                            radius_worst, texture_worst, perimeter_worst, area_worst, smoothness_worst,
                            compactness_worst, concavity_worst, concave_points_worst, symmetry_worst,
                            fractal_dimension_worst]])
    # Modify as per your feature requirements
  
    input_array_scaled = scaler.transform(input_array)
  
    prediction = model.predict(input_array_scaled)
  
    if prediction[0] == 0:
        diagnosis = "Benign"
    else:
        diagnosis = "Malicious"
  
    return diagnosis

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000)