import discord
import os
import google.generativeai as genai
from typing import Optional
from dotenv import load_dotenv
load_dotenv()


class MyClient(discord.Client):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Initialize Gemini
        api_key = os.environ.get("GOOGLE_API_KEY")
        if not api_key:
            raise ValueError("Google API key not found in environment variables")
        genai.configure(api_key=api_key)
        self.model = genai.GenerativeModel('gemini-1.5-flash')

    async def on_ready(self):
        print(f'Logged on as {self.user}!')

    async def generate_response(self, user_message: str) -> Optional[str]:
        try:
            response = self.model.generate_content(user_message)
            return response.text
        except Exception as e:
            print(f"Error generating Gemini response: {e}")
            return "I apologize, but I encountered an error processing your request."

    async def on_message(self, message):
        print(f'Message from {message.author}: {message.content}')
        print(message.mentions)

        # Ignore messages from the bot itself
        if message.author == self.user:
            return

        # Check if bot is mentioned
        if self.user in message.mentions:
            try:
                async with message.channel.typing():
                    # Remove the bot mention and clean the message
                    clean_message = message.content.replace(f'<@{self.user.id}>', '').strip()

                    response = await self.generate_response(clean_message)

                    # Handle Discord's 2000 character limit
                    if len(response) > 2000:
                        chunks = [response[i:i+1999] for i in range(0, len(response), 1999)]
                        for chunk in chunks:
                            await message.channel.send(chunk)
                    else:
                        await message.channel.send(response)

            except discord.errors.HTTPException as e:
                print(f"Discord API error: {e}")
                await message.channel.send("I encountered an error sending the message.")
            except Exception as e:
                print(f"Unexpected error: {e}")
                await message.channel.send("An unexpected error occurred.")

def main():
    try:
        token = os.environ.get("SECRET_KEY")
        if not token:
            raise ValueError("Discord token not found in environment variables")

        intents = discord.Intents.default()
        intents.message_content = True

        client = MyClient(intents=intents)
        client.run(token)
    except Exception as e:
        print(f"Failed to start the bot: {e}")

if __name__ == "__main__":
    main()