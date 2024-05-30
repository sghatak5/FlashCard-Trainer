from flask import Blueprint, render_template, request, redirect, url_for
import json
from datetime import datetime, timedelta

start_learning_blueprint = Blueprint('start_learning', __name__)