import discord, sys, asyncio                            # Importing Modules
from discord.ext.commands import Bot
from discord.ext import commands
from core.tokenkey import token
from cwd import cwd
 
Client = discord.Client()
bot = commands.Bot(command_prefix = "f!")

initial_extensions = ['core.core',
                      'core.usercmds']

# Perms
guest = {'Guest'}
members = {'Member'}
