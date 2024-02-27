from flask import Flask, render_template

app = Flask(__name__)

# Маршрут для главной страницы
@app.route('/')
def index():
    return render_template('mainPage.html')

if __name__ == '__main__':
    app.run(debug=True)
