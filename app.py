from flask import Flask, render_template, request, redirect, url_for, session
import csv
import random

app = Flask(__name__)
app.secret_key = 'your_secret_key'

def fetch_words(level):
    words = []
    with open('words.csv', newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        level_words = [row[f'Level {level}'] for row in reader]
        words = random.sample(level_words, 7)  # Choose 7 random words from the level
    return words

def scramble_word(word):
    word_list = list(word)
    random.shuffle(word_list)
    scrambled = ''.join(word_list)
    return scrambled if scrambled != word else scramble_word(word)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        username = request.form['username']
        session['username'] = username
        session['score'] = 0
        session['level'] = 1
        session['words'] = fetch_words(1)
        session['current_word_index'] = 0
        session['level_score'] = 0
        session['user_answers'] = []
        session['scrambled_words'] = []
        return redirect(url_for('level'))
    return render_template('index.html')

@app.route('/level', methods=['GET', 'POST'])
def level():
    level = session.get('level')
    words = session.get('words')
    current_word_index = session.get('current_word_index', 0)
    
    if request.method == 'POST':
        user_answer = request.form['answer'].strip().lower()
        scrambled_word = scramble_word(words[current_word_index])
        session['scrambled_words'].append(scrambled_word)
        session['user_answers'].append(user_answer)
        
        if user_answer == words[current_word_index].strip().lower():
            session['score'] += 1
            session['level_score'] += 1
            session['correct'] = True
        else:
            session['correct'] = False
        session['current_word_index'] += 1
        current_word_index = session['current_word_index']
        
        if current_word_index >= len(words):
            return redirect(url_for('level_complete'))
    
    scrambled_word = scramble_word(words[current_word_index])
    return render_template('level.html', level=level, scrambled_word=scrambled_word)

@app.route('/level_complete', methods=['GET', 'POST'])
def level_complete():
    level = session.get('level')
    level_score = session.get('level_score')
    words = session.get('words')
    scrambled_words = session.get('scrambled_words')
    user_answers = session.get('user_answers')
    
    if request.method == 'POST':
        if 'next' in request.form:
            if level < 3:
                session['level'] += 1
                session['words'] = fetch_words(session['level'])
                session['current_word_index'] = 0
                session['level_score'] = 0
                session['user_answers'] = []
                session['scrambled_words'] = []
                return redirect(url_for('level'))
            else:
                return redirect(url_for('game_over'))
        elif 'quit' in request.form:
            return redirect(url_for('index'))
    
    results = list(zip(scrambled_words, words, user_answers))
    return render_template('level_complete.html', level=level, level_score=level_score, results=results)

@app.route('/game_over')
def game_over():
    username = session.get('username')
    score = session.get('score')
    return render_template('game_over.html', username=username, score=score)

if __name__ == '__main__':
    app.run(debug=True)
