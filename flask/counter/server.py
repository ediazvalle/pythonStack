import flask from Flask,render_template,session, redirect
app = Flask(__name__)

@app.route('/')
def index():
    if "count" not in session:
        session['count'] = 0
    else:
        session['count'] += 1
    return render_template("index.html")

@app.route('/destroy_session')
def index():
    session.clear()		# clears all keys  
    session.pop('key_name')		# clears a specific key

@app.route('/reset_key')
def key():
    session.clear()		# clears all keys
    session.pop('key_name')		# clears a specific key

