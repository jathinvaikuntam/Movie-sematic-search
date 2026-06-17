from search_engine import query_movies

query = "underdog sports story"

results = query_movies(query)

titles = results["metadatas"][0]
plots = results["documents"][0]
distances = results["distances"][0]

sorted_data = sorted(zip(titles, plots, distances), key=lambda x: x[2], reverse=True)

for title, plot, distance in sorted_data:

    print(title["title"])
    print(plot)
    print(f"Similarity: {round((1 - distance) * 100, 2)}%") 

    print("-" * 50)