# 1. korak - import klase Flask iz modula flask
from flask import Flask, render_template
import random

from services.datetime_services.datetime_manager import get_current_datetime
from services.web_api_services.web_api_manager import get_users


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


@app.route('/users')
def users():
    users_list = get_users()
    for user in users_list:
        user['user_avatar'] = f'https://robohash.org/{random.randint(1, 10)}.png?size=100x100'
    return render_template('user.html', users=users_list)


@app.route('/currentdate')
def current_date():
    current_date_var = get_current_datetime()
    return render_template('current_date.html', current_date_var=current_date_var)






if __name__ == '__main__':
    # 3. korak - pokrenuti Flask aplikaciju
    app.run(debug=True)
