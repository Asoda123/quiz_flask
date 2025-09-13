from http.client import responses
from locale import currency

from flask import Flask
from flask import url_for, redirect
from flask import render_template, request





api = 'https://api.privatbank.ua/p24api/pubinfo?exchange&coursid=5'

capitals = ['paris',"berlin",'tokyo','washington','rome']


app = Flask(__name__)

@app.route('/quiz', methods=['GET','POST'])
def quiz_site():
    if request.method == 'GET':
        return render_template('quiz.html')
    else:
        score = 0
        france = request.form['france'].lower()
        germany = request.form['germany'].lower()
        japan = request.form['japan'].lower()
        usa = request.form['usa'].lower()
        italy = request.form['italy'].lower()
        user_list = [france,germany,japan,usa,italy]

        for number, city in enumerate(capitals):
            if user_list[number] == city:
                score+=1
        else:
            return (f'Your score is {str(score)}/5!')


if __name__ == '__main__':
    app.run(debug=True, port = 8000)

