import discord, sys, asyncio                            # Importing Modules
from discord.ext.commands import Bot
from discord.ext import commands
from core.tokenkey import token
from cwd import cwd
 
Client = discord.Client()
bot = commands.Bot(command_prefix = "f!")

initial_extensions = ['core.core',
                      'core.usercmds',
                      'core.modcmds']

adminstaff = ['アロンニクスゲーム「archonxgames」#5535',
              'Karlo#2230',
              'NotSoSaint Nik#9492',
              'iSupernova#0001',
              'rgb#7152']
modstaff = ['4614/goinallout8#8911',
            'Garenthino#7782',
            'yelyaH#0420',
            'T.#6294',
            'MrChallenor#4807',
            'Nathan Best|NEBEST04#5298',
            'SKULL9867#3659',
            '4We2eb0#5615',
            'Wolfy#9498',
            'Technobot#5601',
            'Nukelar#2781',
            '黑人#1241']

# Perms
guest = {'Guest'}
members = {'Member'}
mod = {'Moderator'}
admin = {'Admin'}
