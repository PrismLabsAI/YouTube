# Outreach Bot Agent Example
# This script simulates a DenchClaw outreach agent that generates personalized emails.
# It uses a local AI model to create email content based on lead data.

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

# Generate email function
def generate_emails(leads_df, model_name, prompt_template):
    try:
        # Load local text generation pipeline
        generator = pipeline('text-generation', model=model_name)
        
        emails = []
        for index, row in leads_df.iterrows():
            prompt = prompt_template.format(name=row['name'])
            result = generator(prompt, max_length=100, num_return_sequences=1)[0]['generated_text']
            emails.append(result.strip())
            print(f"Generated email for {row['name']}:\n{result.strip()}\n")
        
        leads_df['email_content'] = emails
        return leads_df
    except Exception as e:
        print(f"Error during generation: {e}")
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
    
    # Generate emails
    updated_df = generate_emails(leads_df, config['model_name'], config['prompt_template'])
    if updated_df is not None:
        updated_df.to_csv('outreach_emails.csv', index=False)
        print("Outreach emails saved to outreach_emails.csv")
