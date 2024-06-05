import random
from flask import Flask, redirect, request 

game = Flask(__name__)
@game.route('/duel', methods=['GET', 'POST']):
def duel_numero_uno():
    answers = ['left', 'right', 'center']

    if request.method == 'POST':
        selected = request.form['selected']
        
