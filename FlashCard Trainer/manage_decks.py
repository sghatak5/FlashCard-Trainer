from flask import Blueprint, render_template, request, redirect, url_for, flash
import json

deck = Blueprint('decks', __name__,)
 
@deck.route('/create_deck', methods=['GET', 'POST'])
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
    @deck_blueprint.route('/show_decks')

def show_decks():
    with open('decks.json', 'r') as file:
        decks = json.load(file)
    return render_template('show_decks.html', decks=decks)
 
@deck_blueprint.route('/delete_deck', methods=['POST'])
def delete_deck():
    if request.method == 'POST':
        deck_name = request.form['deck_name']
        print("Deleting deck:", deck_name)
        decks_file = 'decks.json'
        try:
            with open(decks_file, 'r') as file:
                decks = json.load(file)
        except FileNotFoundError:
            decks = []
        decks = [deck for deck in decks if deck['name'].strip().lower() != deck_name.strip().lower()]
        print("Updated decks:", decks)  
        with open(decks_file, 'w') as file:
            json.dump(decks, file, indent=4)
        return redirect(url_for('decks.show_decks'))
    
    