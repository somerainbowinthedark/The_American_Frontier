from flask import Flask, render_template, request
from titles import app
from titles import character_select

@app.route('/thievery', methods =['GET', 'POST'])
def theives():
    r