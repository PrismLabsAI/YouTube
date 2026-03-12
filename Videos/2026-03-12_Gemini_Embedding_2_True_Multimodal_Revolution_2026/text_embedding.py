#!/usr/bin/env python3
"""
Example script to generate text embeddings using Google Gemini Embedding 2 via Vertex AI.
"""
import os
from google.cloud import aiplatform
from vertexai.vision_models import MultiModalEmbeddingModel

# Initialize Vertex AI
def init_vertex_ai():
    project_id = os.environ.get('GOOGLE_CLOUD_PROJECT')
    if not project_id:
        raise ValueError("GOOGLE_CLOUD_PROJECT environment variable must be set.")
    aiplatform.init(project=project_id, location='us-central1')

# Function to get text embeddings
def get_text_embedding(text):
    """Generate embedding for the given text."""
    try:
        model = MultiModalEmbeddingModel.from_pretrained("multimodalembedding@001")
        embeddings = model.get_embeddings(text=text)
        return embeddings[0].text_embedding  # Returns a list of floats (1408 dimensions)
    except Exception as e:
        print(f"Error generating embedding: {e}")
        return None

if __name__ == "__main__":
    init_vertex_ai()
    sample_text = "This is a sample text for embedding."
    embedding = get_text_embedding(sample_text)
    if embedding:
        print(f"Text: {sample_text}")
        print(f"Embedding (first 10 values): {embedding[:10]}")
        print(f"Embedding dimension: {len(embedding)}")
    else:
        print("Failed to generate embedding.")