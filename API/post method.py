from flask import Flask
from flask import jsonify
from flask import request

app = Flask(__name__)

movies = [{'name': 'The Godfather', 'imdb': '9.2/10'},
          {'name': 'The Prestige', 'imdb': '8.5/10'},
          {'name': 'The Dark Knight', 'imdb': '9/10'},
          {'name': 'Dunkirk', 'imdb': '7.8/10'}]

@app.route('/postImdb', methods=['POST'])
def postImdb():
    newMovie = request.get_json()
    movies.append(newMovie)
    return jsonify({'movies': movies})


if __name__ == '__main__':
    app.run()
