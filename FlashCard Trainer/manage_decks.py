from flask import Blueprint, render_template, request, redirect, url_for, flash
import json

deck_blueprint = Blueprint('decks', __name__,)