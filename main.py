from translate import detect_language
from flask import Flask, request, render_template

app = Flask(__name__)

@app.route('/')
def form():
    return render_template('index.html')

@app.route('/', methods=['POST'])
def form_post():
    text = request.form['text']
    output = detect_language(text)
    return render_template('index.html', text=output)

@app.route('/health')
def health():
    return "Application is running"