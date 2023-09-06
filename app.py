from flask import Flask
app = Flask(__name__)

@app.route("/")
def start():
    return """
<!doctype html>
<html>
    <head>
        <title>Сыпченко Александр Евгеньевич, Лабораторная 1</title>
    </head>
    <body>
        <header>
            НГТУ, ФБ, Лабораторная работа 1
        </header>

        <h1>web-cthdth yf flask</h1>

        <footer>
            &copy; Александр Сыпченко, ФБИ-14, 3 курс, 2023
        </footer>
    </body>
</html>
"""
