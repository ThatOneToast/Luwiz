
import os, sys, termcolor, discord, asyncio, random, time, datetime, tinydb,json
from termcolor import colored 
from termcolor import cprint 
from discord.ext import commands
from discord.ext.commands import Bot
from discord.utils import get
from discord.ext import tasks
from discord.ext.tasks import loop
from modules import __classes__
from discord.ext.commands import BucketType, cooldown, CommandOnCooldown
from tinydb import TinyDB, Query

__colors__ = __classes__.__colors__
__attributes__ = __classes__.__attributes__
__highlights__ = __classes__.__highlights__
#Starts cog
class profanity(commands.Cog):
  def __init__(self,bot):
      self.bot = bot










  @commands.command()
  @commands.has_permissions(administrator = True)
  async def profanity(self,ctx, input):

    if input == "true":
      with open("profanity.json", "r") as f:
        profanityList = json.load(f)

      profanityList[str(ctx.guild.id)] = input

      with open("profanity.json", "w") as f:
        json.dump(profanityList,f)    

      embed=discord.Embed(title=f"Profanity is now {input}", description=f"Profanity is now {input} by {ctx.author}", colour=0x30e40b)
      await ctx.send(embed=embed)

    if input == "false":
      with open("profanity.json", "r") as f:
        profanityList = json.load(f)

      profanityList[str(ctx.guild.id)] = input

      with open("profanity.json", "w") as f:
        json.dump(profanityList,f)    

      embed=discord.Embed(title=f"Profanity is now {input}", description=f"Profanity is now {input} by {ctx.author}", colour=0x30e40b)
      await ctx.send(embed=embed)


    else:
      await ctx.channel.send("profanity can only be **true** or **false**")


  @commands.command()
  @commands.has_permissions(administrator = True)
  async def banword(self,ctx,inputword):
    with open("profanitywords.json", "r")as f:
      profanitywords = json.load(f)
    
    if inputword in profanitywords:
      await ctx.channel.send(f"{inputword} is already blacklisted")
    else:
      profanitywords[str(ctx.guild.id)] = inputword

    with open("profanitywords.json","w")as f:
      json.dump(profanitywords,f)



  @commands.Cog.listener
  async def on_message(self,message):
    with open("profanitywords.json","r")as f:
      words = json.load(f)
  
    if words[str(message.guild.id)] in message.content:
      await message.delete
      await message.channel.send("Sorry, that word is **blacklisted** in this server.")
    await self.bot.process_commands(message)





def setup(bot):
    bot.add_cog(profanity(bot))
    cprint(colored("""Cog: profanity
Status: Loaded""", __colors__.blue))