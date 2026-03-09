require('dotenv').config();
const { Anthropic } = require('@anthropic-ai/sdk');
const fs = require('fs');

// Initialize Anthropic client
const anthropic = new Anthropic({
  apiKey: process.env.ANTHROPIC_API_KEY,
});

let ideaCount = 0;
const maxIdeas = 50;

async function runContentGeneratorAgent() {
  console.log('Starting Content Generator Agent...');

  while (true) {
    try {
      if (ideaCount >= maxIdeas) {
        console.log('Reached max ideas. Resetting...');
        ideaCount = 0;
      }

      // Generate Twitter thread idea
      const response = await anthropic.messages.create({
        model: 'claude-3-5-sonnet-20241022',
        max_tokens: 1000,
        messages: [
          {
            role: 'user',
            content: 'Generate a daily Twitter thread idea on AI news. Format as JSON with keys: title, tweets (array of strings).',
          },
        ],
      });

      const idea = JSON.parse(response.content[0].text);
      console.log('Generated Idea:', idea.title);

      // Save to file
      const state = { count: ++ideaCount, lastIdea: idea };
      fs.writeFileSync('agent_state.json', JSON.stringify(state, null, 2));

      // Wait 1 hour (3600 seconds)
      await new Promise(resolve => setTimeout(resolve, 3600000));
    } catch (error) {
      console.error('Error in content generator:', error.message);
      await new Promise(resolve => setTimeout(resolve, 5000));
    }
  }
}

runContentGeneratorAgent();