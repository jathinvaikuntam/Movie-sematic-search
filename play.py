import chromadb

client = chromadb.Client()

collection = client.create_collection(name="movies")

collection.add(
    documents=[
        "Baahubali is an epic action movie.",
        "RRR is a blockbuster Telugu movie.",
        "Pushpa is a movie about red sandalwood smuggling.",
        "Eega is a fantasy revenge movie.",
        "Salaar is an action thriller movie."
    ],
    ids=["1", "2", "3", "4", "5"]
)

query = input("Enter the movie description to search for: ")

results = collection.query(
    query_texts=[query],
    n_results=3
)

print(f"\nQuery: {query}\n")
print("Top Matches:\n")

for i, doc in enumerate(results["documents"][0], start=1):
    print(f"{i}. {doc}")