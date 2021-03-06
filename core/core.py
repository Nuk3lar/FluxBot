# Imports all the modules
import discord, sys, asyncio, logging, traceback     
from discord.ext.commands import Bot
from discord.ext import commands
from core.config import Client, bot, embedcolorred, embedcolorpur

Client = discord.Client()

class JoinLeave:
    def __init__(self, bot):
        self.bot = bot
    #On member join
    @Client.event
    async def on_member_join(self, member: discord.Member):
        memberidint = member.id
        memberid = str(memberidint)
        logging.info('User ID [ '+memberid+' ] joined the server')
        await member.create_dm()      #Makes a DM with user
        channel = member.dm_channel
        user = member
        role = discord.utils.get(user.guild.roles, id=319105999485009920)
        await member.add_roles(role)
        await channel.send('Welcome to GCorp '+member.mention)
    #On member leave/kick/ban
    @Client.event
    async def on_member_remove(self, member: discord.Member):
        memberidint = member.id
        memberid = str(memberidint)
        logging.info('User ID [ '+memberid+' ] was kicked, banned or left the server')

class ErrorHandler:
    def __init__(self, bot):
        self.bot = bot
    #Error handler
    async def on_command_error(self, ctx, error):
        error = getattr(error, 'original', error)
        if isinstance(error, commands.CommandNotFound): #CommandNotFound
            logging.error(error) #logs the error
            embed=discord.Embed(title=u'\u274C That is not a command!', description="Please use f!help for a list of valid commands ", color=embedcolorred)
            embed.add_field(name="Make sure you input a **actual** command!", value="This includes capitalisation", inline=True)
            embed.add_field(name="If you continue to experience problems, please raise a issue at", value="https://github.com/Nuk3lar/FluxBot/issues", inline=True)
            channel = ctx.message.channel
            await channel.send('', embed=embed)
        elif isinstance(error, commands.UserInputError):  #User Input not right
            logging.error(error) #logs the error
            embed=discord.Embed(title=u'\u274C You did not input the command correctly!', description='Check that you have entered all the variables.' , color=embedcolorred)
            embed.add_field(name="If you continue to experience problems, please raise a issue at", value="https://github.com/Nuk3lar/FluxBot/issues", inline=True)
            channel = ctx.message.channel
            await channel.send('', embed=embed)
        elif isinstance(error, commands.BotMissingPermissions):  #Bot does not have perms
            logging.error(error) #logs the error
            embed=discord.Embed(title=u'\u274C The bot does not have permission to do that!', description='' , color=embedcolorred)
            embed.add_field(name="Please raise a issue at: ", value="https://github.com/Nuk3lar/FluxBot/issues", inline=True)
            channel = ctx.message.channel
            await channel.send('', embed=embed)
        elif isinstance(error, commands.NoPrivateMessage): #Cant do in dms
            logging.error(error) #logs the error
            embed=discord.Embed(title=u"\u274C Commands can't be ran in DMs ", description='Please run commands for this bot in https://discord.gg/3tgU3E6' , color=embedcolorred)
            embed.add_field(name="If you continue to experience problems, please raise a issue at", value="https://github.com/Nuk3lar/FluxBot/issues", inline=True)
            channel = ctx.message.channel
            await channel.send('', embed=embed)
        elif isinstance(error, commands.DisabledCommand): #Command is disabled
            logging.error(error) #logs the error
            embed=discord.Embed(title=u"\u274C This Command is Disabled", description='' , color=embedcolorred)
            embed.add_field(name="If you continue to experience problems, please raise a issue at", value="https://github.com/Nuk3lar/FluxBot/issues", inline=True)
            channel = ctx.message.channel
            await channel.send('', embed=embed)
        elif isinstance(error, commands.CheckFailure): #User missing role, or other things
            member = ctx.message.author
            memberidint = member.id
            memberid = str(memberidint)
            logging.error('User ID: '+memberid+' tried to run command: '+ctx.command.qualified_name+' but was denied!')
            logging.error(error) #logs the error
            embed=discord.Embed(title=u'\u274C You do not have the permissions for that!', description='If you think that is a error contact Nukelar#2781' , color=embedcolorred)
            embed.add_field(name="If you continue to experience problems, please raise a issue at", value="https://github.com/Nuk3lar/FluxBot/issues", inline=True)
            channel = ctx.message.channel
            await channel.send('', embed=embed)
        else:
            logging.error(error)

def setup(bot):
    bot.add_cog(JoinLeave(bot))
    bot.add_cog(ErrorHandler(bot))