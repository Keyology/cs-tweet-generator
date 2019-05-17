from flask import Flask
from markov import corpus
from markov import second_order
from markov import second_order_sentence
from flask import render_template
app = Flask(__name__)


@app.route('/')
def generate_sentence():
    sentence = second_order_sentence(second_order(corpus))
    return render_template("index.html", sentence=sentence)


if __name__ == '__main__':
    app.run(debug=True)
