from flask import Flask

app = Flask(__name__)


@app.route('/')
def load():
    sp = ['список-ссылок для перехода к следующим страничкам:',
         'http://127.0.0.1:8080/miss',
         'http://127.0.0.1:8080/index',
         'http://127.0.0.1:8080/promotion',
         'http://127.0.0.1:8080/image']
    return '</br>'.join(sp)

@app.route('/miss')
def test():
    return "Миссия поиски Атлантиды"

@app.route('/index')
def index():
    return "Потеряться - не значит пропасть"

@app.route('/promotion')
def promotion():
    s = ['Общество интересуется ей.',
         'Человечеству интересны мифы и легенды.',
         'Мы найдём сокровища Атлантиды.',
         'А также узнаем её секрет.',
         'Присоединяйся!']
    return '</br>'.join(s)

@app.route('/image')
def image_mars():
    return """<!doctype html>
                <html lang="en">
                  <head>
                    <meta charset="utf-8">
                    <title>Атлантида</title>
                  </head>
                  <body>
                    <h1>Таинственный остров-государство</h1>
                    <<img src="https://hi-news.ru/wp-content/uploads/2017/07/Atlantis-750x422.png"
                     alt="здесь должна была быть картинка, но не нашлась">>
                     <p>Вот какой удивительный остров</p>
                  </body>
                </html>"""


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')
