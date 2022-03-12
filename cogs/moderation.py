# -*- coding: utf-8 -*-
import discord
import os, sys, termcolor, asyncio, random, time, datetime
from termcolor import colored 
from termcolor import cprint 
from discord.ext import commands
from discord.ext.commands import Bot
from discord.utils import get
from discord.ext import tasks
from discord.ext.tasks import loop
from random import *
from modules import __classes__
from discord.ext.commands import BucketType, cooldown, CommandOnCooldown,has_permissions


__colors__ = __classes__.__colors__
__attributes__ = __classes__.__attributes__
__highlights__ = __classes__.__highlights__
#Starts cog
class moderation(commands.Cog):
  def __init__(self,bot):
      self.bot = bot

#have someone set a prefix and get prefix




#mute and unmute commands workind <----Working on temp mutes----->
  @commands.command()
  @commands.has_permissions(manage_messages=True)
  async def unmute(self, ctx, member: discord.Member):
    mutedRole = discord.utils.get(ctx.guild.roles, name="Muted")

    await member.remove_roles(mutedRole)
    embed = discord.Embed(title=f"{member} was unmuted by {ctx.author}", colour=0x0ef3f0)
    embed.set_author(name="unmute command 🔈 ", icon_url=member.avatar_url)
    await ctx.send(embed=embed)
  





  @commands.command()
  @commands.has_permissions(manage_messages=True)
  async def mute(self, ctx, member: discord.Member, *, reason = "unspecified"):
    guild = ctx.guild
    mutedRole = discord.utils.get(guild.roles, name = "Muted")
    
    if not mutedRole:
      mutedRole = await guild.create_role(name = "Muted", colour=0x070606)

      for channel in guild.channels:
        await channel.set_permissions(mutedRole, speak = False, send_messages = False, read_message_history = False, read_messages = True)
    await member.add_roles(mutedRole, reason = reason) 
    embed = discord.Embed(title=f"{member} was muted by {ctx.author}", colour=0xf10a0a)
    embed.set_author(name="mute command", icon_url=member.avatar_url)
    embed.add_field(name=f"reason - {reason}", value="🔇")
    await ctx.send(embed=embed)
#\u200b ctx.author



  @commands.Cog.listener()
  async def on_member_join(self, member):
    if member.guild.id == 839307082503159859:
      join_role = discord.utils.get(member.guild.roles, name='Member')
      await member.add_roles(join_role)
      






#ban command and kick command
  @commands.command()
  @commands.has_permissions(ban_members=True)
  async def ban(self, ctx, member: discord.Member=None):
    embed = discord.Embed(color= discord.Color.red(), timestamp=ctx.message.created_at)
    embed.add_field(name="Luwiz BanHammer", value="****{}**** was banned" .format(member.name), inline=False)
    await ctx.send(embed=embed)
    await member.ban()


  @commands.command()
  @commands.has_permissions(kick_members=True)
  async def kick(self, ctx, member: discord.Member=None,*, reason = "unspecified"):
    #embed = discord.Embed(color= discord.Color.red(), timestamp=ctx.message.created_at)
    #embed.add_field(name='Luwiz: Kick', value='**{}** was kicked'.format(member.name), inline=False)
    embed=discord.Embed(color= discord.Color.red(), timestamp=ctx.message.created_at)
    embed.add_field(name=f"{member} was kicked by {ctx.author}", value=f"reason: - {reason}")
    await ctx.send(embed=embed)
    await member.kick()
#make sure bot role is higher than muting person role

    #embed1 = discord.Embed()
    #embed1.set_author(name="mute command", icon_url=member.avatar_url)
    #embed1.add_field(name=f"reason", value="dd")
    #await member.send(f"You kicked from {guild.name} for {reason}")
    #embed1.add_field(f"You kicked from {guild.name} by {ctx.author}", value="{reason}")
    #await ctx.send(embed1=embed1)



  @commands.command()
  @commands.has_permissions(administrator=True)
  @commands.cooldown(1, 5, BucketType.guild)
  async def embed(self, ctx, *, message):
    await ctx.message.delete()
    embed = discord.Embed(color= discord.Color.light_gray())
    embed.set_author(name="Luwiz Embeder")
    embed.add_field(name=f"{ctx.author} embeded", value=f"{message}")
    message = await ctx.channel.send(embed=embed)
    await ctx.message.delete()



  @commands.command()
  @commands.has_permissions(kick_members=True)
  @commands.cooldown(1, 2, BucketType.guild)
  async def warn(self, ctx, member, *, reason = "unspecified"):
    await ctx.message.delete()
    embed = discord.Embed(colour=0xeba309)
    #embed.set_author(name="Luwiz mod warner")
    embed.add_field(name="Luwiz mod warner", value=f"{ctx.author.mention} warned {member}\n reason - {reason}")
    #embed.add_field(name=f"Staff Warn", value=f"{ctx.author.mention}")
    await ctx.channel.send(embed=embed)




  #@commands.Cog.listener()
  #async def on_guild_join(self, ctx):
    #await ctx.send('welcome')



  @commands.command()
  @commands.has_permissions(manage_messages = True)
  async def purge(self, ctx, limit : int):
    await ctx.channel.purge(limit=limit+1)
    message = await ctx.send(f'I have purged {limit} messages')
    await asyncio.sleep(10)
    await message.delete()




  @commands.command()
  @commands.has_permissions(manage_messages=True)
  async def delay(self,ctx,seconds: int):
    await ctx.channel.edit(slowmode_delay=seconds)
    await ctx.send(f"{ctx.author} has changed the slowmode to {seconds}!")

  @commands.command()
  @commands.has_permissions(manage_messages=True)
  async def name(self,ctx,*,name):
    await ctx.channel.edit(name=name)
    await ctx.channel.send(f"{ctx.author.mention} has chganged the name to {name}")
  
  @commands.command()
  @commands.has_permissions(manage_messages=True)
  async def topic(self,ctx,*,description):
    await ctx.channel.edit(topic=description)
    await ctx.channel.send(f"{ctx.author.mention} has set the channel topic to {description}")

  @commands.command()
  @commands.has_permissions(manage_messages=True)
  async def vcmute(self, ctx, member: discord.Member):
    await member.edit(mute=True)


  @commands.command()
  @commands.has_permissions(manage_messages=True)
  async def vcunmute(self, ctx, member: discord.Member):
    await member.edit(mute=False)


#tells in console if cog has been loaded
def setup(bot):
    bot.add_cog(moderation(bot))
    cprint(colored("""Cog: Moderation
Status: Loaded""", __colors__.blue))