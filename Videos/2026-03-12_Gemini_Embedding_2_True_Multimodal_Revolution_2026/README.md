# Gemini Embedding 2: True Multimodal Revolution 2026

> **[Watch on YouTube](https://youtu.be/MbxVxMG88ZM)**

Published by [Prism Labs AI](https://youtube.com/@prismlabsai)

---

# Gemini Embedding 2 Companion Code

This repository provides real, working code examples demonstrating Google Gemini Embedding 2, the first truly multimodal embedding model. It unifies text, images, video, audio, and documents into a single 1408-dimensional vector space, perfect for RAG, cross-modal search, and enterprise AI applications.

## Files Overview

- `requirements.txt`: Lists the Python dependencies needed to run the examples.
- `setup.py`: A script to install dependencies and verify your Google Cloud setup.
- `text_embedding.py`: Generates embeddings for text inputs using Gemini Embedding 2.
- `image_embedding.py`: Generates embeddings for image inputs.
- `video_embedding.py`: Generates embeddings for video inputs (placeholder, as full API support may vary).
- `audio_embedding.py`: Generates embeddings for audio inputs (placeholder, as full API support may vary).
- `document_embedding.py`: Generates embeddings for document inputs (placeholder, as full API support may vary).
- `multimodal_search.py`: Demonstrates cross-modal search by computing similarity between text and image embeddings.

## Setup Instructions

1. **Google Cloud Project**: Create a Google Cloud project and enable the Vertex AI API.
2. **Authentication**: Set up authentication using a service account key or Application Default Credentials (ADC). Export the project ID as an environment variable:
   ```bash
   export GOOGLE_CLOUD_PROJECT=your-project-id
   ```
   If using a service account, set:
   ```bash
   export GOOGLE_APPLICATION_CREDENTIALS=path/to/service-account-key.json
   ```
3. **Install Dependencies**: Run `pip install -r requirements.txt` or use the `setup.py` script.
4. **Run Examples**: Each script can be run independently. For example, `python text_embedding.py`.

## How to Run

- **Text Embeddings**: Run `python text_embedding.py` to generate and print embeddings for sample text.
- **Image Embeddings**: Run `python image_embedding.py` to generate embeddings for a sample image (ensure you have an image file at `sample_image.jpg`; if not, the script will prompt to download or provide one).
- **Video Embeddings**: Run `python video_embedding.py` (placeholder implementation).
- **Audio Embeddings**: Run `python audio_embedding.py` (placeholder implementation).
- **Document Embeddings**: Run `python document_embedding.py` (placeholder implementation).
- **Multimodal Search**: Run `python multimodal_search.py` to compute cosine similarity between text and image embeddings.

Note: Gemini Embedding 2 is accessed via Vertex AI. Ensure your project has the necessary quotas and permissions. Some modalities like video, audio, and documents may require additional API support or preprocessing.

## Key Features Demonstrated

- Unified vector space for multimodal inputs.
- High performance on benchmarks like MTEB.
- Applications in RAG and cross-modal retrieval.

For more details, watch the video: https://youtu.be/MbxVxMG88ZM

---

## Disclaimer

This code is provided as-is for educational purposes only. **Use at your own risk** — no warranty is provided, express or implied. The authors are not responsible for any damages or issues arising from the use of this code.

## License

MIT License

---

*Made by [Prism Labs AI](https://youtube.com/@prismlabsai)*