from flask import Flask
app = Flask(__name__)
@app.route("/")
def homepage():
    return "welocme to the global world"

@app.route("/aboutus")
def aboutus():
    companyname = "giftedbrush llc"
    phone = "4049931269"
    return companyname + ' , ' + phone 


@app.route("/total")
def total():
    a = 40
    b = 30
    c = 40 + 30
    return "this the addition of the two numbers:" + str(c)

@app.route("/product")
def product():
    a = 40
    b = 30
    c = 40 * 30
    return "this the product of the two numbers:" + str(c)

@app.route("/sub")
def sub():
    a = 40
    b = 30
    c = 40 - 30
    if c < 11:
        return "the value is less than 11:" + str(c)
    else:
        return "the value is greater than 11:" + str(c)
     
    


if __name__ == '__main__':
   app.run(host='127.0.0.1', port=5000, debug =True)