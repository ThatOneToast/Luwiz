import os, sys, termcolor, discord, asyncio, random, json, time
from termcolor import colored 
from termcolor import cprint  
from discord.ext import commands
from discord.ext.commands import Bot
from discord.utils import get
from discord.ext import tasks
from discord.ext.tasks import loop
from modules import __classes__
from discord.ext.commands import BucketType, cooldown, CommandOnCooldown

__colors__ = __classes__.__colors__
__attributes__ = __classes__.__attributes__
__highlights__ = __classes__.__highlights__
#Starts cog
class commands(commands.Cog):
  def __init__(self,bot):
      self.bot = bot




  @commands.command()
  async def test(self, ctx, member: discord.Member):
    embed=discord.Embed(title=f"um mentioned")
    embed.add_field(name=f" working", value=f"{ctx.author.mention} has mentioned {member.mention}")
    await ctx.channel.send(embed=embed)


#----------------------------------------------------#
#                 Level Role Commands                #
#----------------------------------------------------#
  @commands.command()
  @commands.has_permissions(administrator=True)
  async def levelroles(self,ctx):
    guild = ctx.guild
    await guild.create_role(name="Level 30",color=0x7e7a7a)
    await guild.create_role(name="Level 25",color=0x7e7a7a)
    await guild.create_role(name="Level 20",color=0x7e7a7a)
    await guild.create_role(name="Level 15",color=0x7e7a7a)
    await guild.create_role(name="Level 10",color=0x7e7a7a)
    await guild.create_role(name="Level 5", color=0x7e7a7a)
  
    await ctx.channel.send("Creating all level roles.")
    







  @commands.command()
  async def claim(self,ctx):
    await ctx.message.delete()
    with open("users.json","r") as f:
      users = json.load(f)
    level = users[str(ctx.author.id)]['level']
    if level >= 5:
      role = discord.utils.get(ctx.guild.roles, name="Level 5")
      await ctx.author.add_roles(role)
    if level >= 10:
      role = discord.utils.get(ctx.guild.roles, name="Level 10")
      await ctx.author.add_roles(role)
    if level >= 15:
      role = discord.utils.get(ctx.guild.roles, name="Level 15")
      await ctx.author.add_roles(role)
    if level >= 20:
      role = discord.utils.get(ctx.guild.roles, name="Level 20")
      await ctx.author.add_roles(role)
    if level >= 25:
      role = discord.utils.get(ctx.guild.roles, name="Level 25")
      await ctx.author.add_roles(role)
    if level >= 30:
      role = discord.utils.get(ctx.guild.roles, name="Level 30")
      await ctx.author.add_roles(role)



def setup(bot):
    bot.add_cog(commands(bot))
    cprint(colored("""Cog: commands
Status: Loaded""", __colors__.blue))
