from flask import Blueprint

web = Blueprint("book", __name__)

from app.web import book