from flask import Blueprint, render_template, request, redirect, url_for
import json

flashcard_blueprint = Blueprint('flashcards', __name__)

@flashcard_blueprint.route('/create_flashcard', methods=['GET', 'POST'])

def create_flashcard():
    if request.method == 'POST':
        # Get form data
        deck = request.form['deck']
        question = request.form['question']
        answer = request.form['answer']
       
        # Create dictionary for the flashcard
        flashcard = {
            'deck': deck,
            'question': question,
            'answer': answer
        }
       
        # Load existing flashcards from JSON file if available
        try:
            with open('flashcards.json', 'r') as file:
                flashcards = json.load(file)
        except FileNotFoundError:
            flashcards = []
 
        # Append new flashcard to list
        flashcards.append(flashcard)
 
        # Write updated flashcards to JSON file
        with open('flashcards.json', 'w') as file:
            json.dump(flashcards, file, indent=4)
 
        # Redirect back to create_flashcard route
        return redirect(url_for('flashcards.create_flashcard'))
    else:
        # Load list of decks from decks.json
        try:
            with open('decks.json', 'r') as file:
                decks = [deck['name'] for deck in json.load(file)]
        except (FileNotFoundError, json.JSONDecodeError):
            # If file not found or cannot be decoded, provide default value
            decks = ["Deck 1", "Deck 2", "Deck 3"]
       
        # Render the template with the form and list of decks
        return render_template('create_flashcard.html', decks=decks)