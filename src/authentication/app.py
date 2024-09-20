from flask import Flask, redirect, url_for, session
from flask_dance.contrib.google import make_google_blueprint, google
from auth_controller import AuthController
import os
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)
app.secret_key = os.getenv('APP_KEY')

# Google OAuth configuration
google_bp = make_google_blueprint(
    client_id=os.getenv('GOOGLE_CLIENT_ID'),
    client_secret=os.getenv('GOOGLE_KEY'),
    scope=['profile', 'email'],
    redirect_url='/login/google/authorized'
)
app.register_blueprint(google_bp, url_prefix='/login')

@app.route('/login/google')
def login_google():
    if not google.authorized:
        return redirect(url_for('google.login'))
    resp = google.get('/oauth2/v2/userinfo')
    assert resp.ok, resp.text
    user_info = resp.json()
    return AuthController.process_google_login(user_info)

# ... existing routes ...

if __name__ == '__main__':
    app.run(debug=True)