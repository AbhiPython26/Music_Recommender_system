import pickle
import pandas as pd
import streamlit as st
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
from scipy.sparse import load_npz

# Spotify API credentials
CLIENT_ID = "70a9fb89662f4dac8d07321b259eaad7"
CLIENT_SECRET = "4d6710460d764fbbb8d8753dc094d131"

# Initialize the Spotify client
client_credentials_manager = SpotifyClientCredentials(client_id=CLIENT_ID, client_secret=CLIENT_SECRET)
sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)

# Load the large dataset with title and artist_name columns
@st.cache_data
def load_large_dataset():
    # Limit columns to only the ones you need to speed up load time
    return pd.read_csv("data/song_data.csv", usecols=["title", "artist_name"])

# Load the precomputed similarity matrix (ensure it's in a fast, optimized format like sparse matrix)
@st.cache_data
def load_similarity_matrix():
    # Loading the similarity matrix in sparse format for efficiency
    return load_npz('similarity_sparse_matrix.npz')

# Function to get album cover from Spotify
def get_song_album_cover_url(song_name, artist_name):
    search_query = f"track:{song_name} artist:{artist_name}"
    results = sp.search(q=search_query, type="track")

    if results and results["tracks"]["items"]:
        track = results["tracks"]["items"][0]
        album_cover_url = track["album"]["images"][0]["url"]
        return album_cover_url
    else:
        return "https://i.postimg.cc/0QNxYz4V/social.png"  # Default image in case no album is found

# Function to recommend similar songs
def recommend(song, similarity_matrix, large_dataset):
    # Get the song's index
    index = large_dataset[large_dataset['title'] == song].index[0]
    
    # Calculate similarity based on the preloaded sparse matrix
    distances = similarity_matrix[index].toarray().flatten()  # Convert sparse row to dense array
    
    # Sort based on similarity values (excluding the song itself)
    sorted_indices = distances.argsort()[-6:-1][::-1]  # Top 5 recommendations
    
    recommended_music_names = []
    recommended_music_posters = []
    
    for idx in sorted_indices:
        artist = large_dataset.iloc[idx].artist_name
        recommended_music_posters.append(get_song_album_cover_url(large_dataset.iloc[idx].title, artist))
        recommended_music_names.append(large_dataset.iloc[idx].title)
    
    return recommended_music_names, recommended_music_posters

# Add background CSS
background_image_url = "static/mountain.jpg"  # Local static file

st.markdown(
    f"""
    <style>
    .stApp {{
        background-image: url("{background_image_url}");
        background-size: cover;
        background-position: center;
        background-repeat: no-repeat;
        background-attachment: fixed;
        color: white;
    }}
    div[data-testid="stSidebar"] {{
        background-color: rgba(0, 0, 0, 0.6);
    }}
    </style>
    """,
    unsafe_allow_html=True
)

st.header('🎵 Music Recommender System')

# Load the pre-calculated similarity matrix and music dataset for recommendations
large_dataset = load_large_dataset()
similarity_matrix = load_similarity_matrix()

# Do not display the dataset to the user
# Instead, show a song selection dropdown
music_list = large_dataset['title'].values  # List of song titles for dropdown

# Allow the user to select a song from the dropdown
selected_song = st.selectbox(
    "Select a song from the list:",
    music_list
)

if st.button('Show Recommendation'):
    # Get recommendations using the selected song
    recommended_music_names, recommended_music_posters = recommend(selected_song, similarity_matrix, large_dataset)
    
    # Display the recommended songs and their album covers in a grid layout
    col1, col2, col3, col4, col5 = st.columns(5)
    
    with col1:
        st.text(recommended_music_names[0])
        st.image(recommended_music_posters[0])
    
    with col2:
        st.text(recommended_music_names[1])
        st.image(recommended_music_posters[1])
    
    with col3:
        st.text(recommended_music_names[2])
        st.image(recommended_music_posters[2])
    
    with col4:
        st.text(recommended_music_names[3])
        st.image(recommended_music_posters[3])
    
    with col5:
        st.text(recommended_music_names[4])
        st.image(recommended_music_posters[4])
