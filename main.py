# 1. korak - import klase Flask iz modula flask
from flask import Flask, render_template


# 2. korak - kreirati objekt klase Flask. Uobicajeno je nazvati ga app
app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/about')
def about():
    return render_template('about.html')


@app.route('/contact')
def contact():
    return 'Contact Page is working!'


@app.route('/user/<name>')
def user(name):
    if name:
        message = f'{name.capitalize()}, pozdrav iz User stranice!'
    else:
        message = f'User Page is working!'
    
    return message




if __name__ == '__main__':
    # 3. korak - pokrenuti Flask aplikaciju
    app.run(debug=True)
