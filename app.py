from flask import *
import re

app = Flask("app")

items = [
    {
        "item": "задачки с кэтса",
        "cost": "примерно миллион",
        "picture": "static\images\MKN_Hub_title.png"
    },
    {
        "item": "задачки с информатикса",
        "cost": "примерно два миллиона",
        "picture": "static\images\MKN_Hub_title.png"
    },
    {
        "item": "задачки по линалу",
        "cost": "примерно три миллиона",
        "picture": "static\images\MKN_Hub_title.png"
    }, 
    {
        "item": "задачки по матану",
        "cost": "бесценно....",
        "picture": "static\images\MKN_Hub_title.png"
    }, 
    {
        "item": "задачки с кэтса",
        "cost": "примерно миллион",
        "picture": "static\images\MKN_Hub_title.png"
    },
    {
        "item": "задачки с информатикса",
        "cost": "примерно два миллиона",
        "picture": "static\images\MKN_Hub_title.png"
    },
    {
        "item": "задачки по линалу",
        "cost": "примерно три миллиона",
        "picture": "static\images\MKN_Hub_title.png"
    }, 
    {
        "item": "задачки по матану",
        "cost": "бесценно....",
        "picture": "static\images\MKN_Hub_title.png"
    }, 
    {
        "item": "задачки с кэтса",
        "cost": "примерно миллион",
        "picture": "static\images\MKN_Hub_title.png"
    },
    {
        "item": "задачки с информатикса",
        "cost": "примерно два миллиона",
        "picture": "static\images\MKN_Hub_title.png"
    },
    {
        "item": "задачки по линалу",
        "cost": "примерно три миллиона",
        "picture": "static\images\MKN_Hub_title.png"
    }, 
    {
        "item": "задачки по матану",
        "cost": "бесценно....",
        "picture": "static\images\MKN_Hub_title.png"
    }, 
    {
        "item": "задачки с кэтса",
        "cost": "примерно миллион",
        "picture": "static\images\MKN_Hub_title.png"
    },
    {
        "item": "задачки с информатикса",
        "cost": "примерно два миллиона",
        "picture": "static\images\MKN_Hub_title.png"
    },
    {
        "item": "задачки по линалу",
        "cost": "примерно три миллиона",
        "picture": "static\images\MKN_Hub_title.png"
    }, 
    {
        "item": "задачки по матану",
        "cost": "бесценно....",
        "picture": "static\images\MKN_Hub_title.png"
    }
]


@app.route("/")
def index():
    return render_template("index.html", items=items)


@app.route("/buy_product")
def buy_product():
    return render_template("buy_product.html")


@app.post("/buy_product")
def process_info():
    number = request.form["card_number"]
    date = request.form["date"]
    name = request.form["name"]
    code = request.form["code"]

    if not number.isdigit() or len(number) != 16:
        return redirect("/buy_product")

    for i in name:
        if re.search(r"[a-zA-Z\s]", i) == None:
            return redirect("/buy_product")

    if len(name.split(" ")) != 2:
        return redirect("/buy_product")

    if not code.isdigit() or len(code) != 3:
        return redirect("/buy_product")

    print(f"{number}, {date}, {name}, {code}")
    return redirect("/payment_recived")


@app.route("/payment_recived")
def scam():
    return render_template("scam.html")

