# FluxBot by Nuk3lar and Silver07(Maxminecraft101e) for the GCorp Discord
# Discord.py rewrite branch docs https://discordpy.readthedocs.io/en/rewrite/index.html
import discord, sys, asyncio, logging, traceback
from discord.ext.commands import Bot
from discord.ext import commands
from core.config import token, Client, bot, initial_extensions
# Logging config
logging.basicConfig(filename='output.log', filemode='w', level=logging.INFO, format='%(asctime)s:%(levelname)s:%(message)s')

print('==============FluxBot Starting==============')

# Loading Modules
if __name__ == '__main__':
    print('[ExtensionManager] Loading Extensions')
    logging.info('[ExtensionManager] Loading Extensions')
    for extension in initial_extensions:
        try:
            bot.load_extension(extension)
            print('[ExtensionManager] Extension: '+extension+' loaded')
            logging.info('[ExtensionManager] Extension: '+extension+' loaded')
        except Exception as e:
            print(f'[ExtensionManager] Failed to load extension {extension}.', file=sys.stderr)
            logging.info('[ExtensionManager] Failed to load extension '+extension+'.')
            traceback.print_exc()
    print('[ExtensionManager] Extension Loading Complete')
    logging.info('[ExtensionManager] Extension Loading Complete')
        

version="0.1.5"
# On bot ready
print(f'[Version] {version}')
@bot.event
async def on_ready():
    print(f'==============FluxBot {version} Started==============')
    logging.info("FLUXBOT "+version+" STARTED")
    await bot.change_presence(activity=discord.Activity(name='f!help', type=3))
    embed=discord.Embed(title= u"\u2705"+f" FluxBot {version} Started!", desctiption="", color=0xb20000)
    channel = bot.get_channel(430463352523849740)
    await channel.send('', embed=embed)

bot.run(token, bot=True, reconnect=True)