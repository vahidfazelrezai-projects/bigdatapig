from flask import Flask, url_for, redirect
app = Flask(__name__)

@app.route('/')
def home():
    return redirect(url_for('static', filename='index.html'))

if __name__ == '__main__':
    app.run()