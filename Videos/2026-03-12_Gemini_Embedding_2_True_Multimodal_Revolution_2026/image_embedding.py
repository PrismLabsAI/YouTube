#!/usr/bin/env python3
"""
Example script to generate image embeddings using Google Gemini Embedding 2 via Vertex AI.
"""
import os
from google.cloud import aiplatform
from vertexai.vision_models import MultiModalEmbeddingModel
from PIL import Image
import io

# Initialize Vertex AI
def init_vertex_ai():
    project_id = os.environ.get('GOOGLE_CLOUD_PROJECT')
    if not project_id:
        raise ValueError("GOOGLE_CLOUD_PROJECT environment variable must be set.")
    aiplatform.init(project=project_id, location='us-central1')

# Function to get image embeddings
def get_image_embedding(image_path):
    """Generate embedding for the given image."""
    try:
        if not os.path.exists(image_path):
            print(f"Error: {image_path} not found. Please provide a valid image file or download one.")
            return None
        model = MultiModalEmbeddingModel.from_pretrained("multimodalembedding@001")
        image = Image.open(image_path)
        embeddings = model.get_embeddings(image=image)
        return embeddings[0].image_embedding  # Returns a list of floats (1408 dimensions)
    except Exception as e:
        print(f"Error generating embedding: {e}")
        return None

if __name__ == "__main__":
    init_vertex_ai()
    image_path = "sample_image.jpg"  # Ensure this file exists
    embedding = get_image_embedding(image_path)
    if embedding:
        print(f"Image: {image_path}")
        print(f"Embedding (first 10 values): {embedding[:10]}")
        print(f"Embedding dimension: {len(embedding)}")
    else:
        print("Failed to generate embedding.")