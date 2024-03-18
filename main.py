# 1. korak - import klase Flask iz modula flask
from flask import Flask, render_template


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


@app.route('/user/<name>')
def user(name):
    return render_template('user.html')




if __name__ == '__main__':
    # 3. korak - pokrenuti Flask aplikaciju
    app.run(debug=True)
