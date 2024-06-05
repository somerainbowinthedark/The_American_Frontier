from flask import Flask, render_template, request

app = Flask(__name__)

IMG_DIR = './static'

@app.route('/welcome')
def title_screen():
    return render_template('placeholder.html')

@app.route('/characters', methods=['GET', 'POST'])
def character_select():
    cowboys = ["TallDust", "Augustin"]

    if request.method == 'GET':
        return render_template('character.html', cowboys = cowboys)
    
    if request.method == 'POST':
        selected = request.form['selected']
        print ('selected: ' + selected)


if __name__ == '__main__':
    app.run(host='localhost', port=2469)