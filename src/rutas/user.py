import os, threading
from ..main import request, jsonify, app
from ..db import db
from ..modelos import User
from flask import Flask, request, jsonify, url_for
from datetime import datetime
import json
from io import StringIO
from ast import literal_eval
import re
#from werkzeug.security import safe_str_cmp, generate_password_hash, check_password_hash
from base64 import b64encode

@app.route('/register', methods=['POST'])
def register_user():
    """
        "POST": registrar un usuario y devolverlo
    """
    body = request.json

    print(body)

    if body is None:
        return jsonify({
            "response": "empty body"
        }), 400

    if (
        "email" not in body or
        "name" not in body or
        "last_name" not in body or
        "username" not in body or
        "password" not in body 
    ):
        return jsonify({
            "response": "Missing properties"
        }), 400
    if(
        body["email"] == "" or
        body["name"] == "" or
        body["last_name"] == "" or
        body["username"] == "" or
        body["password"] == ""
    ):
        return jsonify({
            "response": "empty property values"
        }), 400

    new_user = User.register(
        body["email"],
        body["name"],
        body["last_name"],
        body["username"],
        body["password"],
        
    )
    db.session.add(new_user)
    try:
        db.session.commit()
        return jsonify(new_user.serialize()), 201
    except Exception as error:
        db.session.rollback()
        print(f"{error.args} {type(error)}")
        return jsonify({
            "response": f"{error.args}"
        }), 500
