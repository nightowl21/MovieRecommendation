# Usage: streamlit run app.py


import pickle
import pandas as pd
import streamlit as st
from streamlit import session_state as session
import tensorflow as tf
import pandas as pd
import pickle

input_userid = int(st.text_input("Enter User Id", 1))


model = tf.keras.models.load_model('./saved_artifacts/model')

movies_data = pd.read_pickle("./saved_artifacts/movies_data")
user_data = pd.read_pickle("./saved_artifacts/user_data")
unwatched_movies = pd.read_pickle("./saved_artifacts/unwatched_movies")

with open("./saved_artifacts/all_user_columns.pkl", 'rb') as f:
    all_user_columns = pickle.load(f)

with open("./saved_artifacts/all_movie_columns.pkl", 'rb') as f:
    all_movie_columns = pickle.load(f)

unwatched_movies = pd.DataFrame(unwatched_movies)
unwatched_movies = unwatched_movies[unwatched_movies.userId==input_userid]
if len(unwatched_movies) == 0:
    st.markdown(f"UserId {input_userid} does not exist in the database.")
else:
    unwatched_movies = unwatched_movies.explode("movieId")

    movies_data = pd.merge(movies_data, unwatched_movies, on="movieId")
    user_data = user_data[user_data.userId==input_userid] 
    user_data = pd.concat([user_data]*movies_data.shape[0], ignore_index=True)

    X = [user_data[all_user_columns], movies_data[all_movie_columns]]
    scores = model.predict(X)

    recommendations = sorted(list(zip(scores.reshape(scores.shape[0]), unwatched_movies["movieId"])), reverse=True)[:5]
    movie_ids = [movie_id for _, movie_id in recommendations]
    pred_scores = [score for score, _ in recommendations]
    print(movie_ids)

    st.markdown(f"Movie Recommendations for User Id {input_userid} are:")

    for i in movie_ids:
        st.markdown("- " + 
                    str(movies_data[movies_data.movieId == i].title.values[0]) +
                    "\t" + "( MovieId: " + str(i) + ")"
                    )