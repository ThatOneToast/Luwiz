#!dice# -*- coding: utf-8 -*-
import os, sys, discord, termcolor, asyncio, aiohttp, socket, datetime, time, random, requests, logging, json
from modules import __classes__
from termcolor import colored 
from termcolor import cprint 
from discord.ext import commands
from discord.ext.commands import Bot
from discord.utils import get
from discord.ext import tasks
from discord.ext.commands import BucketType, cooldown, CommandOnCooldown
from discord.ext.tasks import loop
from discord import Member, Role

__colors__ = __classes__.__colors__
__attributes__ = __classes__.__attributes__
__highlights__ = __classes__.__highlights__

class Games(commands.Cog):
  def __init__(self,bot):
      self.bot = bot
      






  @commands.command()
  @commands.cooldown(1, 10, BucketType.user)
  async def dice(self, ctx):
    one = "You rolled a...**1**!"
    two = "You rolled a...**2**!"
    three = "You rolled a...**3**!"
    four = "You rolled a...**4**!"
    five = "You rolled a...**5**!"
    six = "You rolled a...**6**!"
    foo = [one, two, three, four, five, six]
    embed = discord.Embed(
    title = 'Dice Roll',
    description = random.choice(foo),
    color = discord.Color.blue())
    embed.set_author(name='Luwiz')
    await ctx.send(embed=embed)
    
  @commands.command()
  @commands.cooldown(1, 15, BucketType.user)
  async def draw(self, ctx):
    foo = ["You drew a...3 of :diamonds:",
              "You drew a...3 of :hearts:",
              "You drew a...3 of :clubs:",
              "You drew a...3 of :spades:",
              "You drew a...4 of :diamonds:",
              "You drew...4 of :hearts:",
              "You drew a...4 of :clubs:",
              "You drew a...4 of :spades:",
              "You drew a...5 of :diamonds:",
              "You drew a...5 of :hearts:",
              "You drew a...5 of :clubs:",
              "You drew a...5 of :spades:",
              "You drew a...6 of :diamonds:",
              "You drew a...6 of :hearts:",
              "You drew a...6 of :clubs:",
              "You drew a...6 of :spades:",
              "You drew a...7 of :diamonds:",
              "You drew a...7 of :hearts:",
              "You drew a...7 of :clubs:",
              "You drew a...7 of :spades:",
              "You drew a...8 of :diamonds:",
              "You drew a...8 of :hearts:",
              "You drew a...8 of :clubs:",
              "You drew a...8 of :spades:",
              "You drew a...9 of :diamonds:",
              "You drew a...9 of :hearts:",
              "You drew a...9 of :clubs:",
              "You drew a...9 of :spades:",
              "You drew a...10 of :diamonds:",
              "You drew a...10 of :hearts:",
              "You drew a...10 of :clubs:",
              "You drew a...10 of :spades:",
              "You drew a...J of :diamonds:",
              "You drew a...J of :hearts:",
              "You drew a...J of :clubs:",
              "You drew a...J of :spades:",
              "You drew a...Q of :diamonds:",
              "You drew a...Q of :hearts:",
              "You drew a...Q of :clubs:",
              "You drew a...Q of :spades:",
              "You drew a...K of :diamonds:",
              "You drew a...K of :hearts:",
              "You drew a...K of :clubs:",
              "You drew a...K of :spades:",
              "You drew a...A of :diamonds:",
              "You drew a...A of :hearts:",
              "You drew a...A of :clubs:",
              "You drew a...A of :spades:",
              "You drew a...2 of :diamonds:",
              "You drew a...2 of :hearts:",
              "You drew a...2 of :clubs:",
              "You drew a...2 of :spades:"]
    embed = discord.Embed(title = 'Card Draw', 
    description = random.choice(foo), 
    color = discord.Color.blue())
    embed.set_author(name='Luwiz')
    await ctx.send(embed=embed)

  @commands.command()
  @commands.has_permissions(administrator=True)
  @commands.cooldown(1, 3, BucketType.user)
  async def bingo(self, ctx):
    await ctx.message.delete()
    foo = ["0",
    "1",
    "2",
    "3",
    "4",
    "5",
    "6",
    "7",
    "8",
    "9",
    "10",
    "11",
    "12",
    "13",
    "14",
    "15",
    "16",
    "17",
    "18",
    "19",
    "20",
    "21",
    "22",
    "23",
    "24",
    "25",
    "26",
    "27",
    "28",
    "29",
    "30",
    "31",
    "32",
    "33",
    "34",
    "35",
    "36",
    "38",
    "39",
    "40",
    "41",
    "42",
    "43",
    "44",
    "45",
    "46",
    "47",
    "48",
    "49",
    "51",
    "52",
    "53",
    "54",
    "55",
    "56",
    "57",
    "58",
    "59",
    "60",
    "61",
    "62",
    "63",
    "64",
    "65",
    "66",
    "67",
    "68",
    "69",
    "70",
    "72",
    "73",
    "74",
    "75",
    "76",
    "77",
    "78",
    "79",
    "80",
    "81",
    "82",
    "83",
    "84",
    "85",
    "86",
    "87",
    "88",
    "89",
    "90",
    "91",
    "92",
    "93",
    "94",
    "95",
    "96",
    "97",
    "98",
    "99",
    "100"]
    embed = discord.Embed(title = 'Bingo Picker', 
    description = random.choice(foo), 
    color = discord.Color.blue())
    embed.set_author(name='Luwiz')
    await ctx.send(embed=embed)

  @commands.command()
  @commands.has_permissions(administrator=True)
  @commands.cooldown(1, 15, BucketType.user)
  async def sbingo(self, ctx):
    await ctx.message.delete()
    embed = discord.Embed(color=discord.Colour.blue())
    embed.set_author(name="This is the start of the bingo game")
    embed.add_field(name="Bingo", value= "[Bingo](https://docs.google.com/document/d/1vCmPYWq-RdjOgovlI6YOaQvv0pz3BzMnujjvgAJwieY/edit?usp=sharing)")
    embed.add_field(name="How To", value="Make a copy of this document and place numbers in spaces 1-100")
    await ctx.send(embed=embed)


  @commands.command()
  @commands.cooldown(1, 30, BucketType.user)
  async def kill(self, ctx, member: discord.Member=None):
    foo = [f"You stabbed {member.mention} 140 times in the back",
    f"You suffocated {member.mention} with a plastic bag",
    f"You shot {member.mention} 12 times in the skull",
    f"You dunmped {member.mention} in a bucket of acid",
    f"You gave {member.mention} a heart attack ",
    f"{ctx.author.mention} has thrown {member.mention} off a plane",
    f"You beat {member.mention} with a baseball bat 12 times",
    f"You bashed {member.mention} there skull in",
    f"You ran {member.mention} over with a semi truk",
    f"{ctx.author.mention} threw {member.mention} down the stairs",
    f"{member.mention} tripped and died",]
    embed = discord.Embed(title = 'Sentance death', 
    description = random.choice(foo), 
    color = discord.Color.blue())
    embed.set_author(name='Luwiz')
    await ctx.send(embed=embed)






  @commands.command()
  @commands.cooldown(1, 10, BucketType.user)
  async def number(self, ctx):
    foo = ["0",
    "1",
    "2",
    "3",
    "4",
    "5",
    "6",
    "7",
    "8",
    "9",
    "10",
    "11",
    "12",
    "13",
    "14",
    "15",
    "16",
    "17",
    "18",
    "19",
    "20",
    "21",
    "22",
    "23",
    "24",
    "25",
    "26",
    "27",
    "28",
    "29",
    "30",
    "31",
    "32",
    "33",
    "34",
    "35",
    "36",
    "38",
    "39",
    "40",
    "41",
    "42",
    "43",
    "44",
    "45",
    "46",
    "47",
    "48",
    "49",
    "51",
    "52",
    "53",
    "54",
    "55",
    "56",
    "57",
    "58",
    "59",
    "60",
    "61",
    "62",
    "63",
    "64",
    "65",
    "66",
    "67",
    "68",
    "69",
    "70",
    "72",
    "73",
    "74",
    "75"]
    embed = discord.Embed(title = 'Number draw out of 75', 
    description = random.choice(foo), 
    color = discord.Color.blue())
    embed.set_author(name='Scooper Rooper')
    await ctx.send(embed=embed)
      








    








def setup(bot):
    bot.add_cog(Games(bot))
    cprint(colored("""Cog: Games
Status: Loaded""", __colors__.blue))