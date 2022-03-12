# -*- coding: utf-8 -*-
import os, sys, termcolor, discord, asyncio, random, time, datetime,json
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
#from discord.ext.commands import MissingPermissions

__colors__ = __classes__.__colors__
__attributes__ = __classes__.__attributes__
__highlights__ = __classes__.__highlights__
#Starts cog
class listens(commands.Cog):
  def __init__(self,bot):
      self.bot = bot




  @commands.Cog.listener()
  async def on_error(self,error,ctx):
    if isinstance(error, discord.errors.Forbidden):
      await ctx.channel.send("I don't have permissions please give me permissions")
      







  @commands.command()
  @commands.has_permissions(administrator=True)
  async def poll(self, ctx, *, message):
    await ctx.message.delete()
    embed = discord.Embed(color= discord.Color.green(), timestamp=ctx.message.created_at)
    embed.set_author(name="Luwiz poll")
    embed.add_field(name="poll Request", value=f"{message}")
    message = await ctx.channel.send(embed=embed)
    await message.add_reaction('👍')
    await message.add_reaction('👎')

  @commands.command()
  @commands.has_permissions(embed_links=True)
  @commands.cooldown(1, 60, BucketType.guild)
  async def answer(self, ctx, *, message):
    await ctx.message.delete()
    embed = discord.Embed(colour=0x06eebf)
    embed.set_author(name="Luwiz Answer Sheet")
    embed.add_field(name=f"{ctx.author} needs an answer", value=f"{message}")
    message = await ctx.channel.send(embed=embed)
    await message.add_reaction('✅')
    await message.add_reaction('❌')






  @commands.Cog.listener()
  async def on_member_join(self, ctx, member):
    if ctx.guild.id == 810973735749550141:
      embed1 = discord.Embed(color=discord.Color.red())
      embed1.set_author(name="🔑Verification🔑")
      embed1.add_field(name="🔑Server Authentication🔑", value=f" You must wait utpo 12 minutes before entering ****{member.guild}****.")
      await member.send(embed=embed1)
      await asyncio.sleep(480)
      role = discord.utils.get(member.guild.roles, name='Users')
      await member.add_roles(role)
      embed = discord.Embed(color=discord.Color.red())
      embed.set_author(name="🔑Verification🔑")
      embed.add_field(name="🔑Server Authentication🔑", value=f"****{member.guild}**** has now been granted")
      await member.send(embed=embed)
 
  @commands.Cog.listener()
  async def on_member_join(self,member):
    channel = member.guild.system_channel
    if channel is not None: 
      embed = discord.Embed(colour=0x06e4ee)
      embed.set_author(name=f"{member.name}")
      embed.add_field(name="Welcome!", value=f"Please welcome {member.mention} to the server!")
      embed.set_image(url=member.avatar_url)  
      await channel.send(embed=embed)
    else:
      pass











  @commands.Cog.listener()
  async def on_guild_join(self,guild):
    channel = guild.system_channel
    if channel is None:
      pass
    else:
      embed = discord.Embed(title = f"👋 Hello! Thanks for adding me to the server", colour = 0x1df30e) 
      embed.add_field(name=f"defult prefix is ! \nto get help say help ", value=f"for any other questions join our [support server](https://discord.gg/dnBcSafW9Z)\nmake sure i have admin permissions so you can get the most out of me")
      #await owner.send("hey there thanks for adding me to youre server make sure i have admin permissions so people can get the most out of me")
      await channel.send(embed=embed)





















#tells in console if cog has been loaded
def setup(bot):
    bot.add_cog(listens(bot))
    cprint(colored("""Cog: listens
Status: Loaded""", __colors__.blue))