from flask import Flask, render_template
from manage_decks import deck_blueprint
from manage_flashcards import flashcard_blueprint
from start_learning import start_learning_blueprint

app = Flask(__name__)

app.register_blueprint(deck_blueprint, url_prefix='/decks')
app.register_blueprint(flashcard_blueprint, url_prefix='/flashcards')
app.register_blueprint(start_learning_blueprint, url_prefix='/start_learning')

@app.route('/')
def index():
    """
    Render the index (home) page.

    Returns:
        str: The rendered HTML of the index page.
    """
    return render_template('index.html')

@app.route('/manage_decks')
def manage_decks():
    """
    Render the manage decks page.

    Returns:
        str: The rendered HTML of the manage decks page.
    """
    return render_template('manage_decks.html')

@app.route('/manage_flashcards')
def manage_flashcards():
    """
    Render the manage flashcards page.

    Returns:
        str: The rendered HTML of the manage flashcards page.
    """
    return render_template('manage_flashcards.html')

@app.route('/start_learning')
def start_learning():
    """
    Render the start learning page.

    Returns:
        str: The rendered HTML of the start learning page.
    """
    return render_template('start_learning.html')

if __name__ == '__main__':
    app.run(debug=True)