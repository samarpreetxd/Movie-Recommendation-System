# Movie-Recommendation-System
A Flask-based web application that provides movie recommendations based on user-input movie titles and their genres. The system leverages the MovieLens dataset for its recommendations.

# Movie Recommendation System

A Flask-based web application that provides movie recommendations based on user-input movie titles and their genres. The system leverages the MovieLens dataset for its recommendations.

## Features

- Users can input movie titles they like.
- The system recommends movies based on the genres of the input movies.
- Recommendations are provided using the MovieLens dataset.
- Simple web interface for ease of use.

## Dataset

The application uses the [MovieLens dataset (ml-latest-small)](https://files.grouplens.org/datasets/movielens/ml-latest-small.zip).

## Requirements

- Python 3.x
- Flask
- Pandas

## Setup

1. **Clone the repository:**
   ```sh
   git clone https://github.com/yourusername/movierecommendation.git
   cd movierecommendation
   ```

2. **Create a virtual environment and activate it:**
   ```sh
   python3 -m venv venv
   source venv/bin/activate
   ```

3. **Install the required packages:**
   ```sh
   pip install flask pandas
   ```

4. **Download and unzip the dataset:**
   ```sh
   curl -O https://files.grouplens.org/datasets/movielens/ml-latest-small.zip
   unzip ml-latest-small.zip
   ```

5. **Run the Flask application:**
   ```sh
   python app.py
   ```

6. **Open your web browser and navigate to:**
   ```
   http://127.0.0.1:5000
   ```

## Usage

1. Enter the titles of movies you like in the input field (separated by commas).
2. Specify the number of recommendations you want.
3. Click on the "Get Recommendations" button.
4. The system will display a list of recommended movies based on the genres of the input movies.

## File Structure

- `app.py`: Flask application file.
- `templates/index.html`: HTML template for the web interface.
- `ml-latest-small/`: Directory containing the MovieLens dataset.

## Contributing

Contributions are welcome! Please fork the repository and create a pull request with your changes.

## License

This project is licensed under the MIT License. See the `LICENSE` file for details.
```

