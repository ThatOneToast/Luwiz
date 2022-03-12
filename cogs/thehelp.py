import os, sys, termcolor, discord, asyncio, random, time, datetime, tinydb,json
from termcolor import colored 
from termcolor import cprint 
from discord.ext import commands
from discord.ext.commands import Bot
from discord.utils import get
from discord.ext import tasks
from discord.ext.tasks import loop
from random import *
from modules import __classes__
from discord.ext.commands import BucketType, cooldown, CommandOnCooldown
from tinydb import TinyDB, Query

__colors__ = __classes__.__colors__
__attributes__ = __classes__.__attributes__
__highlights__ = __classes__.__highlights__
#Starts cog
class thehelp(commands.Cog):
  def __init__(self,bot):
      self.bot = bot






  @commands.command()
  @commands.has_permissions(send_messages=True)
  async def help(self, ctx):
    with open("prefixes.json", "r") as f:
      prefixes = json.load(f)
    guild = ctx.guild
    embed = discord.Embed(title=f"""Help category comands""", description=f"My prefix is: {prefixes[str(ctx.guild.id)]}",  colour=0x16e70e)
    embed.add_field(name=f"```{prefixes[str(ctx.guild.id)]}eco```", value="shows eco commands", inline=False)
    embed.add_field(name=f"```{prefixes[str(ctx.guild.id)]}moderation```", value="shows mod commands", inline=False)
    embed.add_field(name=f"```{prefixes[str(ctx.guild.id)]}cmd```", value="shows other commands", inline=False)
    embed.add_field(name=f"```{prefixes[str(ctx.guild.id)]}custom```", value="shows custom commands such as prefix", inline=False)

    embed.add_field(name=f"**invite me and join our support server**", value=f"[Luwiz's website](https://luwizsys.ga)\n[bot invite link](https://discord.com/api/oauth2/authorize?client_id=835248881633329252&permissions=8&scope=bot)\n [support server](https://discord.gg/mM9bAfZ7QH)")

    #embed.set_thumbnail(url=self.bot.user.avatar_url)
    await ctx.channel.send(embed=embed)



