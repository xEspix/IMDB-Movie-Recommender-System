import streamlit as st
import pickle

def app():
    st.title('Movie Recommender System')
    movies=pickle.load(open('E:\\ML PROJECTS\\my_streamlit_app\\movies_list.pkl','rb'))
    similarity_matrix=pickle.load(open('E:\\ML PROJECTS\\my_streamlit_app\\similarity_matrix.pkl','rb'))


    def recommend(movie):
        idx=movies[movies['Title']==movie].index[0]
        distance=sorted(list(enumerate(similarity_matrix[idx])), reverse=True, key=lambda x: x[1])
        movie_names=[]
        movie_posters = []
        for i in distance[0:7]:
            movie_names.append(movies.iloc[i[0]].Title)
            movie_posters.append(movies.iloc[i[0]].Poster)
        return movie_names, movie_posters

    movie_list=movies['Title'].values

    selected_movie=st.selectbox(
    "Type or select the movie",
    movie_list
    )

    if st.button('Results'):
        recommended_movie_names, recommended_movie_posters = recommend(selected_movie)
        col1, col2, col3 = st.columns(3)
        with col1:
            
            st.image(recommended_movie_posters[0])
            st.text(recommended_movie_names[0])
        with col2:
            
            st.image(recommended_movie_posters[1])
            st.text(recommended_movie_names[1])
        with col3:
            st.image(recommended_movie_posters[2])
            st.text(recommended_movie_names[2])
        col4, col5, col6 =st.columns(3)
        with col4:
            st.image(recommended_movie_posters[3])
            st.text(recommended_movie_names[3])
        with col5:
            st.image(recommended_movie_posters[4])
            st.text(recommended_movie_names[4])
        with col6:
            st.image(recommended_movie_posters[5])
            st.text(recommended_movie_names[5])

