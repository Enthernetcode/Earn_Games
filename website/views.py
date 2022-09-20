from flask import Blueprint, render_template, request, flash, jsonify
from flask_login import login_required, current_user
from .models import Dashboard
from . import db
import json

views = Blueprint('views', __name__)
                                                                
@views.route('/home', methods=['GET', 'POST'])
@login_required
def home():
   return render_template('home.html', user=current_user, balance=00)


@views.route('/dashboard')
@login_required
def dashboard():
   return render_template('dashboard.html', user=current_user, dashboard=current_user)


@views.route('/dashboard/withdrawal' or '/withdrawal')
@login_required
def withdrawal():
   return render_template('withdrawal.html', user=current_user)


@views.route('/score')
@login_required
def score_history():
   return render_template('score.html', user=current_user)

@views.route('/games')
@login_required
def games_list():
   return render_template('games.html', user=current_user)

@views.route('/games1')
@login_required
def game_list():
 return render_template('games1.html', user=current_user)

@views.route('/games2')
@login_required
def gamex_list():
 return render_template('games2.html', user=current_user)

@views.route('/')
@login_required
def test_page():
  return '<h1>To be deleted after site creation</h1><br><b><p>/home</p><br><p>/dashboard</p><br><p>/dashboard/withdrawal</p><br><p>/score</p><br><p>/games</p><br><p>/login</p><br><p>/sign_up</p><br><p>/about</p><br><p>/customer_care</p><br><p>/newsupdate</p><br><p>/user</p><br><p>/admin</p><br><p>/password_recovery</p><br><p>/</p></b>'

@views.route('/admin')
@login_required
def admin():
 id = user=current_user.id
 if id == 2 or 4:
  return render_template('admin.html', user=current_user)
 else:
  flash ('you are not an admin, you can never access this page', category='error')
  return render_template('home.html', user=current_user)


#class RequestPasswordResetEmail(GenericApiView):
# serializer_class = RewuestPasswordEmailRequestSerializer
# def post(self, request):
#  serializer = self.serializer_class(data = request.data)
#  email = request.data['email']
#  if Customuser.object.filter(email = email).exist():
#   user = Custom.object.get(email = email)
#   uidb64 = urlsafe_base64_encoded(smart_byte(user.id))
#   token = PasswordResetTokenGenerator().make_token(user)
#   current_site = get_current_site(request).domain
#   relativeLink = reverse('account:reset-token', kwargs = ['uidb64':uidb64, 'token':token])
#   absurl = f'http://{current_site}{relativelink}'
#   email_body = 'Hello \n 


@views.route('/funding')
@login_required
def wallet_funding():
 return render_template('fund.html', user=current_user)

@views.route('/verify')
@login_required
def verification():
 return render_template('verify.html', user=current_user)
