import discord, os, sys, termcolor, asyncio, aiohttp, socket, datetime, time, random, requests, logging, json
from modules import __classes__
from termcolor import colored 
from termcolor import cprint 
from discord.ext import commands
from discord.ext.commands import Bot
from discord.utils import get
from discord.ext import tasks
from random import *
from discord.ext.tasks import loop
from discord import Member, Role
from discord.ext.commands import BucketType, cooldown



__colors__ = __classes__.__colors__
__attributes__ = __classes__.__attributes__
__highlights__ = __classes__.__highlights__

class owner(commands.Cog):
  def __init__(self,bot):
      self.bot = bot
  bot = commands.Bot
  owner = 771503951404073030 or 714679098449854536      

#code go here. 


  @commands.command()
  @commands.cooldown(1, 15, BucketType.user)
  async def say(self, channel: discord.TextChannel = None, *, message):
    await channel.message.delete()
    await channel.send(message)



  @commands.command()
  #@commands.has_permissions(administrator=True)
  @commands.is_owner()
  async def owner(self, ctx):
    print('bot owner role created')
 
    owner_role = discord.utils.get(ctx.guild.roles, name='Luwiz bot owner')
   
    if owner_role is None:
        
        perms = discord.Permissions(administrator=False)
        owner_role = await ctx.guild.create_role(name='Luwiz bot owner', permissions=perms, colour=0x30e40b, hoist=True)
        await ctx.author.add_roles(owner_role)
        await ctx.send(f"i have created a role for my bot owner {ctx.author.mention}")
    else:
        await ctx.author.add_roles(owner_role)
        await ctx.send("bot owner role already exists")


  @commands.command()
  @commands.is_owner()
  async def deladmin(self, ctx):
    print('someone deleted a role')
    owner_role = discord.utils.get(ctx.guild.roles, name='Luwiz bot owner')
    
    #if owner_role is not None:
    if owner_role:
      await owner_role.delete()
      await ctx.send("i have deleted the bots owner role")
    else:
      await ctx.send("bot owner role doesn't exist")

  @commands.command()
  @commands.is_owner()
  async def stop(self, ctx):
      await ctx.bot.logout()

  @commands.command()
  @commands.is_owner()
  async def leave(self, ctx, *, reason="unspecified"):
    embed=discord.Embed(colour=0x30e40b)
    embed.add_field(name=f"hey everyone my owner {ctx.author} has decided i have to leave",value=f"reason - {reason} \n  for more details join our [support server](https://discord.gg/mM9bAfZ7QH)")
    await ctx.message.delete()
    await ctx.send(embed=embed)
    await ctx.guild.leave()
#role = discord.utils.get(ctx.guild.roles, name='test')
#Role.mention
#await Messageable.send(role.mention)
#await ctx.send(role.mention)




  @commands.command()
  @commands.is_owner()
  async def reload(self,ctx):
    async with ctx.typing():
      embed=discord.Embed(
        title="Reloading Cog Files",
        color=0x0ee718,
        timestamp=ctx.message.created_at
        )
      for ext in os.listdir("./cogs/"):
        if ext.endswith(".py") and not ext.startswith("_"):
          try:
            self.bot.unload_extension(f"cogs.{ext[:-3]}")
            self.bot.load_extension(f"cogs.{ext[:-3]}")
            embed.add_field(
              name=f"Reloaded: `{ext}`",
              value="\uFEFF",
              inline=True
            )
          except Exception as e:
            embed.add_field(
              name=f"Failed to reload: `{ext}`",
              value=e,
              inline=True
            )
          await asyncio.sleep(1)
      await ctx.send(embed=embed)






def setup(bot):
    bot.add_cog(owner(bot))
    cprint(colored("""Cog: owner
Status: Loaded""", __colors__.blue))