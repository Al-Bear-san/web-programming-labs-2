from flask import Blueprint, Flask, redirect, url_for, render_template, request
lab4 = Flask(__name__)
lab4 = Blueprint('lab4', __name__)



@lab4.route('/lab4/')
def lab():
    return render_template('lab4.html')

@lab4.route('/lab4/login', methods = ['GET', 'POST'])
def login():
    if request.method == 'GET':
        return render_template('login.html')
    UserName = request.form.get('UserName')
    password = request.form.get('password')
    if UserName == 'sanya' and password == '12345':
        return render_template('success.html')
    
    error = 'Наверные логин и/или пороль'
    return render_template('login.html', error=error)

@lab4.route('/lab4/fridge', methods = ['GET', 'POST'])
def fridge():
    if request.method == 'GET':
        return render_template('fridge.html')
    temp = request.form.get('temp')
    temp_meseg = ''

    if temp == '':
        temp_meseg = 'Нет данных'
        return render_template('fridge.html', temp_meseg=temp_meseg, temp=temp) 
    elif float(temp) < -12:
        temp_meseg = 'Не удалось установить температуру — слишком низкое значение'
        return render_template('fridge.html', temp_meseg=temp_meseg)
    elif -12 <= float(temp) <= -9:
        temp_meseg = 'Установлена температура: ' + temp +'°С' + ' ***'
        return render_template('fridge.html', temp_meseg=temp_meseg)
    elif -8 <= float(temp) <= -5:
        temp_meseg = 'Установлена температура: ' + temp +'°С' + ' **'
        return render_template('fridge.html', temp_meseg=temp_meseg)
    elif -4 <= float(temp) <= -1:
        temp_meseg = 'Установлена температура: ' + temp +'°С' + ' *'
        return render_template('fridge.html', temp_meseg=temp_meseg)
    elif float(temp) > -1:
        temp_meseg = 'Не удалось установить температуру — слишком высокое значение'
        return render_template('fridge.html', temp_meseg=temp_meseg)


# Цены на зерно
prices = {'ячмень': 12000, 'овёс': 8500, 'пшеница': 8700, 'рожь': 14000}

@lab4.route('/lab4/seed')
def seed():
    return render_template('seed.html')

@lab4.route('/lab4/grain_order', methods = ['GET', 'POST'])
def grain_order():
    grain_type = request.form.get('grain_type')
    weight = request.form.get('weight')

    # Проверка наличия значения веса
    if not weight:
        return "Ошибка: не введён вес. <a href='/lab4/grain_order'>Вернуться</a>"

    weight = float(weight)

    # Проверка корректности значения веса
    if weight <= 0:
        return "Ошибка: неверное значение веса. <a href='/lab4/grain_order'>Вернуться</a>"

    # Проверка наличия зерна в наличии
    if weight > 500:
      return "Ошибка: такого объёма сейчас нет в наличии. <a href='/lab4/grain_order'>Вернуться</a>"

    # Рассчет суммы заказа
    total_cost = prices[grain_type] * weight

    # Применение скидки, если заказ более 50 тонн
    if weight > 50:
        total_cost *= 0.9
        discount_message = "Применена скидка за большой объём."

    else:
        discount_message = ""

    return render_template('grain_order.html', grain_type=grain_type, weight=weight, total_cost=total_cost, discount_message=discount_message)

if __name__ == '__main__':
    lab4.run(debug=True)

@lab4.route('/lab4/cookies', methods = ['GET', 'POST'])
def cookies():
    if request.method == 'GET':
        return render_template('cookies.html')

    color = request.form.get('color')
    headers = {
        'Set-Cookie': 'color=' + color + '; path=/',
        'Location': '/lab4/cookies'
    }
    return '', 303, headers