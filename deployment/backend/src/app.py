from flask import Flask
from flask_cors import CORS

from share.extensions.exception import handler_exception_error
from src.select_information.main import select_information

app = Flask(__name__)
CORS(app)

app.add_url_rule("/selcetInformation", view_func=select_information, methods=["POST"])

app.register_error_handler(Exception, handler_exception_error)