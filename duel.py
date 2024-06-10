from flask import Flask, redirect, request ,render_template
from titles import app
from titles import character_select

game = Flask(__name__)
@game.route('/duel', methods=['GET', 'POST'])
def duel_numero_uno():
    answers = ['left', 'right', 'center']

    if request.method == 'GET':
        return render_template('duels.html', answers = answers)

    if request.method == 'POST':
        selected = request.form['selected']
        if selected == answers[0]:
            return redirect('/morir')
        if selected == answers[1]:
            return redirect('/mierda')
        if selected == answers[2]:
            return redirect('/ganar')
        
@game.route('/morir', methods=['GET', 'POST'])
def lose():
    return 'uh oh'

@game.route('/mierda', methods=['GET', 'POST'])
def tie():
    return 'You both shot each other in the shoulder! Its a draw!'

@game.route('/ganar', methods=['GET', 'POST'])
def win():
    return 'You shot em right in the chest! Congrats!'