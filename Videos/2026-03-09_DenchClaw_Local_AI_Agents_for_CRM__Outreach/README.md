# DenchClaw: Local AI Agents for CRM & Outreach

Published by [Prism Labs AI](https://youtube.com/@prismlabsai)

---

# DenchClaw Companion Examples

This repository provides companion code examples for the DenchClaw video tutorial. These are standalone Python scripts that simulate CRM and outreach agents using local AI models, demonstrating the concepts of local automation without cloud dependencies.

## Files Overview

- `requirements.txt`: Lists the Python packages needed to run the examples.
- `crm_scorer.py`: A script that loads leads from a CSV file and scores them using a local AI model (Hugging Face Transformers).
- `sample_leads.csv`: Sample CSV file with lead data for testing the CRM scorer.
- `outreach_bot.py`: A script that generates personalized outreach emails based on lead data.
- `config.yaml`: Configuration file for agent settings, such as model paths and prompts.

## Setup

1. Ensure you have Python 3.8+ installed.
2. Clone this repository: `git clone https://github.com/your-repo/denchclaw-companion` (replace with actual repo).
3. Create a virtual environment: `python -m venv venv`.
4. Activate it: `source venv/bin/activate` (Linux/Mac) or `venv\Scripts\activate` (Windows).
5. Install dependencies: `pip install -r requirements.txt`.
6. Download a local model (e.g., via Hugging Face): The scripts use 'distilbert-base-uncased-finetuned-sst-2-english' for sentiment scoring as a proxy for lead scoring. For better results, fine-tune or use a custom model.

## Running the Examples

### CRM Scorer
Run `python crm_scorer.py` to score leads in `sample_leads.csv`. It outputs scored leads to `scored_leads.csv`.

### Outreach Bot
Run `python outreach_bot.py` to generate sample outreach emails for the leads.

These scripts are beginner-friendly and include error handling. Customize `config.yaml` for different models or prompts.

Note: For full DenchClaw integration, install the main framework as shown in the video.

---

## Disclaimer

This code is provided as-is for educational purposes only. **Use at your own risk** — no warranty is provided, express or implied. The authors are not responsible for any damages or issues arising from the use of this code.

## License

MIT License

---

*Made by [Prism Labs AI](https://youtube.com/@prismlabsai)*
