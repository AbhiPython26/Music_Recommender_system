# Music Recommender System

Welcome to the **Music Recommender System** project! This system helps users discover new songs based on their music preferences. It uses a combination of **Collaborative Filtering** and **Cosine Similarity** to recommend songs that are similar to the one the user selects. The app is built using **Python**, **Streamlit**, and **Spotify API** for dynamic song metadata. This system is designed to offer a personalized music experience, making it easy for users to find new music that suits their taste.

## Features
- **Song Selection**: Users can choose any song from a list of available songs.
- **Song Recommendations**: After selecting a song, the system provides the top 5 similar songs based on **Cosine Similarity**.
- **Album Covers**: Fetches album covers dynamically using **Spotify API**.
- **Interactive Interface**: Built using **Streamlit**, providing an easy-to-use web interface.
- **Real-time Data**: Always up-to-date song details from Spotify API.

## Technologies Used
- **Python**: For the core programming of the recommender system.
- **Streamlit**: For creating the interactive web app.
- **Spotify API**: To fetch real-time song information such as album art and track details.
- **Scikit-learn**: For implementing **Cosine Similarity** to compute song similarity.
- **Pandas**: For data manipulation and processing.
- **SciPy**: For handling sparse matrices efficiently.
- **Numpy**: For numerical operations related to cosine similarity calculations.

## Getting Started

### Prerequisites
To run the **Music Recommender System** on your machine, make sure you have **Python 3.7+** installed. You'll also need an active **Spotify Developer account** to get the API credentials.

### Installation
1. Clone or download the repository.
2. Install the required libraries:
   ```bash
   pip install -r requirements.txt
Set up Spotify API credentials:
Go to Spotify Developer Dashboard and create a new app to get your CLIENT_ID and CLIENT_SECRET.
Replace the placeholders in the code with your actual credentials:
python
Copy code
CLIENT_ID = "your_spotify_client_id"
CLIENT_SECRET = "your_spotify_client_secret"
How It Works
Data Preprocessing:

The dataset with song details (like title, artist_name, year) is loaded.
The numeric features (like year) are selected to compute similarity.
Cosine Similarity:

The Cosine Similarity between songs is calculated using the numeric features (e.g., year).
The resulting similarity matrix contains similarity scores between all pairs of songs.
Song Recommendations:

The user selects a song from a dropdown list.
The system finds the song's index in the dataset and calculates similarity scores for all songs.
The top 5 most similar songs are returned as recommendations.
Spotify API Integration:

The app uses Spotify API to fetch dynamic album covers for the recommended songs.
Streamlit Interface:

The app presents the results in an easy-to-use interface where the user can select a song and see recommendations along with album covers.
File Structure
php
Copy code
Music-Recommender-System/

### Explanation of Files:

- **app.py**: This is the main file that runs the **Streamlit** app. It interacts with the user, loads the song dataset, and displays song recommendations based on the selected song.
  
- **song_data.csv**: This file contains metadata about the songs, such as the title, artist name, and year of release.

- **similarity_sparse_matrix.npz**: This is a precomputed sparse matrix containing cosine similarity values between songs. It is used to recommend similar songs.

- **requirements.txt**: This file lists the Python dependencies required to run the application. It ensures that anyone who clones the repository can easily set up the environment.


 <h2 style="color: #FF6347; font-size: 30px; font-weight: bold;">Thank you for visiting!  🎶🎵</h2> ```


