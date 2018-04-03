import discord, sys, asyncio, logging, time, traceback                                  # Importing Modules
from discord.ext.commands import Bot
from discord.ext import commands
from core.config import Client, bot, admin, mod, embedcolorred, embedcolorpur, dev
class management:
    def __init__(self, bot):
        self.bot = bot
    @commands.has_any_role(*mod, *admin)
    @commands.guild_only()
    @commands.command(name="kick", enabled=False)
    async def _kick(self, message, member: discord.Member, *, reason : str = None):
        strmember = str(member)
        strauthor = str(message.author)
        channel = self.bot.get_channel(430538897211129856)
        intauthorid = message.author.id
        authorid = str(intauthorid)
        logging.info('CMD f!kick ran by User ID: '+authorid)
        if reason is None:
            embed=discord.Embed(title=u'\u26D4'+' User '+strmember+' was kicked by '+strauthor, description='\nNo reason provided', color=embedcolorred)
            await channel.send(embed=embed)
            kickedIDint = member.id
            kickedid = str(kickedIDint)
            logging.info('User ID: '+kickedid+' was kicke by User ID: '+authorid)
            embed=discord.Embed(title=u'\u26D4'+' You were kicked by '+strauthor, description='\nNo reason provided', color=embedcolorred)
            await member.create_dm()      #Makes a DM with user
            channel = member.dm_channel
            await channel.send('', embed=embed)
            await member.kick(reason=reason)
        else:
            embed=discord.Embed(title=u'\u26D4'+' User '+strmember+' was kicked by '+strauthor, description='\nReason: '+reason, color=embedcolorred)
            await channel.send(embed=embed)
            intauthorid = message.author.id
            authorid = str(intauthorid)
            logging.info('CMD f!kick ran by User ID: '+authorid)
            kickedIDint = member.id
            kickedid = str(kickedIDint)
            logging.info('User ID: '+kickedid+' was kicked for: '+reason+' by User ID: '+authorid)
            embed=discord.Embed(title=u'\u26D4'+' You were kicked by '+strauthor, description='\nReason: '+reason, color=embedcolorred)
            await member.create_dm()      #Makes a DM with user
            channel = member.dm_channel
            await channel.send('', embed=embed)
            await member.kick(reason=reason)
    @commands.has_any_role(*admin)
    @commands.guild_only()
    @commands.command(name="ban", enabled=False)
    async def  _ban(self, message, member: discord.Member, *, reason : str = None):
        strmember = str(member)
        strauthor = str(message.author)
        intauthorid = message.author.id
        authorid = str(intauthorid)
        logging.info('CMD f!ban ran by User ID: '+authorid)
        channel = self.bot.get_channel(430538897211129856)
        if reason is None:
            embed=discord.Embed(title=u'\u26D4'+' User '+strmember+' was BANNED by '+strauthor, description='\nNo reason provided', color=embedcolorred)
            await channel.send(embed=embed)
            bannedIDint = member.id
            bannedid = str(bannedIDint)
            logging.info('User ID: '+bannedid+' was BANNED by User ID: '+authorid)
            embed=discord.Embed(title=u'\u26D4'+' You were BANNED by '+strauthor, description='\nNo reason provided', color=embedcolorred)
            await member.create_dm()      #Makes a DM with user
            channel = member.dm_channel
            await channel.send('', embed=embed)
            await member.ban(reason=reason, delete_message_days=0)
        else:
            embed=discord.Embed(title=u'\u26D4'+' User '+strmember+' was BANNED by '+strauthor, description='\nReason: '+reason, color=embedcolorred)
            await channel.send(embed=embed)
            bannedIDint = member.id
            bannedid = str(bannedIDint)
            logging.info('User ID: '+bannedid+' was BANNED for: '+reason+' by User ID: '+authorid)
            embed=discord.Embed(title=u'\u26D4'+' You were BANNED by '+strauthor, description='\nReason: '+reason, color=embedcolorred)
            await member.create_dm()      #Makes a DM with user
            channel = member.dm_channel
            await channel.send('', embed=embed)
            await member.ban(reason=reason, delete_message_days=0)
        
        
    @commands.has_role(*mod)
    @commands.has_role(*dev)
    @commands.command(name="reload")
    async def _reload(self, message, *, part: str):
        channel = message.channel
        intauthorid = message.author.id
        authorid = str(intauthorid)
        logging.info('CMD f!reload ran by User ID: '+authorid)
        
        if part == "main":
            embed=discord.Embed(title=u'\u274C'+' You cannot reload the main file!', color=embedcolorred)
            await message.channel.send('', embed=embed)
        else:
            try:
                bot.unload_extension(part)
                embed=discord.Embed(title=u'\u2705'+f' {part} unloaded successfly!', color=embedcolorpur)
                await channel.send('', embed=embed)
                print(f'[ExtensionManager] Successfully unloaded extension {part}')
                logging.info('[ExtensionManager] Successfully unloaded extension '+part+'')
                time.sleep(2)
                try:
                    
                    bot.load_extension(part)
                    print(f'[ExtensionManager] Successfully reloaded extension {part}')
                    logging.info('[ExtensionManager] Successfully reloaded extension '+part+'')
                    embed=discord.Embed(title=u'\u2705'+f' {part} reloaded successfly!', color=embedcolorpur)
                    await channel.send('', embed=embed)
                except:
                    print(f'[ExtensionManager] Failed to load extension {part} back in.', file=sys.stderr)
                    logging.info('[ExtensionManager] Failed to load extension '+part+' back in.')
                    embed=discord.Embed(title=u'\u274C'+f' {part} failed to load back in...', color=embedcolorred)
                    traceback.print_exc()
                    await channel.send('', embed=embed)
            except:
                embed=discord.Embed(title=u'\u274C'+f' {part} failed to unload...', color=embedcolorred)
                print(f'[ExtensionManager] Failed to unload extension {part}')
                logging.info('[ExtensionManager] Failed to unload extension '+part+'')
                traceback.print_exc()
                await channel.send('', embed=embed)
class ModHelp:
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name='modhelp')
    @commands.has_any_role(*mod, *admin)
    @commands.guild_only()
    async def _modhelp(self, message, *, part : str = None):
        if part is None:
            embed=discord.Embed(title="Help for FluxBot", description="List of Admin & Mod commands\n(part) | Required arguement\n[part] | Optional arguement\nDon't include the brackets used in examples!", color=embedcolorpur)
            embed.set_author(name="Nukelar", url="https://github.com/Nuk3lar/FluxBot", icon_url="https://i.imgur.com/xBxfC7Y.png")
            embed.set_thumbnail(url="https://i.imgur.com/mNMjP3D.png")
            embed.add_field(name='Commands', value='`f!kick` | Kicks a user\n`f!warn` | Warns a user\n`f!ban` | Bans a user\n`f!reload` | Reloads a part of the bot')
            embed.set_footer(text="Use f!modhelp [cmd] to view specific help and usage info on a command!")
            channel = message.channel
            await channel.send('', embed=embed)

def setup(bot):
    bot.add_cog(management(bot))
    bot.add_cog(ModHelp(bot))