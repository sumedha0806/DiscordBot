# Discord AI Chatbot 🤖  

A Discord bot that leverages OpenAI's GPT and Google's Gemini AI to respond to user messages intelligently. This bot listens for mentions in a server and generates responses using AI models.  

## 🚀 Features  
- Responds to messages when mentioned  
- Uses both OpenAI's GPT and Google's Gemini AI for responses  
- Handles message chunking for Discord’s 2000-character limit  
- Error handling for API failures  

## 🛠️ Setup Instructions  

### 1️⃣ Prerequisites  
Ensure you have:  
- Python 3.8+ installed  
- A Discord bot token  
- OpenAI API key  
- Google API key  
- `dotenv` package for managing environment variables  

### 2️⃣ Install Dependencies  
Run the following command to install the required libraries:  
```bash

pip install discord openai google-generativeai python-dotenv
```

### 3️⃣ Environment Variables
Create a .env file in the project directory and add:
SECRET_KEY=your_discord_bot_token    
GOOGLE_API_KEY=your_google_api_key

### 4️⃣ Run the Bot
Execute the script with:
```bash

python main.py
```

🛠️ How It Works
1. Listens to messages on a Discord server
2. If the bot is mentioned, it processes the message
3. Uses either OpenAI's GPT-3.5 or Google's Gemini AI to generate a response
4. Sends the response back to the Discord channel

📌 Notes
Please make sure your bot has the necessary permissions (read/write message content).
Handle API rate limits properly if you expect high usage.
Feel free to modify the bot’s logic to improve responses.

📜 License
This project is open-source under the MIT License.
