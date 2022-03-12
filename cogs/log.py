# -*- coding: utf-8 -*-
import os, sys, termcolor, discord, asyncio, random, time, datetime
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
class log(commands.Cog):
  def __init__(self,bot):
      self.bot = bot





#Mod logging Stuff(s) - currently only working for my server :). sorry :(


  @commands.Cog.listener()
  async def on_command_error(self, ctx, error):
    if isinstance(error, commands.errors.CommandOnCooldown):
     embed = discord.Embed(
       title = 'Cooldown Timer',
       description = f'try again in {error.retry_after:,.2f} seconds',
       color = discord.Color.blue())
     embed.set_author(name='Luwiz')
     await ctx.send(embed=embed)
    else:
      raise error





  @commands.Cog.listener()
  async def on_command_error(self,ctx,error):
    if isinstance(error,discord.errors.Forbidden):
      print(f"{ctx.guild} has triggeren an error")
    else:
      raise error








#tells in console if cog has been loaded
def setup(bot):
    bot.add_cog(log(bot))
    cprint(colored("""Cog: log
Status: Loaded""", __colors__.blue))