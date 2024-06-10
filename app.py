from flask import Flask, request, render_template
import pandas as pd

app = Flask(__name__)

# Load the movies dataset
movies = pd.read_csv('ml-latest-small/movies.csv')

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/recommend', methods=['GET'])
def recommend():

    movie_titles = request.args.get('movie_titles').split(',')
    num_recommendations = int(request.args.get('num_recommendations', 10))

    movie_titles = [title.strip() for title in movie_titles]

    input_movies = movies[movies['title'].isin(movie_titles)]
    genres = input_movies['genres'].str.split('|').explode().unique()

    recommended_movies = movies[movies['genres'].str.contains('|'.join(genres))]
    recommended_movies = recommended_movies.sample(n=num_recommendations)

    return render_template('index.html', recommendations=recommended_movies[['title', 'genres']].to_dict(orient='records'))

if __name__ == '__main__':
    app.run(debug=True)
