# -*- coding: utf-8 -*-
import os, sys, termcolor, discord, asyncio, random,json
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
from replit import db


__colors__ = __classes__.__colors__
__attributes__ = __classes__.__attributes__
__highlights__ = __classes__.__highlights__
#Starts cog
class premium(commands.Cog):
  def __init__(self,bot):
      self.bot = bot


#premium commands for premium subscribers. 

  @commands.command()
  @commands.has_role("Premium")
  async def premium(self,ctx,*,message=None):
    if ctx.guild.id == 839307082503159859:
      with open("Premium.json","r") as f:
        F = json.load(f)
      #F[str(ctx.guild.id)] = {}
      db[str(ctx.guild.id)] = {}
      db[str(ctx.guild.id)]['GuildID'] = message
      with open("Premium.json","w") as q:
        json.dump(F,q)
      await ctx.channel.send(f"{ctx.author.mention} has claimed their premium ****server****")
    else:
      pass
      
  @commands.command(aliases=['si'])
  async def serverinfo(self,ctx):
    print("test1")
    with open("Premium.json","r") as f:
      fq = json.load(f)
    if str(ctx.guild.id) == fq[str(ctx.guild.id)][("GuildID")]:
      print("test")
      name = str(ctx.guild.name)
      description = str(ctx.guild.description)
      owner = str(ctx.guild.owner)
      id = str(ctx.guild.id)
      region = str(ctx.guild.region)
      memberCount = str(ctx.guild.member_count)
      icon = str(ctx.guild.icon_url)
      embed = discord.Embed(
          title=name + " Server Information",
          description=description,
          color=discord.Color.blue()
        )
      embed.set_thumbnail(url=icon)
      embed.add_field(name="Owner", value=owner, inline=True)
      embed.add_field(name="Server ID", value=id, inline=True)
      embed.add_field(name="Region", value=region, inline=True)
      embed.add_field(name="Member Count", value=memberCount, inline=True)
      await ctx.channel.send(embed=embed)
    else:
      await ctx.channel.send("This is a premium command")



#tells in console if cog has been loaded
def setup(bot):
    bot.add_cog(premium(bot))
    cprint(colored("""Cog: premium
Status: Loaded""", __colors__.blue))