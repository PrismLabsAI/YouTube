#!/usr/bin/env python3
"""
Example script demonstrating cross-modal search: Compute similarity between text and image embeddings.
"""
import os
import numpy as np
from google.cloud import aiplatform
from vertexai.vision_models import MultiModalEmbeddingModel
from PIL import Image

# Initialize Vertex AI
def init_vertex_ai():
    project_id = os.environ.get('GOOGLE_CLOUD_PROJECT')
    if not project_id:
        raise ValueError("GOOGLE_CLOUD_PROJECT environment variable must be set.")
    aiplatform.init(project=project_id, location='us-central1')

# Function to get text embedding
def get_text_embedding(text):
    try:
        model = MultiModalEmbeddingModel.from_pretrained("multimodalembedding@001")
        embeddings = model.get_embeddings(text=text)
        return np.array(embeddings[0].text_embedding)
    except Exception as e:
        print(f"Error generating text embedding: {e}")
        return None

# Function to get image embedding
def get_image_embedding(image_path):
    try:
        if not os.path.exists(image_path):
            print(f"Error: {image_path} not found.")
            return None
        model = MultiModalEmbeddingModel.from_pretrained("multimodalembedding@001")
        image = Image.open(image_path)
        embeddings = model.get_embeddings(image=image)
        return np.array(embeddings[0].image_embedding)
    except Exception as e:
        print(f"Error generating image embedding: {e}")
        return None

# Function to compute cosine similarity
def cosine_similarity(vec1, vec2):
    dot_product = np.dot(vec1, vec2)
    norm1 = np.linalg.norm(vec1)
    norm2 = np.linalg.norm(vec2)
    return dot_product / (norm1 * norm2)

if __name__ == "__main__":
    init_vertex_ai()
    sample_text = "A beautiful sunset over the ocean."
    image_path = "sample_image.jpg"
    
    text_emb = get_text_embedding(sample_text)
    image_emb = get_image_embedding(image_path)
    
    if text_emb is not None and image_emb is not None:
        similarity = cosine_similarity(text_emb, image_emb)
        print(f"Text: {sample_text}")
        print(f"Image: {image_path}")
        print(f"Cosine Similarity: {similarity:.4f}")
    else:
        print("Failed to generate embeddings.")