import discord
from dotenv import load_dotenv
from discord.ext import commands
import os

load_dotenv()

bot_token = os.getenv('TOKEN_CAC')

if bot_token is None:
    raise Exception('BOT_TOKEN not found in .env file')

intents = discord.Intents.default()
intents.members = True

bot = commands.Bot(command_prefix='!', intents=intents)
member_list = []

@bot.event
async def on_ready():
    print(f'{bot.user.name} has connected to Discord!')
    server = bot.guilds[0]
    member_list = [member.name for member in server.members]
    print("\n".join(member_list))
    
@bot.event
async def on_member_join(member):
    print(f'{member.name} has joined the server')
    welcome_message = f'Welcome to the Wulfing server, {member.name}! Please fill out this form [here](https://docs.google.com/forms/d/e/1FAIpQLSebHG8Z2jDBtnGz5gsCQ6DWnZN9m9vO9-KSpyAf-kwqj9TUEA/viewform)'
    if not member.bot:
        await member.send(welcome_message)
    else:
        print("Nope it's a bot, i can't send him a message")
    print("Last test")
    for member in member_list:
        print(member)
    member_list.append(member.name)
    print("\n".join(member_list))
    print(f'Current members:')
    for member in member_list:
        print(member)
        
@bot.event
async def on_member_remove(member):
    print(f'{member.name} has left the server')
    leave_message = f'Hey, we are really sad for by your leaving we know you have your reasons and we understand it. But please can you fill out this form [here](https://docs.google.com/forms/d/e/1FAIpQLSeyHu4P2eMRwgd0GwMC_ntI95UY_Q7sXyqpWPQSR25Sw54Llw/viewform)'
    if not member.bot:
        try:
            user_id = None
            
            for user in member.guild.members:
                if user.name == member.name:
                    user_id = user.id
                    break
            if user_id is not None:
                user = await bot.fetch_user(user_id)
                await user.send(leave_message)
            else:
                print(f'User {member.name} not found')
        except discord.Forbidden as e:
            print(f'I cant send him a message to {member.name}: {e}')
    else:
        print("Nope it's a bot, i can't send him a message")

bot.run(bot_token)

