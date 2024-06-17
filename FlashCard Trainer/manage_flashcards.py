from flask import Blueprint, render_template, request, redirect, url_for, flash
import json

flashcard_blueprint = Blueprint('flashcards', __name__)

@flashcard_blueprint.route('/create_flashcard', methods=['GET', 'POST'])
def create_flashcard():
    if request.method == 'POST':
        flashcard_question = request.form['question']
        flashcard_answer = request.form['answer']
        if flashcard_question and flashcard_answer:
            deck = request.form['deck']
            question = request.form['question']
            answer = request.form['answer']
        
            flashcard = {
                'deck': deck,
                'question': question,
                'answer': answer
            }
        
            try:
                with open('flashcards.json', 'r') as file:
                    flashcards = json.load(file)
            except FileNotFoundError:
                flashcards = []
    
            flashcards.append(flashcard)
    
            with open('flashcards.json', 'w') as file:
                json.dump(flashcards, file, indent=4)
    
            return redirect(url_for('flashcards.create_flashcard'))
        else:
            flash('Please provide a question and answer')
            return redirect(request.url)
    else:
        try:
            with open('decks.json', 'r') as file:
                decks = [deck['name'] for deck in json.load(file)]
        except (FileNotFoundError, json.JSONDecodeError):
            decks = ["Deck 1", "Deck 2", "Deck 3"]
       
        return render_template('create_flashcard.html', decks=decks)
    
@flashcard_blueprint.route('/show_flashcards', methods=['GET', 'POST'])
def show_flashcards():
    try:
        with open('flashcards.json', 'r') as file:
            flashcards = json.load(file)
    except FileNotFoundError:
        flashcards = []

    return render_template('show_flashcards.html', flashcards=flashcards)

@flashcard_blueprint.route('/delete_flashcard', methods=['POST'])
def delete_flashcard():
    if 'deck' in request.form and 'question' in request.form:
        deck = request.form['deck']
        question = request.form['question']

        try:
            with open('flashcards.json', 'r') as file:
                flashcards = json.load(file)
        except FileNotFoundError:
            flashcards = []

        index_to_delete = None
        for i, flashcard in enumerate(flashcards):
            if flashcard['deck'] == deck and flashcard['question'] == question:
                index_to_delete = i
                break

        if index_to_delete is not None:
            del flashcards[index_to_delete]

            with open('flashcards.json', 'w') as file:
                json.dump(flashcards, file, indent=4)

    return redirect(url_for('flashcards.show_flashcards'))
