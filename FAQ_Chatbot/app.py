
from flask import Flask, render_template, request, jsonify
import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity

app = Flask(__name__)

faq = pd.read_csv('faq.csv')

questions = faq['Question'].tolist()
answers = faq['Answer'].tolist()

vectorizer = CountVectorizer()
question_vectors = vectorizer.fit_transform(questions)

def get_answer(user_question):

    user_vector = vectorizer.transform([user_question])

    similarity = cosine_similarity(user_vector, question_vectors)

    best_match = similarity.argmax()

    return answers[best_match]

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/chat', methods=['POST'])
def chat():

    user_message = request.json['message']

    response = get_answer(user_message)

    return jsonify({'reply': response})

if __name__ == '__main__':
    app.run(debug=True)