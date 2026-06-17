import chromadb
from movies import movies_list as movies


client = chromadb.PersistentClient(path="./chroma_db")

collection = client.get_or_create_collection(name="movies")

def load_movies():
    
    """
    Add movies to ChromaDB only if the collection is empty.
    """
    if collection.count() == 0:
        collection.add(
            documents=[{"plot": movie["plot"]} for movie in movies],
            metadatas=[{"title": movie["title"]} for movie in movies],
            ids=[
                str(i)
                for i in range(len(movies))
            ]
        )

        print(f"{len(movies)} movies added successfully!")
    else:
        print("Movies already exist in the database.")


def query_movies(query, n=5):
    """
    Search for similar movies.
    """

    results = collection.query(
        query_texts=[query],
        n_results=n,
        include=["metadatas", "documents","distances"] 
    )
    

    return results


# Load movies when this file runs
load_movies()