require('dotenv').config();
const { Anthropic } = require('@anthropic-ai/sdk');
const axios = require('axios');

// Initialize Anthropic client
const anthropic = new Anthropic({
  apiKey: process.env.ANTHROPIC_API_KEY,
});

let lastPrice = null;

async function runBitcoinAgent() {
  console.log('Starting Bitcoin Price Monitor Agent...');

  while (true) {
    try {
      // Fetch Bitcoin price from CoinGecko (free API)
      const response = await axios.get('https://api.coingecko.com/api/v3/simple/price?ids=bitcoin&vs_currencies=usd');
      const currentPrice = response.data.bitcoin.usd;

      console.log(`Current Bitcoin Price: $${currentPrice}`);

      if (lastPrice !== null) {
        const changePercent = ((currentPrice - lastPrice) / lastPrice) * 100;
        if (Math.abs(changePercent) > 5) {
          // Alert via Claude analysis
          const analysis = await anthropic.messages.create({
            model: 'claude-3-5-sonnet-20241022',
            max_tokens: 500,
            messages: [
              {
                role: 'user',
                content: `Bitcoin price changed by ${changePercent.toFixed(2)}%. Analyze the market impact and suggest actions.`,
              },
            ],
          });
          console.log('Alert:', analysis.content[0].text);
        }
      }

      lastPrice = currentPrice;

      // Wait 30 seconds
      await new Promise(resolve => setTimeout(resolve, 30000));
    } catch (error) {
      console.error('Error in Bitcoin agent:', error.message);
      await new Promise(resolve => setTimeout(resolve, 5000));
    }
  }
}

runBitcoinAgent();