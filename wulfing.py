##
## FF14 PROJECT, 2023
## Bot-Wulfing
## File description:
## this file will serve as the main file for the bot to create interaction with the server (when a member join or leave the server)
##

import discord
from dotenv import load_dotenv
from discord.ext import commands
import os
# from login_part import access_token

load_dotenv()

bot_token = os.getenv('TOKEN_CAC')

if bot_token is None:
    raise Exception('BOT_TOKEN not found in .env file')

intents = discord.Intents.default()
intents.members = True

bot = commands.Bot(command_prefix='!', intents=intents)
member_list = []
Role = "Newbie"

@bot.event
async def on_ready():
    global member_list
    print(f'{bot.user.name} has connected to Discord!')
    server = bot.guilds[0]
    member_list = [member.name for member in server.members]
    print("\n".join(member_list))
    
@bot.event
async def on_member_join(member):
    global member_list
    print(f'{member.name} has joined the server')
    welcome_message = f'Welcome to the Wulfing server, {member.name}! Please fill out this form [here](https://docs.google.com/forms/d/e/1FAIpQLSebHG8Z2jDBtnGz5gsCQ6DWnZN9m9vO9-KSpyAf-kwqj9TUEA/viewform) and use after the command !Validate to get the role and access to all channels.'
    if not member.bot:
        await member.send(welcome_message)
    else:
        print("Nope it's a bot, i can't send him a message")
    member_list.append(member.name)
    print("\n".join(member_list))
            
@bot.command(name="Validate")
async def validate_member(ctx):
    print("vaise je suis la")
    guild = bot.guilds[0]
    member = guild.get_member_named(ctx.author.name)
    if member:
        print(member)
        validate_role = discord.utils.get(guild.roles, name=Role)
        print("VVAA " + str(validate_role))
        await member.add_roles(validate_role)
    else:
        print("Nope, no member found")
            
bot.run(bot_token)

