# Custom Tools for NanoClaw Agent
# This script defines tools using Anthropic's SDK for tool calling.
# Tools are functions that the AI can invoke.

import os
import requests
from anthropic import Anthropic

# Initialize Anthropic client
client = Anthropic(api_key=os.environ['ANTHROPIC_API_KEY'])

# Tool: Get current weather (mock example)
def get_weather(location: str) -> str:
    """Fetch weather data for a location."""
    try:
        # In a real scenario, use a weather API like OpenWeatherMap
        # For demo, return mock data
        return f"Weather in {location}: Sunny, 75°F"
    except Exception as e:
        return f"Error fetching weather: {str(e)}"

# Tool: Send weekly report (for scheduled jobs)
def send_weekly_report() -> str:
    """Generate and send a weekly report."""
    try:
        # Mock report generation
        report = "Weekly Summary: All systems operational."
        # In real use, send via email or messaging
        print(f"Sending report: {report}")
        return "Weekly report sent successfully."
    except Exception as e:
        return f"Error sending report: {str(e)}"

# Tool: Calculate sum
def calculate_sum(a: int, b: int) -> int:
    """Add two numbers."""
    return a + b

# List of available tools for the agent
tools = [
    {
        "name": "get_weather",
        "description": "Get the current weather for a location.",
        "input_schema": {
            "type": "object",
            "properties": {
                "location": {"type": "string", "description": "City name"}
            },
            "required": ["location"]
        }
    },
    {
        "name": "send_weekly_report",
        "description": "Send a weekly report.",
        "input_schema": {"type": "object", "properties": {}}
    },
    {
        "name": "calculate_sum",
        "description": "Calculate the sum of two numbers.",
        "input_schema": {
            "type": "object",
            "properties": {
                "a": {"type": "integer"},
                "b": {"type": "integer"}
            },
            "required": ["a", "b"]
        }
    }
]

# Function to handle tool calls
def handle_tool_call(tool_name, tool_input):
    if tool_name == "get_weather":
        return get_weather(**tool_input)
    elif tool_name == "send_weekly_report":
        return send_weekly_report()
    elif tool_name == "calculate_sum":
        return calculate_sum(**tool_input)
    else:
        return "Unknown tool."
