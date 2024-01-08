from flask import Blueprint, redirect, url_for, render_template, request, session, abort
<<<<<<< HEAD
=======

>>>>>>> 1663294acd1edade7083f8e87f7d10cf51663658
lab7 = Blueprint("lab7",__name__)

@lab7.route("/lab7/")
def main():
    return render_template('lab7/index.html')

@lab7.route("/lab7/drink")
def drink():
    return render_template('lab7/drink.html')

@lab7.route("/lab7/api", methods = ['POST'])
def api():
    data = request.json

    if data['method'] == 'get-price':
        return get_price(data['params'])
<<<<<<< HEAD
=======
    
>>>>>>> 1663294acd1edade7083f8e87f7d10cf51663658
    if data['method'] == 'pay':
        return pay(data['params'])
    
    abort(400)

def get_price(params):
    return {"result": calculate_price(params), "error": None}

def calculate_price(params):
    drink = params['drink']
    milk = params['milk']
    sugar = params['sugar']

<<<<<<< HEAD
=======
    #Напитки
>>>>>>> 1663294acd1edade7083f8e87f7d10cf51663658
    if drink == 'cofee':
        price = 120
    elif drink == 'black-tea':
        price = 80
    else:
        price = 70

<<<<<<< HEAD
=======
    #Допы
>>>>>>> 1663294acd1edade7083f8e87f7d10cf51663658
    if milk:
        price += 30
    if sugar:
        price += 10
<<<<<<< HEAD
=======
    
>>>>>>> 1663294acd1edade7083f8e87f7d10cf51663658
    return price

def pay(params):
    card_num = params['card_num']
    if len(card_num) != 16 or not card_num.isdigit():
        return {"result": None, "error": "Неверный номер карты"}
    
    cvv = params['cvv']
    if len(cvv) != 3 or not cvv.isdigit():
        return {"result": None, "error": "Неверный номер CVV/CVC"}
<<<<<<< HEAD
=======
    
>>>>>>> 1663294acd1edade7083f8e87f7d10cf51663658
    price =  calculate_price(params)
    return {"result": f'С карты {card_num} списано {price} руб', "error": None}