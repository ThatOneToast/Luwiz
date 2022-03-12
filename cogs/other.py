# -*- coding: utf-8 -*-
import os, sys, termcolor, discord, asyncio, random, time, datetime,json, requests
from termcolor import colored 
from termcolor import cprint 
from discord.ext import commands
from discord.ext.commands import Bot
from discord.utils import get
from discord.ext import tasks
from discord.ext.tasks import loop
from modules import __classes__
from discord.ext.commands import BucketType, cooldown, CommandOnCooldown

import mojang
from mojang import MojangAPI


__colors__ = __classes__.__colors__
__attributes__ = __classes__.__attributes__
__highlights__ = __classes__.__highlights__
#Starts cog
class other(commands.Cog):
  def __init__(self,bot):
      self.bot = bot

  @commands.command()
  async def pfp(self, ctx, member: discord.Member=None):
    if member is None: 
      with open("prefixes.json", "r") as f:
        prefixes = json.load(f)
      embed = discord.Embed(color=discord.Colour.blue())
      embed.add_field(name=f"Showing Avatar For ****{ctx.author.name}****", value="Avatar")
      embed.set_image(url=ctx.author.avatar_url)
      embed.set_footer(text=f"If you would like to show someone elses pfp, Do {prefixes[str(ctx.guild.id)]}pfp @example")
      await ctx.send(embed=embed)
    else:
      embed = discord.Embed(color=discord.Colour.green())
      embed.add_field(name=f"Showing Avatar For ****{member.name}****", value="Avatar")
      embed.set_image(url=member.avatar_url)
      await ctx.send(embed=embed)

  @commands.command()
  async def ping(self, ctx):
    embed=discord.Embed(title=f"bot latency", description=f"{round(self.bot.latency * 1000)}ms", colour=0x0e0ff3)
    #await ctx.send(f"Pong! {round(self.bot.latency * 1000)}ms")
    await ctx.send(embed=embed)




  

#Hypixel API Stuff













  @commands.command()
  async def hypixel(self,ctx,username,gamemode):
    uuid = MojangAPI.get_uuid(username)
    requestlink = str("https://api.hypixel.net/player?key=820ca8a6-1856-4673-a48f-fdc01e82c28f&uuid="+uuid)
    hydata = requests.get(requestlink).json()
    player = hydata["player"]["displayname"]



    if "rank" in hydata["player"] and not hydata["player"]["rank"] == "NORMAL":
      rank = hydata["player"]["rank"]
    elif "monthlyPackageRank" in hydata["player"] and not hydata["player"]["monthlyPackageRank"] == "NONE":
        rank = hydata["player"]["monthlyPackageRank"]
    elif "newPackageRank" in hydata["player"]:
        rank = hydata["player"]["newPackageRank"]
    elif "packageRank" in hydata["player"]:
        rank = hydata["player"]["packageRank"]
    else:
      rank = None



    karma = hydata["player"]["karma"]
    karma = "{:,}".format(karma)

    bw = hydata["player"]["stats"]["Bedwars"]
    bedwars = hydata["player"]["stats"]["Bedwars"]["games_played_bedwars"]
    bedwars1 = hydata["player"]["stats"]["Bedwars"]["wins_bedwars"]
    bedwars2 = hydata["player"]["stats"]["Bedwars"]["losses_bedwars"]
    bedwars3 = hydata["player"]["stats"]["Bedwars"]["wins_bedwars"]/hydata["player"]["stats"]["Bedwars"] ["losses_bedwars"]
    bedwars4 = bw["kills_bedwars"]
    bedwars5 = bw["deaths_bedwars"]
    bedwars6 = bw["kills_bedwars"]/bw["deaths_bedwars"]
    bedwars7 = bw["final_deaths_bedwars"]
    bedwars8 = bw["final_kills_bedwars"]
    d = hydata["player"]["stats"]["Duels"]
    duels = d["games_played_duels"]
    duels1 = d["op_duel_rounds_played"]
    duels2 = d["op_duel_damage_dealt"]
    duels3 = d["current_op_winstreak"]
    duels4 = d["op_duel_deaths"]
    duels5 = d["op_duel_kills"]
    duels6 = d["op_doubles_deaths"]
    duels7 = d["op_doubles_kills"]
    duels8 = d["op_doubles_rounds_played"]
    duels9 = d["op_doubles_wins"]
    duels10 = d["op_doubles_losses"]
    duels11 = d["best_op_winstreak"]
    duels12 = d["op_doubles_wins"]/d["op_doubles_losses"]
    duels13 = d["duels_winstreak_best_op_doubles"]
    duels14 = d["current_winstreak_mode_op_doubles"]


    if gamemode == "info":
      embed = discord.Embed(color=discord.Colour.green())
      embed.add_field(name=f"__****[{rank}]{player}****__ Karma:",value=f"""****{karma}**** points!""")
      await ctx.channel.send(embed=embed)
    


    elif gamemode == "bedwars":
      embed = discord.Embed(color=discord.Colour.green())
      embed.add_field(name=f"Showing bedwars stats for {player}", value=f"""
       \n bedwars games played >>> ****{bedwars}**** 
       \n bedwars games won >>> ****{bedwars1}****
       \n bedwars games lost >>> ****{bedwars2}****
       \n Bedwars Win/Loss ratio >>> ****{bedwars3}****
       \n Bedwars kills >>> ****{bedwars4}****
       \n Bedwars Deaths >>> ****{bedwars5}****
       \n Bedwars Kills/Deaths >>> ****{bedwars6}****
       \n Bedwars finial deaths >>> ****{bedwars7}****
       \n Bedwars final kills >>> ****{bedwars8}****
      """)
      await ctx.channel.send(embed=embed)
      


    if gamemode == "duels":
      embed = discord.Embed(color=discord.Colour.green())
      embed.add_field(name=f"OP Duels stats >> {player}", value=f"""
      \nOP duels games played >>> ****{duels1}****
      \nOP duels damage dealt >>> ****{duels2}****
      \nOP duels winstreak >>> ****{duels3}****
      \nOP duels kills >>> ****{duels5}****
      \nOP duels deaths >>> ****{duels4}****
      \nOP duels K/D >>> ****{duels5/duels4}****
      \nOP duels best winstreak >>> ****{duels11}****
      """)
      embed.add_field(name=f"OP Duels Doubles stats >> {player}", value=f"""
      \nOP Doubles played >>> ****{duels8}****
      \nOP Doubles wins >>> ****{duels9}****
      \nOP Doubles losses >>> ****{duels10}****
      \nOP Doubles W/L >>> ****{duels12}****
      \nOP Doubles best winstreak >>> ****{duels13}****
      \nOP Doubles winstreak >>> ****{duels14}****
      \nOP Doubles kills >>> ****{duels7}****
      \nOP Doubles deaths >>> ****{duels6}****
      \nOP Doubles K/D >>> ****{duels7/duels6}****
      """)
      await ctx.channel.send(embed=embed)







def setup(bot):
    bot.add_cog(other(bot))
    cprint(colored("""Cog: other
Status: Loaded""", __colors__.blue))