#help command goes here
  @commands.command()
  async def eco(self, ctx):
    with open("prefixes.json", "r") as f:
      prefixes = json.load(f)
    guild = ctx.guild
    embed = discord.Embed(color=discord.Colour.blue())
    embed.set_author(name="Economy Commands")
    embed.add_field(name=f"```{prefixes[str(ctx.guild.id)]}bal```", value="""```fix
show your balance of coins in wallet and bank```""", inline=False)
    embed.add_field(name=f"```{prefixes[str(ctx.guild.id)]}beg```", value="""```fix
Beg random strangers for money```""", inline=False)
    embed.add_field(name=f"```{prefixes[str(ctx.guild.id)]}pay```", value="""```fix
send someone money```""", inline=False)
    embed.add_field(name=f"```{prefixes[str(ctx.guild.id)]}slots```", value="""```fix
bet some money on slots```""", inline=False)
    embed.add_field(name=f"```{prefixes[str(ctx.guild.id)]}rob```", value="""```fix
Rob some people```""", inline=False)
    embed.add_field(name=f"```{prefixes[str(ctx.guild.id)]}buy```", value="""```fix
Buy some items```""", inline=False)
    embed.add_field(name=f"```{prefixes[str(ctx.guild.id)]}shop```", value="""```fix
see what items you can buy```""", inline=False)
    embed.add_field(name=f"```{prefixes[str(ctx.guild.id)]}sell```", value="""```fix
sell some items you don't want anymore```""", inline=False)
    embed.add_field(name=f"```{prefixes[str(ctx.guild.id)]}leaderboard```", value="""```fix
view the top 3 richest people```""", inline=False)
    await ctx.channel.send(embed=embed)

  @commands.command(aliases=["mod"])
  async def moderation (self, ctx):
    with open("prefixes.json", "r") as f:
      prefixes = json.load(f)
    embed = discord.Embed(colour=0xf08d08)
    embed.set_author(name=f"modration commands")
    embed.add_field(name=f"```{prefixes[str(ctx.guild.id)]}mute```", value="""```fix
mute a member```""", inline=False)
    embed.add_field(name=f"```{prefixes[str(ctx.guild.id)]}unmute```", value="""```fix
unmute a member```""", inline=False)
    embed.add_field(name=f"```{prefixes[str(ctx.guild.id)]}kick```", value="""```fix
kick a member```""", inline=False)
    embed.add_field(name=f"```{prefixes[str(ctx.guild.id)]}ban```", value="""```fix
bans a member```""", inline=False)  
    embed.add_field(name=f"```{prefixes[str(ctx.guild.id)]}purge```", value="""```fix
delete a amount of messages```""", inline=False)  
    embed.add_field(name=f"```{prefixes[str(ctx.guild.id)]}say```", value="""```fix
make the bot say something```""", inline=False)
    embed.add_field(name=f"```{prefixes[str(ctx.guild.id)]}warn```", value="""```fix
warns a user```""", inline=False)
    await ctx.send(embed=embed) 

  
  @commands.command(aliases=["commands","command"])
  async def cmd(self, ctx):
    with open("prefixes.json", "r") as f:
      prefixes = json.load(f)
    embed = discord.Embed(title="commands", colour=0x0ee7f3)
    embed.add_field(name=f"```{prefixes[str(ctx.guild.id)]}pfp```", value="""```fix
shows a members avatar image```""", inline=False)
    embed.add_field(name=f"```{prefixes[str(ctx.guild.id)]}embed```", value="""```fix
embed a ctx```""", inline=False)
    embed.add_field(name=f"```{prefixes[str(ctx.guild.id)]}poll```", value="""```fix
have a poll```""", inline=False)
    embed.add_field(name=f"```{prefixes[str(ctx.guild.id)]}answer```", value="""```fix
ask a question and get a answer```""", inline=False)
    embed.add_field(name=f"```{prefixes[str(ctx.guild.id)]}dice```", value="""```fix
roll a number```""", inline=False)
    embed.add_field(name=f"```{prefixes[str(ctx.guild.id)]}draw```", value="""```fix
draw a card```""", inline=False)
    embed.add_field(name=f"```{prefixes[str(ctx.guild.id)]}bingo```", value="""```fix
get a bingo number```""")
    embed.add_field(name=f"```{prefixes[str(ctx.guild.id)]}number```", value="""```fix
get a number```""", inline=False)
    embed.add_field(name=f"```{prefixes[str(ctx.guild.id)]}kill```", value="""```fix
kill a user```""", inline=False)
    embed.add_field(name=f"```{prefixes[str(ctx.guild.id)]}sbingo```", value="""```fix
bingo link```""", inline=False)
    await ctx.send(embed=embed) 

  @commands.command(aliases=["other"])
  async def custom(self, ctx):
    with open("prefixes.json", "r") as f:
      prefixes = json.load(f)
    embed = discord.Embed(title="custom commands", colour=0x0ee7f3)
    embed.add_field(name=f"```{prefixes[str(ctx.guild.id)]}changeprefix```", value="""```fix
changes the bot prefix```""", inline=False)
    embed.add_field(name=f"```{prefixes[str(ctx.guild.id)]}rank```", value="""```fix
Get your experience level```""", inline=False)
    embed.add_field(name=f"```{prefixes[str(ctx.guild.id)]}levelroles```", value="""```fix
Activates level rewards(AdminOnly)```""", inline=False)
    embed.add_field(name=f"```{prefixes[str(ctx.guild.id)]}claim```", value="""```fix
Claim your level rewards.```""", inline=False)
    await ctx.send(embed=embed)
 


  


def setup(bot):
    bot.add_cog(thehelp(bot))
    cprint(colored("""Cog: thehelp
Status: Loaded""", __colors__.blue))