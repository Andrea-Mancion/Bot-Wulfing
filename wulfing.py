import discord
from dotenv import load_dotenv
import os

load_dotenv()

bot_token = os.getenv('BOT_TOKEN')

if bot_token is None:
    raise Exception('BOT_TOKEN not found in .env file')

bot = discord.Client()

@bot.event
async def on_ready():
    print(f'{bot.user.name} has connected to Discord!')
    
@bot.event
async def on_member_join(member):
    welcome_message = f'Welcome to the Wulfing server, {member.name}! Please fill out this form [here](https://docs.google.com/forms/d/e/1FAIpQLSebHG8Z2jDBtnGz5gsCQ6DWnZN9m9vO9-KSpyAf-kwqj9TUEA/viewform)'
    if not member.bot:
        await member.send(welcome_message)
    else:
        print("Nope it's a bot, i can't send him a message")
        
@bot.event
async def on_member_remove(member):
    leave_message = f'Hey, we are really sad for by your leaving we know you have your reasons and we understand it. But please can you fill out this form [here](https://docs.google.com/forms/d/e/1FAIpQLSeyHu4P2eMRwgd0GwMC_ntI95UY_Q7sXyqpWPQSR25Sw54Llw/viewform)'
    if not member.bot:
        await member.send(leave_message)
    else:
        print("Nope it's a bot, i can't send him a message")

bot.run(bot_token)

