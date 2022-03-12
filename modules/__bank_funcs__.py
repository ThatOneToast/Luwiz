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
from pymongo import MongoClient


__colors__ = __classes__.__colors__
__attributes__ = __classes__.__attributes__
__highlights__ = __classes__.__highlights__
#Starts cog


class bankfuncs(commands.Cog):
  def __init__(self,bot):
    self.bot = bot



  auth_url = "mongodb+srv://cyhpactic:!LuwizBotIsCool@cluster0.1wjwo.mongodb.net/myFirstDatabase?retryWrites=true&w=majority"



  async def open_bank(user):
      cluster = MongoClient(auth_url)
      db = cluster["my_bot"]

      cursor = db["economy"]

      try:
          post = {"_id": user.id, "wallet": 5000, "bank": 0} # You can add as many columns as you can in this list !!!

          cursor.insert_one(post)

      except:
          pass


  async def get_bank_data(user):
      cluster = MongoClient(auth_url)
      db = cluster["my_bot"]

      cursor = db["economy"]

      user_data = cursor.find({"_id": user.id})

      cols = ["wallet", "bank"] # You can add as many columns as you can in this list !!!

      data = []

      for mode in user_data:
          for col in cols:
              data1 = mode[str(col)]

              data.append(data1)

      return data


  async def update_bank(user, amount=0, mode="wallet"):
      cluster = MongoClient(auth_url)
      db = cluster["my_bot"]

      cursor = db["economy"]

      cursor.update_one({"_id": user.id}, {"$inc": {str(mode): amount}})










def setup(bot):
    bot.add_cog(bankfuncs(bot))
    cprint(colored("""Cog: bankfuncs
Status: Loaded""", __colors__.blue))