from flask import Blueprint, redirect, url_for, render_template
lab1 = Blueprint('lab1', __name__)


@lab1.route("/")
@lab1.route("/index")
def start():
    return redirect("/menu", code=302)



@lab1.route("/menu")
def menu():
    return """
        <!doctype html>
        <html>
            <head>
                <title>НГТУ, ФБ, Лабораторные работы</title>
                <link rel="stylesheet" href="static/main.css">
            </head>
            <body>
                <header>
                    НГТУ, ФБ, WEB-программирование, часть 2. Список лабораторных
                </header>

                <ol>
                    <li><a href="http://127.0.0.1:5000/lab1">Первая лабораторная</a></li>
                    <li><a href="http://127.0.0.1:5000/lab2/">Вторая лабораторная</a></li>
                    <li><a href="http://127.0.0.1:5000/lab3/">Третья лабораторная</a></li>
                    <li><a href="http://127.0.0.1:5000/lab4/">Четвёртая лабораторная</a></li>
                    <li><a href="http://127.0.0.1:5000/lab5/">Пятая лабораторная</a></li>
                    <li><a href="http://127.0.0.1:5000/lab6/">Шестая лабораторная</a></li>
                    <li><a href="http://127.0.0.1:5000/lab7/">Седьмая лабораторная</a></li>
                </ol>

                <footer>
                    &copy; Сыпченко Александр Евгеньевич, ФБИ-14, 3 курс, 2023
                </footer>
            </body>
        </html>
    """


@lab1.route("/lab1/")
def lab():
    return """
<!doctype html>
<html>
    <head>
        <title>Сыпченко Александр Евгеньевич, Лабораторная 1</title>
        <link rel="stylesheet" href="static/main.css">
    </head>
    <body>
        <header>
            НГТУ, ФБ, Лабораторная работа 1
        </header>

        <main>
        <p>Flask — фреймворк для создания веб-приложений на языке
        программирования Python, использующий набор инструментов
        Werkzeug, a также шаблонизатор Jinja2. Относится к категории так
        называемых микрофреймворков — минималистичных каркасов
        веб-приложений, сознательно предоставляющих лишь самые базовые возможности</p>
        </main>

        <ol>
            <li><a href="http://127.0.0.1:5000/lab1/oak">/lab/oak - дуб </a>
            <li><a href="http://127.0.0.1:5000/lab1/student">/lab1/student - студент </a>
            <li><a href="http://127.0.0.1:5000/lab1/python">/lab1/python - python</a>
            <li><a href="http://127.0.0.1:5000/lab1/anime">/lab1/anime - аниме</a>
        </lo>
        <footer>
            &copy; Александр Сыпченко, ФБИ-14, 3 курс, 2023
        </footer>
    </body>
</html>
"""


@lab1.route('/lab1/oak')
def oak():
    return '''
    <!doctype html>
    <html>
        <head> 
            <link rel="stylesheet" href="''' + url_for('static', filename='lab1.css') + '''">
        </head>
        <body>
            <h1>Дуб</h1>
            <img src="''' + url_for('static', filename='oak.jpg') + '''">
        </body>
    </html>
    '''


@lab1.route ('/lab1/student')
def student():
    return'''
        <!doctype html>
        <html>
            <head> 
                <link rel="stylesheet" href="''' + url_for('static', filename='lab1.css') + '''">
            </head>
            <body>
                <header>
                    <h1>Сыпченко Александр Евгеньевич</h1>
                </header>
                <main>
                    <img src="''' + url_for('static' , filename='flag.png') + '''" >
                </main>
                <footer>
                </footer> 
            </body>
        </html>
        '''


@lab1.route ('/lab1/python')
def python():
    return'''
        <!doctype html>
        <html>
            <head> 
                <link rel="stylesheet" href="''' + url_for('static', filename='lab1.css') + '''">
            </head>
            <body>
                <header>
                    <div> Python в русском языке встречаются названия питон или пайтон) — высокоуровневый язык программирования общего назначения 
                    с динамической строгой типизацией и автоматическим управлением памятью, ориентированный на повышение производительности 
                    разработчика, читаемости кода и его качества, а также на обеспечение переносимости написанных на нём программ. 
                    Язык является полностью объектно-ориентированным в том плане, что всё является объектами. Необычной особенностью языка 
                    является выделение блоков кода пробельными отступами. Синтаксис ядра языка минималистичен, за счёт чего на практике 
                    редко возникает необходимость обращаться к документации. Сам же язык известен как интерпретируемый и используется в 
                    том числе для написания скриптов. Недостатками языка являются зачастую более низкая скорость работы и более высокое 
                    потребление памяти написанных на нём программ по сравнению с аналогичным кодом, написанным на компилируемых языках, 
                    таких как C или C++.
                    </div>
                    
                </header>
                <main>
                   <img src="''' + url_for('static' , filename='python.png') + '''" >
                </main>
                <footer>
                </footer> 
            </body>
        </html>
        '''


@lab1.route ('/lab1/anime')
def anime():
    return'''
        <!doctype html>
        <html>
            <head> 
                <link rel="stylesheet" href="''' + url_for('static', filename='lab1.css') + '''">
            </head>
            <body>
                <header>
                    <h2>Что такое аниме?</h2>
                    <div> Все мы знаем, что такое анимация, то есть мультфильмы. Однако аниме – это не просто анимация, придуманная в Японии, 
                    это целый мир, который включает в себя огромное количество жанров и стилей. Он тесно переплетается с японской комиксовой культурой 
                    и состоит из миллионов преданных фанатов. 
                    Разобраться в законах этого мира не так-то просто, но мы попробуем.</div>
                    <h2>В начале была манга…</h2>
                    <div> Огромная вселенная аниме появилась именно из манги – японских комиксов. Термин «манга» впервые упоминается 
                    в 1814-м году знаменитым графиком Хокусай Кацусика и означает буквально «странные (или весёлые) картинки, гротески».
                    </div>
                    
                </header>
                <main>
                   <img src="''' + url_for('static' , filename='anime.jpg') + '''" >
                </main>
                <footer>
                </footer> 
            </body>
        </html>
        '''

