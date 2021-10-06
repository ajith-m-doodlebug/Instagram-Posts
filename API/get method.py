from flask import Flask
from flask import jsonify

app = Flask(__name__)

movies = [{'name': 'The Godfather', 'imdb': '9.2/10'},
          {'name': 'The Prestige', 'imdb': '8.5/10'},
          {'name': 'The Dark Knight', 'imdb': '9/10'},
          {'name': 'Dunkirk', 'imdb': '7.8/10'}]

@app.route('/getImdb/<name>', methods=['GET'])
def getImdb(name):
    for index, value in enumerate(movies):
        if value['name'] == name:
            theMovie = movies[index]
    return jsonify(theMovie)


if __name__ == '__main__':
    app.run()
