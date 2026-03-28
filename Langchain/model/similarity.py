from langchain_openai import OpenAIEmbeddings
from sklearn.metrics.pairwise import cosine_similarity
from dotenv import load_dotenv

load_dotenv()

embeddings = OpenAIEmbeddings(model="text-embedding-3-small", dimensions=32)


docs=["Apple is fruit","Apple is a company","Banana is a fruit"]

query="Apple fruit"

doc_embeddings = embeddings.embed_documents(docs)
query_embedding = embeddings.embed_query(query)

similarities = cosine_similarity([query_embedding], doc_embeddings)

print(similarities)