import discord
from dotenv import load_dotenv
import os

load_dotenv()

bot = discord.Client()

@bot.event
async def on_ready():
    print(f'{bot.user.name} has connected to Discord!')
    
@bot.event
async def on_member_join(member):
    welcome_message = f'Welcome to the Wulfing server, {member.name}! Please fill out this form [here](https://docs.google.com/forms/d/e/1FAIpQLSebHG8Z2jDBtnGz5gsCQ6DWnZN9m9vO9-KSpyAf-kwqj9TUEA/viewform)'
    await member.send(welcome_message)
    
bot_token = os.getenv('BOT_TOKEN')

if bot_token is None:
    raise Exception('BOT_TOKEN not found in .env file')
else:
    bot.run(bot_token)

