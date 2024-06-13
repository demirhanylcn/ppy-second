from flask import Flask, render_template, request
from pymongo import MongoClient
from spellchecker import SpellChecker

app = Flask(__name__)
spell = SpellChecker()

client = MongoClient("mongodb+srv://demirhanylcn:Avatar123!@spell.vtcjugz.mongodb.net/")
db = client['spell']
collection = db['spelldatabase']

@app.route('/')
def index():
    return render_template('index.html')


def spellcheck_text(text):
    words = text.split()
    corrected_text = ""
    corrected_count = 0
    for word in words:
        corrected_word = spell.correction(word)
        if corrected_word != word:
            corrected_count += 1
        corrected_text += corrected_word + " "
    return corrected_text.strip(), corrected_count

if __name__ == '__main__':
    app.run(debug=True)
