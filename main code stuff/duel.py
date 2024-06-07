import random
from flask import Flask, redirect, request 

game = Flask(__name__)
@game.route('/duel', methods=['GET', 'POST'])
def duel_numero_uno():
    answers = ['left', 'right', 'center']

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
    return ''

@game.route('/mierda', methods=['GET', 'POST'])
def tie():
    return ''

@game.route('/ganar', methods=['GET', 'POST'])
def win():
    return ''