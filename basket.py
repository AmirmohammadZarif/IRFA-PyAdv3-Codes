from flask import *
import jwt
import requests

#maiBasket=[{"id":1,"title":"apple","price":10000}
# ,{"id":22,"title":"orange","price":20000}]
f=open("user.py", "r")

token = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VybmFtZSI6ImFsaXJlemEiLCJwZXJtaXNzaW9ucyI6ImFkbWluIn0.JGXRiyNh4DqhYf2il6S1NQe0hwMhDFCpivX5c7t9nz0"


class Basket:
    def __init__(self,user_id : int,products : list,status):
        self.user_id = user_id
        self.products = products
        self.status = status

    def add_product(self,product_id):
        self.products.append(product_id)

    def remove_product(self,product_id):
        self.products.remove(product_id)

    def changeStatus(self,newStatus):
        self.status = newStatus

    def generate_dic(self):
        return {'userId':self.user_id,
        'products':self.products,
        'status':self.status}

basket1 = Basket(user_id=1234,products=[],status="lock")
basket1 = Basket(user_id=1222,products=[],status="lock")


app = Flask(__name__)

@app.route("/returnBasket")
def returmBasket():
    data = jwt.decode(token, "FIRA", algorithms=["HS256"])
    permission = data.get("permissions")

    if(permission == "user"):
        return basket1.generate_dic()
    else:
        return "Error code 403,Not authorized"

@app.route("/add_product")
def addProduct():
    pId = int(request.args.get("product_id"))
    basket1.add_product(pId)
    return basket1.products

@app.route("/remove_product")
def removeProduct():
    pId= int(request.args.get("product_id"))
    basket1.remove_product(pId)
    return basket1.products


@app.route("/updateBasketStatus")
def updateBasketStatus():
    status = request.args.get("status")
    basket1.changeStatus(status)
    return f"satus updated to {status}"


if __name__ == "__main__":
    app.run(host="0.0.0.0",port=8281)
