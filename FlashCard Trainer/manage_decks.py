from flask import Blueprint, render_template, request, redirect, url_for, flash
import json

deck_blueprint = Blueprint('decks', __name__,)
 
@deck_blueprint.route('/create_deck', methods=['GET', 'POST'])
def create_deck():
    if request.method == 'POST':
        deck_name = request.form['deck_name']
        if deck_name:
            with open('decks.json', 'r') as file:
                decks = json.load(file)
                if not isinstance(decks, list):
                    decks = []
            decks.append({'name': deck_name})
            with open('decks.json', 'w') as file:
                json.dump(decks, file, indent=4)
            return redirect(url_for('manage_decks'))
        else:
            flash('Please provide a name for the deck.', 'error')
            return redirect(request.url)
    else:
        return render_template('create_deck.html')