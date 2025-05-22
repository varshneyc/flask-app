from flask import Flask, jsonify
from werkzeug.middleware.proxy_fix import ProxyFix
from mangum import Mangum

app = Flask(__name__)
app.wsgi_app = ProxyFix(app.wsgi_app)

@app.route("/")
def hello():
    return jsonify(message="Hello from Flask deployed on Lambda!")

lambda_handler = Mangum(app)
