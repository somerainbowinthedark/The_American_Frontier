from flask import Flask, render_template, request, redirect

app = Flask(__name__)

IMG_DIR = './static'

@app.route('/welcome')
def title_screen():
        return render_template('titlescreen.html')

@app.route('/characters', methods=['GET', 'POST'])
def character_select():
    cowboys = ["TallDust", "Agustin"]

    if request.method == 'GET':
        return render_template('character.html', cowboys = cowboys)
    
    if request.method == 'POST':
        selected = request.form['selected']
        print ('selected: ' + selected)
    if selected == cowboys[0]:
         return redirect('/thievery')
    if selected == cowboys[1]:
         return redirect('/duel')
    

@app.route('/thievery', methods =['GET', 'POST'])
def thieves():
    objects = ['horse', 'wagon', 'money']
    if request.method == 'GET':
         return render_template('thieving.html', objects = objects)
    
    if request.method == 'POST':
         selected = request.form['selected']
         return redirect(get_redirect(objects, selected))
         
def get_redirect(items: [], selected: str) -> str:
     if selected == items[0]:
          return '/woohoo'
     if selected == items[1]:
          return '/ohdamn'
     if selected == items[2]:
          return '/awjeez'
     

@app.route('/duel', methods = ['GET', 'POST'])
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
        
@app.route('/morir')
def lose():
    return 'uh oh'

@app.route('/mierda')
def tie():
    return 'You both shot each other in the shoulder! Its a draw!'

@app.route('/ganar')
def win():
    return 'You shot em right in the chest! Congrats!'
         
@app.route('/woohoo')
def horsie():
     return 'You rode that horse off into the sunset!'

@app.route('/ohdamn')
def owie():
     return 'The owner caught you stealing his wagon!'

@app.route('/awjeez')
def popo():
     return 'The cops caught ya! Yur getting thrown into the slammer >:( '

    
if __name__ == '__main__':
    app.run(host='localhost', port=2469)