import pandas as pd
from sklearn.metrics.pairwise import cosine_similarity
from scipy.sparse import csr_matrix, save_npz

# Load your dataset (adjust the file path as needed)
data = pd.read_csv("data/song_data.csv")

# Display the column names to verify the data
print(data.columns)

# Select only the numeric columns (assuming 'year' is numeric, replace with relevant numeric columns)
numeric_columns = ['year']  # Add other numeric columns if available
numeric_features = data[numeric_columns]

# Convert the numeric data into a sparse matrix to save memory
sparse_features = csr_matrix(numeric_features)

# Compute the cosine similarity matrix based on sparse data
similarity_matrix_dense = cosine_similarity(sparse_features)

# Convert the dense similarity matrix into a sparse matrix (csr format)
similarity_matrix_sparse = csr_matrix(similarity_matrix_dense)

# Save the sparse similarity matrix
save_npz('similarity_sparse_matrix.npz', similarity_matrix_sparse)

# Display a part of the similarity matrix (dense)
print(similarity_matrix_dense[:5, :5])  # Display the first 5x5 block of the matrix
