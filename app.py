import streamlit as st
from search_engine import query_movies

st.set_page_config(
    page_title="Tollywood and Bollywood Movie Search",
    page_icon="🎬"
)

st.title("🎬 Tollywood and Bollywood Semantic Movie Search")

st.write(
    "Describe the type of movie you want, and AI will find similar Tollywood and Bollywood movies!"
)

query = st.text_input(
    "What kind of movie are you looking for?"
)

num_results = st.slider(
    "Number of Results",
    min_value=1,
    max_value=10,
    value=5
)

if st.button("Search"):

    if query.strip() == "":
        st.warning("Please enter a movie description.")
    else:

        results = query_movies(
            query,
            n=num_results
        )

        titles = results["metadatas"][0]
        plots = results["documents"][0]
        distances = results["distances"][0]

        # Sort by distance (similarity) in descending order
        sorted_data = sorted(zip(titles, plots, distances), key=lambda x: x[2], reverse=True)
        titles, plots, distances = zip(*sorted_data) if sorted_data else ([], [], [])

        st.subheader("Recommended Movies")

        # Display results as cards in a 1-column grid
        cols = st.columns(1)
        for idx, (title, plot, distance) in enumerate(zip(titles, plots, distances)):
            similarity_percentage = round((1 - distance) * 100, 2)
            col = cols[idx % 1]
            
            with col:
                with st.container(border=True):
                    st.markdown(f"#### 🎥 {title['title']}")
                    st.markdown(f"**Similarity:** {similarity_percentage}%")
                    st.write(plot)