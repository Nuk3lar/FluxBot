# FluxBot by Nuk3lar and Silver07(Maxminecraft101e) for the GCorp Discord
# Discord.py rewrite branch docs https://discordpy.readthedocs.io/en/rewrite/index.html
import discord, sys, asyncio, logging, traceback
from discord.ext.commands import Bot
from discord.ext import commands
from core.config import token, Client, bot, initial_extensions
# Logging config
logging.basicConfig(filename='output.log', filemode='w', level=logging.INFO, format='%(asctime)s:%(levelname)s:%(message)s')

print('\n=======FluxBot Starting=======')
print('\nStarting\n\nLoading Modules\n')

# Loading Modules
if __name__ == '__main__':
    for extension in initial_extensions:
        try:
            bot.load_extension(extension)
            print('Extension: '+extension+' loaded\n')
        except Exception as e:
            print(f'Failed to load extension {extension}.', file=sys.stderr)
            traceback.print_exc()
        

version="0.1.3"
# On bot ready
print("Nearly done\n")
@bot.event
async def on_ready():
    print(f"\nFLUXBOT {version} STARTED")
    logging.info("FLUXBOT "+version+" STARTED")
    await bot.change_presence(activity=discord.Activity(name='f!help', type=3))

bot.run(token, bot=True, reconnect=True)