from flask import Blueprint, render_template, request, redirect, url_for
import json
from datetime import datetime, timedelta

start_learning_blueprint = Blueprint('start_learning', __name__)

@start_learning_blueprint.route('/')
def show_decks_for_learning():
    with open('decks.json', 'r') as file:
        decks = json.load(file)
    return render_template('start_learning.html', decks=decks)

@start_learning_blueprint.route('/<deck_name>', methods=['GET', 'POST'])
def learn(deck_name):
    with open('flashcards.json', 'r') as file:
        flashcards = [fc for fc in json.load(file) if fc['deck'] == deck_name]

    if not flashcards:
        return render_template('message.html', message='No flashcards available in this deck.', back_url=url_for('start_learning.show_decks_for_learning'))

    if request.method == 'POST':
        try:
            with open('learning_history.json', 'r') as file:
                learning_history = json.load(file)
        except FileNotFoundError:
            learning_history = []

        card_id = int(request.form['card_id'])
        known = request.form['known'] == 'true'
        timestamp = datetime.now().isoformat()

        learning_history.append({
            'deck_name': deck_name,
            'card_id': card_id,
            'timestamp': timestamp,
            'known': known
        })

        with open('learning_history.json', 'w') as file:
            json.dump(learning_history, file, indent=4)

    try:
        with open('learning_history.json', 'r') as file:
            learning_history = json.load(file)
    except FileNotFoundError:
        learning_history = []

    to_learn = filter_flashcards(flashcards, learning_history, deck_name)

    if not to_learn:
        return render_template('message.html', message='No flashcards to review at this time.', back_url=url_for('start_learning.show_decks_for_learning'))

    return render_template('learn.html', flashcard=to_learn[0], deck_name=deck_name, show_answer=False)

@start_learning_blueprint.route('/<deck_name>/reveal', methods=['POST'])
def reveal_answer(deck_name):
    card_id = int(request.form['card_id'])
    with open('flashcards.json', 'r') as file:
        flashcards = [fc for fc in json.load(file) if fc['deck'] == deck_name]
    flashcard = flashcards[card_id]
    return render_template('learn.html', flashcard={'id': card_id, 'flashcard': flashcard}, deck_name=deck_name, show_answer=True)

def filter_flashcards(flashcards, learning_history, deck_name):
    today = datetime.now()
    to_learn = []

    for i, flashcard in enumerate(flashcards):
        card_history = [h for h in learning_history if h['deck_name'] == deck_name and h['card_id'] == i]

        if not card_history:
            to_learn.append({'id': i, 'flashcard': flashcard})
            continue

        last_attempt = max(card_history, key=lambda x: x['timestamp'])
        last_date = datetime.fromisoformat(last_attempt['timestamp'])

        if last_attempt['known']:
            delta = timedelta(days=2)
        else:
            delta = timedelta(hours=1)

        if today >= last_date + delta:
            to_learn.append({'id': i, 'flashcard': flashcard})

    return to_learn
