import discord, sys, asyncio, logging, time, traceback                                  # Importing Modules
from discord.ext.commands import Bot
from discord.ext import commands
from core.config import Client, bot, admin, mod
class management:
    def __init__(self, bot):
        self.bot = bot
    @commands.has_any_role(*mod, *admin)
    @commands.command(name="kick")
    async def _kick(self, message, member: discord.Member, *, reason : str = None):
        strmember = str(member)
        strauthor = str(message.author)
        channel = self.bot.get_channel(430538897211129856)
        intauthorid = message.author.id
        authorid = str(intauthorid)
        logging.info('CMD ~~kick ran by User ID: '+authorid)
        if reason is None:
            embed=discord.Embed(title=u'\u26D4'+' User '+strmember+' was kicked by '+strauthor, description='\nNo reason provided', color=0xff0000)
            await channel.send(embed=embed)
            kickedIDint = member.id
            kickedid = str(kickedIDint)
            logging.info('User ID: '+kickedid+' was kicke by User ID: '+authorid)
            embed=discord.Embed(title=u'\u26D4'+' You were kicked by '+strauthor, description='\nNo reason provided', color=0xff0000)
            await member.create_dm()      #Makes a DM with user
            channel = member.dm_channel
            await channel.send('', embed=embed)
            await member.kick(reason=reason)
        else:
            embed=discord.Embed(title=u'\u26D4'+' User '+strmember+' was kicked by '+strauthor, description='\nReason: '+reason, color=0xff0000)
            await channel.send(embed=embed)
            intauthorid = message.author.id
            authorid = str(intauthorid)
            logging.info('CMD ~~kick ran by User ID: '+authorid)
            kickedIDint = member.id
            kickedid = str(kickedIDint)
            logging.info('User ID: '+kickedid+' was kicked for: '+reason+' by User ID: '+authorid)
            embed=discord.Embed(title=u'\u26D4'+' You were kicked by '+strauthor, description='\nReason: '+reason, color=0xff0000)
            await member.create_dm()      #Makes a DM with user
            channel = member.dm_channel
            await channel.send('', embed=embed)
            await member.kick(reason=reason)
    @commands.has_any_role(*admin)
    @commands.command(name="ban")
    async def  _ban(self, message, member: discord.Member, *, reason : str = None):
        strmember = str(member)
        strauthor = str(message.author)
        intauthorid = message.author.id
        authorid = str(intauthorid)
        logging.info('CMD ~~ban ran by User ID: '+authorid)
        channel = self.bot.get_channel(430538897211129856)
        if reason is None:
            embed=discord.Embed(title=u'\u26D4'+' User '+strmember+' was BANNED by '+strauthor, description='\nNo reason provided', color=0xff0000)
            await channel.send(embed=embed)
            bannedIDint = member.id
            bannedid = str(bannedIDint)
            logging.info('User ID: '+bannedid+' was BANNED by User ID: '+authorid)
            embed=discord.Embed(title=u'\u26D4'+' You were BANNED by '+strauthor, description='\nNo reason provided', color=0xff0000)
            await member.create_dm()      #Makes a DM with user
            channel = member.dm_channel
            await channel.send('', embed=embed)
            await member.ban(reason=reason, delete_message_days=0)
        else:
            embed=discord.Embed(title=u'\u26D4'+' User '+strmember+' was BANNED by '+strauthor, description='\nReason: '+reason, color=0xff0000)
            await channel.send(embed=embed)
            bannedIDint = member.id
            bannedid = str(bannedIDint)
            logging.info('User ID: '+bannedid+' was BANNED for: '+reason+' by User ID: '+authorid)
            embed=discord.Embed(title=u'\u26D4'+' You were BANNED by '+strauthor, description='\nReason: '+reason, color=0xff0000)
            await member.create_dm()      #Makes a DM with user
            channel = member.dm_channel
            await channel.send('', embed=embed)
            await member.ban(reason=reason, delete_message_days=0)
        
        
    @commands.has_any_role(*admin)
    @commands.command(name="reload")
    async def _reload(self, message, *, part: str):
        channel = message.channel  
        try:
            bot.unload_extension(part)
            embed=discord.Embed(title=u'\u2705'+f' {part} unloaded successfly!')
            await channel.send('', embed=embed)
            time.sleep(2)
            try:
                bot.load_extension(part)
                embed=discord.Embed(title=u'\u2705'+f' {part} reloaded successfly!')
                await channel.send('', embed=embed)
            except:
                embed=discord.Embed(title=u'\u247C'+f' {part} failed to load back in...')
                traceback.print_exc()
                await channel.send('', embed=embed)
        except:
            embed=discord.Embed(title=u'\u247C'+f' {part} failed to unload...')
            traceback.print_exc()
            await channel.send('', embed=embed)
            

def setup(bot):
    bot.add_cog(management(bot))