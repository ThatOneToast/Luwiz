import os, sys, discord, termcolor, asyncio, datetime, time,json,random
from modules import __classes__
from modules import keep_alive
from termcolor import colored
from termcolor import cprint 
from discord.ext import commands
from discord.ext.commands import Bot
from discord.utils import get
from discord.ext import tasks
from discord.ext.tasks import loop
from discord import Member, Role
from discord.ext.commands import BucketType, cooldown, CommandOnCooldown
import traceback




# gets prefix from prefixes.json
async def get_prefix(client,message):

    with open("prefixes.json", "r") as f:
      prefixes = json.load(f)

    return prefixes[str(message.guild.id)]



x = datetime.datetime.now()
a = (x.strftime("%A"))
b = (x.strftime("%B"))
c = (x.strftime("%d"))
d = (x.strftime("%Y"))
e = (x.strftime("%I"))
f = (x.strftime("%M"))
g = (x.strftime("%S"))
h = (x.strftime("%p"))
y = (a + ", " + b + " " + c + ", " + d + "  " + e + ":" + f + "." + g + " " + h)
#defining classes
__colors__ = __classes__.__colors__
__attributes__ = __classes__.__attributes__
__highlights__ = __classes__.__highlights__
#__token__ = __classes__.__token__
__version__ = __classes__.__version__
__credits__ = __classes__.__credits__






#loads all cogs
def load_cogs():
  for file in os.listdir('cogs'):
      if file.endswith('.py') and not file.startswith('_'):
          bot.load_extension(f'cogs.{file[:-3]}')

#adds intents removes default help, and sets prefix
intents = discord.Intents.default()
intents.members = True
intents.presences = True
language = "en"
bot = commands.Bot(command_prefix = get_prefix, intents=intents, case_insensitive = True)

bot.remove_command('help')

os.system('clear')



@bot.event
async def on_guild_join(guild):
    with open("prefixes.json", "r") as f:
      prefixes = json.load(f)

    prefixes[str(guild.id)] = "!"

    with open("prefixes.json", "w") as f:
      json.dump(prefixes,f)

    with open("profanity.json", "r") as f:
      profanityList = json.load(f)

    profanityList[str(guild.id)] = False

    with open("profanity.json", "w") as f:
      json.dump(profanityList,f)

    with open("profanitywords.json","r") as f:
      profanitywords = json.load(f)

    profanitywords[str(guild.id)] = "blacklisted"

    with open("profanitywords.json","w") as f:
      json.dump(profanitywords,f)



@bot.command()
@commands.has_permissions(administrator = True)
async def changeprefix(ctx, prefix):

    with open("prefixes.json", "r") as f:
        prefixes = json.load(f)

    prefixes[str(ctx.guild.id)] = prefix

    with open("prefixes.json", "w") as f:
        json.dump(prefixes,f)    
    embed=discord.Embed(title=f"The prefix was changed to {prefix}", description=f"prefix changed by {ctx.author}", colour=0x30e40b)
    await ctx.send(embed=embed)

@bot.event
async def on_message(ctx):
  if 'luwiz' in ctx.content:
    with open("prefixes.json", "r") as f:
      prefixes = json.load(f)
    embed = discord.Embed(color= discord.Color.green(), timestamp=ctx.created_at)
    embed.add_field(name="Luwiz What Is The Prefix: ",value=f"Prefix Server: {prefixes[str(ctx.guild.id)]}")
    await ctx.channel.send(embed=embed)

#prints details about the bot, as well as Server noticies
@bot.event
async def on_ready():
  cprint(colored(__credits__.__credit__, __colors__.red, attrs = __attributes__.bold))
  cprint(colored("Bot v"+__version__.version, __colors__.green, attrs = __attributes__.bold))
  cprint(colored(f"""{y}
  """, __colors__.cyan))
  cprint(colored("""Logged in as: """, __colors__.magenta))
  cprint(colored(f"""{bot.user.name}""", __colors__.magenta))
  cprint(colored(f"""{bot.user.id}
  """, __colors__.magenta))
  cprint(colored("Discord v"+discord.__version__, __colors__.yellow))
  load_cogs()
  presence_change.start()
  cprint(colored("""________________________________________________
  """, __colors__.blue))     
  cprint(colored('Server List:', __colors__.yellow))
  for guild in bot.guilds:
    cprint(colored(guild.name,__colors__.green))
    




#This changes the status of our bot

@loop(seconds=60)
async def presence_change():
  #pause = 15
  await bot.change_presence(activity=discord.Game(f"This bot is no longer being maintained!"))





@bot.command()
async def mimic(ctx, member: discord.Member, *, message=None):
  if ctx.author.id == 714679098449854536:
    webhook = await ctx.channel.create_webhook(name=member.name)
    await webhook.send(
    str(message), username=member.name, avatar_url=member.avatar_url)
    await ctx.message.delete()

    webhooks = await ctx.channel.webhooks()
    for webhook in webhooks:
      await webhook.delete()








#starts the bot and keeps it alive :)

keep_alive.keep_alive()

my_secret = os.environ['TOKEN']
bot.run(os.getenv('TOKEN'))