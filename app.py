from dotenv import load_dotenv
load_dotenv()
from flask import Flask, request
from flask_restful import Api
from flask import render_template
from views import initialize_routes
from flask_cors import CORS
from flask import render_template
import os
from views import initialize_routes
import datetime

import os

import datetime


app = Flask(__name__)
api = Api(app)
cors = CORS(app, 
    resources={r"/api/*": {"origins": '*'}}, 
    supports_credentials=True
)
initialize_routes(api)
@app.route("/" )
def home():
    return render_template(
        'index.html'    
    )
if __name__ == '__main__':
    app.run()
