import discord
from discord.ext import commands
import os
from dotenv import load_dotenv

# Intents to give bot permission to access data in the server
intents = discord.Intents.default()
# Setting to be able to read messages for command functionality
intents.message_content = True

# Setting a command prefix
bot = commands.Bot(command_prefix='~', intents=intents)

# Event - Runs when bot connects to the server
@bot.event
async def on_ready():
    print(f'Bot connected as {bot.user}')

# Command - Command to test if bot is working
@bot.command()
async def hello(context):
    await context.send(f'Hi {context.author}! I hope you are well.')

# Run the bot with your token
load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
bot.run(TOKEN)
