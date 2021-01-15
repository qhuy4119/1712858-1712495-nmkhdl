from flask import Flask, request, render_template
from . import predict
import numpy as np

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def get_prediction():
    #TODO: load model -> predict -> render html template with prediction result
    result, probability_vector = predict.predictLabel(request.form['content'])
    probability_vector = np.round(probability_vector, 2)*100
    highestProbability = probability_vector.max()
    return render_template('resultPage.html', result=result, highestProbability=highestProbability, requestContent=request.form['content'])
