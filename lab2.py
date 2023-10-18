from flask import Blueprint, redirect, url_for, render_template
lab2 = Blueprint('lab2', __name__)


@lab2.route('/lab2/example')
def example():
    name, nomb, grup, kurs = 'Сыпченко Александр Евгеньевич', 2, 'ФБИ-14', '3 курс'
    fruits = [
        {'name': 'яблоки', 'price': 100},
        {'name': 'груши', 'price': 120},
        {'name': 'апельсины', 'price': 80},
        {'name': 'мандарины', 'price': 95},
        {'name': 'манго', 'price': 321}
    ]
    books = [
        {'book': 'Самый богатый человек в Вавилоне', 'author': 'Джордж Клейсон','genre': 'Книги о личных финансах', 'number': 120},
        {'book': 'Богатый Папа, бедный Папа', 'author': 'Роберт Кийосаки','genre': 'Книги о личных финансах', 'number': 340},
        {'book': 'Думай и богатей', 'author': 'Наполеон Хилл','genre': 'Книги о личных финансах', 'number': 443},
        {'book': 'Азбука финансовой грамотности', 'author': 'Владимир Авденин','genre': 'Книги о личных финансах', 'number': 332},
        {'book': 'Как составить личный финансовый план и как его реализовать', 'author': 'Владимир Савенок','genre': 'Книги о личных финансах', 'number': 343},
        {'book': 'Думай как миллионер', 'author': 'Т. Харв Экер','genre': 'Книги о личных финансах', 'number': 233},
        {'book': 'Тайный язык денег', 'author': 'Дэвид Крюгер, Джон Дэвид Манн','genre': 'Книги о личных финансах', 'number': 439},
        {'book': 'Правила инвестирования Уоррена Баффетта', 'author': 'Джереми Миллер','genre': 'Книги о личных финансах', 'number': 398},
        {'book': 'Разумный инвестор. Полное руководство по стоимостному инвестированию', 'author': 'Бенджамин Грэм','genre': 'Книги о личных финансах', 'number': 369},
        {'book': 'Пёс по имени Мани', 'author': 'Бодо Шефер','genre': 'Книги о личных финансах', 'number': 85}
    ]
    return render_template('example.html', name=name, nomb=nomb, grup=grup, kurs=kurs, fruits=fruits, books=books)

@lab2.route('/lab2/')
def lab():
    return render_template('lab2.html')

@lab2.route('/lab2/offroad')
def offroad():
    return render_template('offroad.html')