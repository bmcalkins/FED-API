from flask import Flask 
from flask_restful import Api, Resource
from fredapi import Fred

app = Flask(__name__)
api = Api(app)
fred = Fred(api_key='6cd659eeb72f5cda524e78dbb3e4d577')

@app.route('/')
def index():
    return "Hello World"
    
if __name__ == "__main__":
    app.run(debug=True)


