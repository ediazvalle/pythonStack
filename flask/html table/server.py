from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    users = [
        {'first_name' : 'Eduardo', 'last_name' : 'Diaz'},
        {'first_name' : 'Bandit', 'last_name' : 'Diaz'},
        {'first_name' : 'Jess', 'last_name' : 'Sosa'},
        {'first_name' : 'Reina', 'last_name' : 'Lopez'}
    ]
    return render_template("index.html",users=users)



if __name__=="__main__":
    app.run(debug=True)