from flask import Blueprint, render_template, request, flash, jsonify
from flask_login import login_required, current_user
from .models import Dashboard
from . import db
import json

views = Blueprint('views', __name__)
                                                                
@views.route('/home', methods=['GET', 'POST'])
@login_required
def home():
   return render_template('home.html', user=current_user)


@views.route('/dashboard')
@login_required
def dashboard():
   return '<p>This is the dashboard</p>'


@views.route('/dashboard/withdrawal' or '/withdrawal')
@login_required
def withdrawal():
   return '<p>This is The withdrawal page</p>'


@views.route('/score')
@login_required
def score_history():
   return '<p>Check your score history here</p>'

@views.route('/games')
@login_required
def games_list():
   return '<h1>pick a game to start playing</h1>'

@views.route('/')
@login_required
def test_page():
  return '<h1>To be deleted after site creation</h1><br><b><p>/home</p><br><p>/dashboard</p><br><p>/dashboard/withdrawal</p><br><p>/score</p><br><p>/games</p><br><p>/login</p><br><p>/sign_up</p><br><p>/about</p><br><p>/customer_care</p><br><p>/newsupdate</p><br><p>/user</p><br><p>/admin</p><br><p>/password_recovery</p><br><p>/</p></b>'

@views.route('/admin')
@login_required
def admin():
 return '<h2> this is 5he admin Page </h2>'


@views.route('/password_recovery')
@login_required
def recoverpass():
 return '<h2> Recover your password here </h2>'
