from flask import Blueprint, render_template, request, redirect, url_for, flash
import json

deck_blueprint = Blueprint('decks', __name__,)
@deck_blueprint.route('/create_deck', methods=['GET', 'POST'])
def create_deck():
    if request.method == 'POST':
        deck_name = request.form['deck_name']
        if deck_name:
            # Load existing decks from JSON file
            with open('decks.json', 'r') as file:
                decks = json.load(file)
                if not isinstance(decks, list):
                    decks = []
            # Append the new deck to the list of decks
            decks.append({'name': deck_name})
            # Write the updated list of decks back to the JSON file
            with open('decks.json', 'w') as file:
                json.dump(decks, file, indent=4)
            # Flash a success message
            #flash(f'Deck "{deck_name}" created successfully!', 'success')
            # Redirect to the Manage Decks page
            #return redirect(url_for('decks.show_decks'))
            return redirect(url_for('manage_decks'))
        else:
            flash('Please provide a name for the deck.', 'error')
            return redirect(request.url)  # Redirect back to the same page if deck_name is not provided
    else:
        return render_template('create_deck.html')