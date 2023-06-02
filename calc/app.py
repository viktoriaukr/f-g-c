# Put your app in here.
from flask import Flask, request
from operations import add, sub, mult, div

app = Flask(__name__)

@app.route('/add')
def do_add():
    """ Add a and b parameters."""

    a = int(request.args.get('a'))
    b = int(request.args.get('b'))
    res = add(a, b)

    return str(res)
    

@app.route('/sub')
def do_sub():
    """Substract b from a."""
    
    a = int(request.args.get('a'))
    b = int(request.args.get('b'))
    res = sub(a, b)

    return str(res)


@app.route('/mult')
def do_mult():
    """Multiply a and b."""
    
    a = int(request.args.get('a'))
    b = int(request.args.get('b'))
    res = mult(a, b)

    return str(res)

@app.route('/div')
def do_div():
    """Divide a by b."""
    
    a = int(request.args.get('a'))
    b = int(request.args.get('b'))
    res = div(a, b)

    return str(res)

OPER = {
    "add": add,
    "sub": sub,
    "mult": mult,
    "div": div
}

@app.route("/math/<oper>")
def do_math(oper):
    
    a = int(request.args.get('a'))
    b = int(request.args.get('b'))
    res = OPER[oper](a, b)

    return str(res)