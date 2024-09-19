import streamlit as st
import pickle



def app():
    st.title('IMDB MOVIE VIEWER')
    st.header('Top Rated Movies')

    movies=pickle.load(open('E:\\ML PROJECTS\\my_streamlit_app//movies_list.pkl','rb'))
    top_rated_movies=[]
    top_rated_posters=[]
    top_ratings=[]   
    rated_movies=sorted(list(enumerate(movies['Rating'])), reverse=True, key=lambda x: x[1])
    for i in rated_movies[0:51]:
        top_rated_movies.append(movies.iloc[i[0]].Title)
        top_rated_posters.append(movies.iloc[i[0]].Poster)
        top_ratings.append(i[1])

    mult=5
    for i in range(10):
        col1, col2, col3, col4, col5=st.columns(5)
        with col1:
            st.image(top_rated_posters[i*mult+0])
            st.text(top_rated_movies[i*mult+0])
            st.text(f'Rating : {top_ratings[i*mult+0]}')
        
        with col2:
            st.image(top_rated_posters[i*mult+1])
            st.text(top_rated_movies[i*mult+1])
            st.text(f'Rating : {top_ratings[i*mult+1]}')

        with col3:
            st.image(top_rated_posters[i*mult+2])
            st.text(top_rated_movies[i*mult+2])
            st.text(f'Rating : {top_ratings[i*mult+2]}')

        with col4:
            st.image(top_rated_posters[i*mult+3])
            st.text(top_rated_movies[i*mult+3])
            st.text(f'Rating : {top_ratings[i*mult+3]}')

        with col5:
            st.image(top_rated_posters[i*mult+4])
            st.text(top_rated_movies[i*mult+4])
            st.text(f'Rating : {top_ratings[i*mult+4]}')
