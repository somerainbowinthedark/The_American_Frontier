from flask import Flask, render_template

app = Flask(__name__)

IMG_DIR = './static'

@app.route('/welcome')
def title_screen():
    return render_template('placeholder.html')

@app.route('/characters')


if __name__ == '__main__':
    app.run(host='localhost', port=2469)