from flask import Blueprint, render_template, request, redirect, url_for
import json

flashcard_blueprint = Blueprint('flashcards', __name__)