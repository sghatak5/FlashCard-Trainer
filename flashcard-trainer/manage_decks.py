from flask import Blueprint, render_template, request, redirect, url_for, flash
import json

deck_blueprint = Blueprint('decks', __name__,)
 
@deck_blueprint.route('/create_deck', methods=['GET', 'POST'])
def create_deck():
    """
    Handle the creation of a new deck.

    GET: Render the form to create a new deck.
    POST: Process the form data to create a new deck and save it to the JSON file.

    Returns:
        str: The rendered HTML of the create deck form or a redirection to the manage decks page.
    """
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
            return redirect(request.url)
    else:
        return render_template('create_deck.html')
    
@deck_blueprint.route('/show_decks')
def show_decks():
    """
    Display all existing decks.

    Returns:
        str: The rendered HTML of the show decks page with the list of decks.
    """
    with open('decks.json', 'r') as file:
        decks = json.load(file)
    return render_template('show_decks.html', decks=decks)
 
@deck_blueprint.route('/delete_deck', methods=['POST'])
def delete_deck():
    """
    Handle the deletion of a deck.

    POST: Process the form data to delete the specified deck from the JSON file.

    Returns:
        str: A redirection to the show decks page.
    """
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
