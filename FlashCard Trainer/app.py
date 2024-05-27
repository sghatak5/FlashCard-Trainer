from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/manage_decks')
def manage_decks():
    return render_template('manage_decks.html')

@app.route('/manage_flashcards')
def manage_flashcards():
    return render_template('manage_flashcards.html')

@app.route('/start_learning')
def start_learning():
    return render_template('start_learning.html')


if __name__ == '__main__':
    app.run(debug=True)