import discord, sys, asyncio, logging                                  # Importing Modules
from discord.ext.commands import Bot
from discord.ext import commands
from core.config import Client, bot, members, guest, cwd, adminstaff, modstaff, embedcolorred, embedcolorpur

class HelpCMD:
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name='help')
    @commands.guild_only()
    async def _help(self, message, *, part=None):
        member = message.author
        memberidint = member.id
        memberid = str(memberidint)
        logging.info('[CommandHandler] CMD f!help ran by User ID: '+memberid)
        print('[CommandHandler] CMD f!help ran by User ID: '+memberid)
        if part is None:
            embed=discord.Embed(title="Help for FluxBot", description="List of commands\n(part) | Required arguement\n[part] | Optional arguement\nDon't include the brackets used in examples!", color=embedcolorpur)
            embed.set_author(name="Nukelar", url="https://github.com/Nuk3lar/FluxBot", icon_url="https://i.imgur.com/xBxfC7Y.png")
            embed.set_thumbnail(url="https://i.imgur.com/mNMjP3D.png")
            embed.add_field(name='Commands', value='`f!help` | Displays this menu\n`f!cookie` | Have a cookie\n`f!staff` | Lists staff\n`f!invite` | Gets invite link\n`f!info` | Get general info ')
            embed.set_footer(text="Use f!help [cmd] to view specific help and usage info on a command!")
            channel = message.channel
            await channel.send('', embed=embed)

class CookieCMD:
    def __init__(self, bot):
        self.bot = bot
    @commands.command(name='cookie')
    @commands.guild_only()
    async def _cookie(self, message, *, touser : discord.Member = None):
        member = message.author
        memberidint = member.id
        memberid = str(memberidint)
        logging.info('[CommandHandler] CMD f!cookie ran by User ID: '+memberid)
        print('[CommandHandler] CMD f!cookie ran by User ID: '+memberid)
        if touser is None:
            channel = message.channel
            await channel.send('Heres a cookie! '+member.mention, file=discord.File(f'{cwd}\\assets\\COOKIE.jpg'))
        else:
            channel = message.channel
            try:
                await channel.send(f'{member.mention} gave you a cookie! {touser.mention}', file=discord.File(f'{cwd}\\assets\\COOKIE.jpg'))
            except:
                await channel.send('Not a user!')

class StaffCMD:
    def __init__(self, bot):
        self.bot = bot
    @commands.command(name='staff')
    @commands.guild_only()
    async def _staff(self, message):
        member = message.author
        memberidint = member.id
        memberid = str(memberidint)
        print('[CommandHandler] CMD f!staff ran by User ID: '+memberid)
        logging.info('[CommandHandler] CMD f!staff ran by User ID: '+memberid)
        embed=discord.Embed(title="Staff list for GCorp", description="", color=embedcolorpur)
        embed.set_author(name="Nukelar", url="https://github.com/Nuk3lar/FluxBot", icon_url="https://i.imgur.com/xBxfC7Y.png")
        embed.set_thumbnail(url="https://i.imgur.com/mNMjP3D.png")
        adminstaffpr = "\n".join(adminstaff)
        
        modstaffpr = "\n".join(modstaff)
        embed.add_field(name='Admins', value=f"{adminstaffpr}\n")
        embed.add_field(name='Mods', value=f"{modstaffpr}")
        channel = message.channel
        await channel.send('', embed=embed)

class GenInvite:
    def __init__(self, bot):
        self.bot = bot
    @commands.command(name="invite")
    @commands.guild_only()
    async def _invite(self, message,):
        embed=discord.Embed(title="Here's a invite!", description="https://discord.gg/8GVxqpz", color=embedcolorpur)
        channel = message.channel
        await channel.send('', embed=embed)
            

def setup(bot):
    bot.remove_command("help")
    bot.add_cog(HelpCMD(bot))
    bot.add_cog(StaffCMD(bot))
    bot.add_cog(CookieCMD(bot))
    bot.add_cog(GenInvite(bot))