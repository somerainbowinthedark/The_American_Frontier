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
    

if __name__ == '__main__':
    app.run(host='localhost', port=2469)