#import statements
import streamlit as st
import pickle
import pandas as pd

#opening the pickle
movies_dict = pickle.load(open('movie_dict.pkl','rb'))
movies = pd.DataFrame(movies_dict)

similarity = pickle.load(open('similarity.pkl','rb'))

#creating the title and select box for the website
st.title('Movie Recommender System')
selected_movie_name=st.selectbox('Which movie would you like to be watch?',movies['title'].values)


#using recommend function to return 5 movies when a user clicks the recommend button
def recommend(movie):
    movie_index = movies[movies['title'] == movie].index[0]
    distances = similarity[movie_index]
    movies_list = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[1:6]

    recommended_movies=[]
    for i in movies_list:
        recommended_movies.append(movies.iloc[i[0]].title)
    return recommended_movies

#creating a recommend button
if st.button('Recommend'):
    recommendations=recommend(selected_movie_name)
    for i in recommendations:
        st.write(i)


