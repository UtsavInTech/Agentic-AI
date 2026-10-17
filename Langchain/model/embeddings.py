from langchain.openai import OpenAIEmbeddings
from dotenv import load_dotenv
load_dotenv()

embeddings = OpenAIEmbeddings(model = "text-embedding-3-small", dimensions = 32)

docs = ["Paris is the capital of France.", "The Eiffel Tower is located in Paris.", "The Louvre Museum is also in Paris."]
doc_embeddings = embeddings.embed_documents(docs)
print(doc_embeddings)

query = "Where is the Eiffel Tower located?"
query_embedding = embeddings.embed_query(query)
print(query_embedding)

from sklearn.metrics.pairwise import cosine_similarity
smilarities = cosine_similarity([query_embedding], doc_embeddings)
print(similarities)