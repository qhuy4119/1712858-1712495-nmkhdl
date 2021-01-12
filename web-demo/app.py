from flask import Flask, request, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def get_prediction():
    #TODO: load model -> predict -> render html template with prediction result
    result = 'placeholder result'
    return render_template('resultPage.html', result=result)
