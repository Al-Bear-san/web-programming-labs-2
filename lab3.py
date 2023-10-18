from flask import Blueprint, url_for, render_template, request
lab3 = Blueprint('lab3', __name__)


@lab3.route('/lab3/')
def lab():
    return render_template('lab3.html')


@lab3.route('/lab3/form1')
def form1():
    errors = {}
    user = request.args.get('user')
    if user == '':
        errors['user'] = 'Заполните поле!'
    
    age = request.args.get('age')
    if age == '':
        errors['age'] = 'Заполните поле!'

    sex = request.args.get('sex')

    return render_template('form1.html', user=user, age=age, sex=sex, errors=errors)


@lab3.route('/lab3/order')
def order():
    return render_template('order.html')


@lab3.route('/lab3/pay')
def pay():
    price = 0
    drink = request.args.get('drink')
    if drink == 'cofee':
        price = 150
    elif drink == 'black-tea':
        price = 80
    else:
        price = 70
    
    if request.args.get('milk') == 'on':
        price += 30
    if request.args.get('sugar') == 'on':
        price += 10
    return render_template('pay.html', price=price)


@lab3.route('/lab3/success')
def success():
    return render_template('success.html')


@lab3.route('/lab3/railway')
def railway():
    return render_template('railway.html')


@lab3.route('/lab3/ticket')
def ticket():
    errors = {}
    name = request.args.get('name')
    if name == '':
        errors['name'] = 'Заполните поле!'
    
    adulthood = request.args.get('adulthood')
    if adulthood == 'adult':
        adulthood = 'Взрослый'
    else:
        adulthood = 'Детский'
    
    shelf = request.args.get('shelf')
    if shelf == 'lower':
        shelf = 'Нижная'
    elif shelf == 'upper':
        shelf = 'Верхная'
    elif shelf == 'upper_side':
        shelf = 'Верхняя боковая'
    else:
        shelf = 'Нижняя боковая'


    luggage = request.args.get('luggage')
    if luggage == 'on':
        luggage = 'Есть'
    else:
        luggage = 'Нет'
    
    age = request.args.get('age')
    if age == '':
        errors['age'] = 'Заполните поле!'

    exit = request.args.get('exit')
    if exit == '':
        errors['exit'] = 'Заполните поле!'
    
    purpose = request.args.get('purpose')
    if purpose == '':
        errors['purpose'] = 'Заполните поле!'
    
    datapo = request.args.get('datapo')
    if datapo == '':
        errors['datapo'] = 'Заполните поле!'
    
    return render_template('ticket.html', name=name, luggage=luggage, age=age, adulthood=adulthood,
                           shelf=shelf, exit=exit, purpose=purpose, datapo=datapo, errors=errors)