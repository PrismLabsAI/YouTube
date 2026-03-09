# CRM Lead Scorer Agent Example
# This script simulates a DenchClaw CRM agent that scores leads using a local AI model.
# It loads leads from a CSV, scores them based on a simple sentiment analysis (as a proxy),
# and saves the results to a new CSV.

import pandas as pd
from transformers import pipeline
import yaml
import os

# Load configuration
def load_config():
    try:
        with open('config.yaml', 'r') as file:
            return yaml.safe_load(file)
    except FileNotFoundError:
        print("Error: config.yaml not found. Please ensure it exists.")
        return None

# Main scoring function
def score_leads(leads_df, model_name):
    try:
        # Load local sentiment analysis pipeline (runs locally, no API calls)
        classifier = pipeline('sentiment-analysis', model=model_name)
        
        scores = []
        for index, row in leads_df.iterrows():
            # Use lead name or email as input for scoring (simple example)
            text = f"{row['name']} {row['email']}"
            result = classifier(text)[0]
            # Map sentiment to lead score
            if result['label'] == 'POSITIVE':
                score = 'hot' if result['score'] > 0.8 else 'medium'
            else:
                score = 'low'
            scores.append(score)
            print(f"{row['name']} ({row['email']}): {score} (confidence: {result['score']:.2f})")
        
        leads_df['score'] = scores
        return leads_df
    except Exception as e:
        print(f"Error during scoring: {e}")
        return None

if __name__ == "__main__":
    config = load_config()
    if not config:
        exit(1)
    
    # Load sample leads
    try:
        leads_df = pd.read_csv('sample_leads.csv')
    except FileNotFoundError:
        print("Error: sample_leads.csv not found.")
        exit(1)
    
    # Score leads
    scored_df = score_leads(leads_df, config['model_name'])
    if scored_df is not None:
        scored_df.to_csv('scored_leads.csv', index=False)
        print("Scored leads saved to scored_leads.csv")
