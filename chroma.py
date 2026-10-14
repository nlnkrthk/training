import chromadb

client = chromadb.Client()

collection = client.create_collection(
    name="my_docs"
)



print("doc created")