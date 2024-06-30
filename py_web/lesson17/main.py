from sqlite3 import connect

from flask import Flask, render_template, request

from hh_json import parce
from crud import add_row

app = Flask(__name__)


@app.get('/index')
@app.get('/')
def index():
    """
    Стартовая страница
    """
    return render_template('index.html')


@app.route('/form/')
def form():
    """
    Форма для поиска
    """
    return render_template('form.html')


@app.post('/result/')
def result():
    """
    Вычисление проекта и вывод страницы результатов
    :return: шаблон с результатами
    """
    vac = request.form
    data = parce(**vac)
    dat = {**data, **vac}
    print(dat)
    dat['where'] = 'в названии вакансии' \
        if dat['where'] == 'name' else 'в названии компании' if dat['where'] == 'company' else 'везде'
    add_row(dat)
    return render_template('about.html', res=dat)

