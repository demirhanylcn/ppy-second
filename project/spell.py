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

@app.route('/check_spell', methods=['POST'])
def check_spell():
    if 'file' not in request.files:
        return "No file part"

    file = request.files['file']

    if file.filename == '':
        return "No selected file"

    if file:
        text = file.read().decode('utf-8')
        corrected_text, corrected_count = spellcheck_text(text)
        collection.insert_one({"corrected_word_count": corrected_count})
        return render_template('result.html', original_text=text, corrected_text=corrected_text)

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
