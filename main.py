# 1. korak - import klase Flask iz modula flask
from flask import Flask, render_template

from services.datetime_services.datetime_manager import get_current_datetime


# 2. korak - kreirati objekt klase Flask. Uobicajeno je nazvati ga app
app = Flask(__name__)


# 4. korak - kreirati funkcije koje ce se pokretati kao odgovor na web upite GET, POST, DELETE ...
@app.route('/')
def index():
    return render_template('index.html')


@app.route('/about')
def about():
    return render_template('about.html')


@app.route('/contact')
def contact():
    return render_template('contact.html')


@app.route('/user')
def user():
    name_in_python = 'Pero Peric' # moze biti dohvacena iz baze
    return render_template('user.html', name_in_html=name_in_python)


@app.route('/currentdate')
def current_date():
    current_date_var = get_current_datetime()
    return render_template('current_date.html', current_date_var=current_date_var)




if __name__ == '__main__':
    # 3. korak - pokrenuti Flask aplikaciju
    app.run(debug=True)
