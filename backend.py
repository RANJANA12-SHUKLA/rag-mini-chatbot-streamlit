# backend.py

from sentence_transformers import SentenceTransformer
from transformers import pipeline
import faiss

# Load embedding model and text generation model
embedder = SentenceTransformer("all-MiniLM-L6-v2")
generator = pipeline("text2text-generation", model="google/flan-t5-small")

# backend.py

from sentence_transformers import SentenceTransformer
from transformers import pipeline
import faiss

# Load models only once
embedder = SentenceTransformer("all-MiniLM-L6-v2")
generator = pipeline("text2text-generation", model="google/flan-t5-small")

def generate_answer(query, document_text):
    # Split doc into chunks
    chunks = document_text.split(". ")
    
    # Embed chunks
    embeddings = embedder.encode(chunks)
    
    # Create FAISS index
    dimension = embeddings[0].shape[0]
    index = faiss.IndexFlatL2(dimension)
    index.add(embeddings)
    
    # Embed query
    query_embedding = embedder.encode([query])
    D, I = index.search(query_embedding, k=1)
    
    # Retrieve best chunk
    context = chunks[I[0][0]]
    
    # Build prompt
    prompt = f"Answer the question based on the context.\n\nContext: {context}\n\nQuestion: {query}\nAnswer:"
    
    # Generate answer
    output = generator(prompt, max_new_tokens=100)
    return output[0]["generated_text"], context
