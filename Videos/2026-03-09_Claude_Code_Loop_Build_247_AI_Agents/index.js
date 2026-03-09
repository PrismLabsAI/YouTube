require('dotenv').config();
const { Anthropic } = require('@anthropic-ai/sdk');
const cron = require('node-cron');

// Initialize Anthropic client
const anthropic = new Anthropic({
  apiKey: process.env.ANTHROPIC_API_KEY,
});

// Core loop template for autonomous agents
async function runAgentLoop(prompt, intervalSeconds = 30) {
  console.log('Starting Claude Code Loop Agent...');

  // Infinite loop with error handling
  while (true) {
    try {
      // Call Claude 3.5 Sonnet
      const response = await anthropic.messages.create({
        model: 'claude-3-5-sonnet-20241022',
        max_tokens: 1000,
        messages: [
          {
            role: 'user',
            content: prompt,
          },
        ],
      });

      console.log('Loop Response:', response.content[0].text);

      // Wait for next iteration
      await new Promise(resolve => setTimeout(resolve, intervalSeconds * 1000));
    } catch (error) {
      console.error('Error in loop:', error.message);
      // Retry after a short delay
      await new Promise(resolve => setTimeout(resolve, 5000));
    }
  }
}

// Example usage: Replace with your custom prompt
// runAgentLoop('Monitor system status and report any issues.', 60);

// For testing, uncomment below:
// runAgentLoop('Generate a random number between 1 and 100.', 10);

// Note: This is a template. Customize the prompt and interval for your use case.
// To make it cron-based instead of while loop, use cron.schedule('* * * * *', async () => { ... });