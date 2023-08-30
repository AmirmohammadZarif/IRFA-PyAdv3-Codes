from flask import Flask, request
from flask_sqlalchemy import SQLAlchemy
import jwt


app = Flask(__name__)

secretKey = "FIRA"

users = {
    "amir" : "abcd",
    "parsa": "28329",
    "sara": "7234",
}   

permissions = {
    'amir' : "admin",
    'parsa' : "writer",
    'sara' : "editor"
}


@app.route('/login', methods=['POST'])
def login():
    auth = request.authorization
 
    if not auth or not auth.username or not auth.password:
        return "username and password are required"

    if users.get(auth.username) is None:
        return "user not found"

    if users.get(auth.username) != auth.password:
        return "incorrect password"

    token = jwt.encode({"username": auth.username, 
                        "permissions" : permissions[auth.username]}, secretKey)

    # decoded = jwt.decode(token, secretKey, algorithms=["HS256"])

    return token

# @app.route('/signup', methods=['POST'])
# def signup():


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8284)