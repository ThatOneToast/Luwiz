# -*- coding: utf-8 -*-
import os, sys, termcolor, discord, asyncio, random, json
from termcolor import colored 
from termcolor import cprint  
from discord.ext import commands
from discord.ext.commands import Bot
from discord.utils import get
from discord.ext import tasks
from discord.ext.tasks import loop
from modules import __classes__
from pymongo import MongoClient
from discord.ext.commands import BucketType, cooldown, CommandOnCooldown


__colors__ = __classes__.__colors__
__attributes__ = __classes__.__attributes__
__highlights__ = __classes__.__highlights__
#Starts cog
class eco(commands.Cog):
  def __init__(self,bot):
      self.bot = bot


  




  async def update_data(self,users, user):

    if not f'{user.id}' in users:
      users[f'{user.id}'] = {}
      users[f'{user.id}']['experience'] = 0
      users[f'{user.id}']['level'] = 1


  async def add_experience(self,users, user, exp):
    users[f'{user.id}']['experience'] += exp


  async def level_up(self,users, user, message):
      with open('levels.json', 'r') as g:
        levels = json.load(g)
      experience = users[f'{user.id}']['experience']
      lvl_start = users[f'{user.id}']['level']
      lvl_end = int(experience ** (1 / 4))
      if lvl_start < lvl_end:
        await message.channel.send(f'{user.mention} has leveled up to level {lvl_end}')
        users[f'{user.id}']['level'] = lvl_end
        await asyncio.sleep(3)
        await message.delete()





  @commands.command()
  @commands.has_permissions(administrator=True)
  async def levelStop(self,ctx):
    with open("levelBlacklist.txt",'w') as f:
      f.write(f"{ctx.guild.id}\n")


      
  @commands.Cog.listener()
  async def on_member_join(self,member):
    with open('users.json', 'r') as f:
      users = json.load(f)

    await self.update_data(users, member)

    with open('users.json', 'w') as f:
      json.dump(users, f)


  @commands.Cog.listener()
  async def on_message(self,message):
    if message.guild.id == 438848185008390158:
      return

    else:
      with open('users.json', 'r') as f:
        users = json.load(f)

      await self.update_data(users, message.author)
      await self.add_experience(users, message.author, random.randint(15,25))
      await self.level_up(users, message.author, message)

      with open('users.json', 'w') as f:
        json.dump(users, f)

    if message.author.bot:
      return
    
    await self.bot.process_commands(message)



  

  @commands.command(aliases=['rank'])
  async def level(self,ctx, member: discord.Member = None):
    if not member:
      id = ctx.message.author.id
      with open('users.json', 'r') as f:
        users = json.load(f)
      lvl = users[str(id)]['level']
      embed = discord.Embed(color= discord.Color.gold())
      embed.set_author(name="Luwiz Leveling System")
      embed.add_field(name=f"{ctx.author}", value=f"Your Discord Chatting Level Is At: ****{lvl}****")
      message = await ctx.channel.send(embed=embed)
    else:
      id = member.id
      with open('users.json', 'r') as f: 
        users = json.load(f)
      lvl = users[str(id)]['level']
      embed = discord.Embed(color= discord.Color.gold())
      embed.set_author(name="Luwiz Leveling System")
      embed.add_field(name=f"{member}", value=f"is at a discord chatting level of: ****{lvl}****")
      await ctx.channel.send(embed=embed)










































































  @commands.command()
  @commands.has_permissions(administrator=True)
  async def ecoStop(self,ctx):
    with open("rankBlacklist.txt",'w') as f:
      f.write(f"{ctx.guild.id}\n")





#Define here
  async def open_account(self, user):
    users = await self.get_bank_data()




    if str(user.id) in users:
      return False
    else:

      users[str(user.id)] = {}
      users[str(user.id)]["wallet"] = 0
      users[str(user.id)]["bank"] = 1000

    with open("mainbank.json", "w") as f:
      json.dump(users,f)

    return True



#Define here
  async def get_bank_data(self):
    with open("mainbank.json", "r") as f:
      users = json.load(f)
      return users






  @commands.command()
  async def withdraw(self,ctx,amount = None):
    await self.open_account(ctx.author)

    if amount == None:
      await ctx.send("ATM: I need an amount to withdraw.")
      return

    bal = await self.update_bank(ctx.author)

    amount = int(amount)

    if amount>bal[1]:
      await ctx.send("ATM: You don't have enough funds")
      return
    if amount<1000:
      await ctx.send("ATM: I'm sorry! As a security policy, you're not allowed to withdraw putting you under 1,000$")
      return

    await self.update_bank(ctx.author,amount, "wallet")
    await self.update_bank(ctx.author,-1*amount, "bank")

    await ctx.send(f"{ctx.author} withdrew ****💰{amount}💰****")







  @commands.command(aliases=['depo'])
  async def deposit(self,ctx,amount = None):
    await self.open_account(ctx.author)

    if amount == None:
      await ctx.send("ATM: I need an amount to deposit.")
      return
    bal = await self.update_bank(ctx.author)

    amount = int(amount)

    if amount>bal[0]:
      await ctx.send("ATM: You don't have enough funds💰")
      return
    if amount<0:
      await ctx.send("ATM: Amount must be positive!")
      return

    await self.update_bank(ctx.author,-1*amount)
    await self.update_bank(ctx.author,amount, "bank")

    await ctx.send(f"{ctx.author} deposited {amount} 💰")





  @commands.command()
  async def pay(self, ctx, member:discord.Member, amount = None):
    await self.open_account(ctx.author)
    await self.open_account(member)

    if amount == None:
      await ctx.send("Please enter an amount")
      return
    bal = await self.update_bank(ctx.author)

    amount = int(amount)

    if amount>bal[1]:
      await ctx.send("You don't have enough funds")
      return
    if amount<0:
      await ctx.send("Amount must be positive!")
      return

    await self.update_bank(ctx.author,-1*amount, "bank")
    await self.update_bank(member,amount, "bank")

    await ctx.send(f"you paid {member.name} ****💰{amount}💰****")





  @commands.command(aliases=['Slot','bet'])
  @commands.cooldown(1, 30, BucketType.user)
  async def slots(self,ctx,amount = None):
    await self.open_account(ctx.author)

    if amount == None:
      await ctx.send("Please enter an amount to withdraw")
      return
    bal = await self.update_bank(ctx.author)

    amount = int(amount)
    if amount>bal[0]:
      await ctx.send("You don't have enough funds")
      return
    if amount<0:
      await ctx.send("Amount must be positive!")
      return

    final = []
    for i in range(3):
      a = random.choice(["💩","👺","🤡","😏","😇","/", "🎃", "👽", "🤑", "👋", "👀", "😱"])
      final.append(a)
    await ctx.send(str(final))

    if final[0] == final[1] or final[0] == final[2] or final[2] == final[1]:
      await self.update_bank(ctx.author,2*amount, "bank")
      await ctx.send("you won DOUBLE!!!")
    else:
      await self.update_bank(ctx.author,-1*amount, "bank")
      await ctx.send("You lost what a bumber try again :)")





  @commands.command(aliases=['balance', 'money', 'credits', 'coins'])
  async def bal(self, ctx):
    await self.open_account(ctx.author)
    users = await self.get_bank_data()

    wallet_amt = users[str(ctx.author.id)]["wallet"]
    bank_amt = users[str(ctx.author.id)]["bank"]

    embed = discord.Embed(title=f"{ctx.author.name}'s balance ", color = discord.Color.gold())
    embed.add_field(name="wallet balance", value = f"💰{wallet_amt}💰")
    embed.add_field(name="bank balance", value = f"💰{bank_amt}💰")
    await ctx.send(embed=embed)



  async def update_bank(self,user,change = 0,mode = "wallet"):
    users = await self.get_bank_data()
    users[str(user.id)][mode] += change

    with open("mainbank.json", "w") as f:
      json.dump(users,f)

    bal = [users[str(user.id)]["wallet"], users[str(user.id)]["bank"]]
    return bal


  @commands.command()
  @commands.cooldown(1, 300, BucketType.user)
  async def beg(self, ctx):
    await self.open_account(ctx.author)
    users = await self.get_bank_data()
    earnings = random.randrange(401)
    await ctx.send(f"Someone gave you 💰****${earnings}****💰")
    users[str(ctx.author.id)]["wallet"] += earnings
    with open("mainbank.json", "w") as f:
      json.dump(users,f)


  @commands.command()
  @commands.cooldown(1, 360, BucketType.user)
  async def rob(self,ctx,member:discord.Member):
    await self.open_account(ctx.author)
    await self.open_account(member)

    bal = await self.update_bank(member)

    if bal[0]<1000:
      await ctx.send("Robbing the poor isn't very nice of me 😇.")
      return

    earnings = random.randrange(0, bal[0])

    await self.update_bank(ctx.author, 1*earnings)
    await self.update_bank(member, -1*earnings)
    await ctx.send(f"{ctx.author.mention} robbed {member.mention} and got 💰****${earnings}****💰")



  @commands.Cog.listener()
  async def on_message(self,ctx):
    await self.open_account(ctx.author)
    users = await self.get_bank_data()
    earnings = random.randrange(75)
    users[str(ctx.author.id)]["wallet"] += earnings
    with open("mainbank.json", "w") as f:
      json.dump(users,f)





  mainshop =  [
                      {
                      "name":"TimeMachine", 
                      "price":100000000, 
                      "description":"Go back in time"},
                      {
                      "name":"Lambo", 
                      "price":850000, 
                      "description":"A fancy car"
                      },
                      {
                      "name":"robot", 
                      "price":340000, 
                      "description":"have someone cook, clean, and do everything for you"
                      },
                      {
                      "name":"Nuke", 
                      "price":704200, 
                      "description":"buy a nuke(fake)"
                      },
                      {
                      "name":"candy", 
                      "price":1, 
                      "description":"buy a piece of candy"
                      },
                      {
                      "name": "Helicopter",
                      "price": 5400000,
                      "description":"Buy a Helicopter"
                      }
              ]


  @commands.command()
  async def shop(self, ctx):
    embed = discord.Embed(title = "Money Shop",color = discord.Color(0xfa43ee))
    for item in self.mainshop:
      name = item["name"]
      price = item["price"]
      desc = item["description"]
      embed.add_field(name=name, value = f"${price} | {desc}")
    await ctx.send(embed=embed)


  @commands.command()
  async def buy(self, ctx, item, amount = 1):
    await self.open_account(ctx.author)

    res = await self.buy_this(ctx.author,item,amount)

    if not res[0]:
      if res[1]==1:
        await ctx.send("That Item isn't offerable")
        return
      if res[1]==2:
        await ctx.send(f"You don't have enough money your wallet to buy {amount}")
        return

    await ctx.send(f"you just bought {amount} {item}")


  async def buy_this(self,user,item_name,amount):
      item_name = item_name.lower()
      name_ = None
      for item in self.mainshop:
          name = item["name"].lower()
          if name == item_name:
              name_ = name
              price = item["price"]
              break

      if name_ == None:
          return [False,1]

      cost = price*amount

      users = await self.get_bank_data()

      bal = await self.update_bank(user)

      if bal[0]<cost:
          return [False,2]


      try:
          index = 0
          t = None
          for thing in users[str(user.id)]["bag"]:
              n = thing["item"]
              if n == item_name:
                  old_amt = thing["amount"]
                  new_amt = old_amt + amount
                  users[str(user.id)]["bag"][index]["amount"] = new_amt
                  t = 1
                  break
              index+=1 
          if t == None:
              obj = {"item":item_name , "amount" : amount}
              users[str(user.id)]["bag"].append(obj)
      except:
          obj = {"item":item_name , "amount" : amount}
          users[str(user.id)]["bag"] = [obj]        

      with open("mainbank.json","w") as f:
          json.dump(users,f)

      await self.update_bank(user,cost*-1,"wallet")

      return [True,"Worked"]

  @commands.command()
  async def bag(self,ctx):
      await self.open_account(ctx.author)
      user = ctx.author
      users = await self.get_bank_data()

      try:
          bag = users[str(user.id)]["bag"]
      except:
          bag = []


      em = discord.Embed(title = "Your inventory of items",color = discord.Color(0xfa43ee))
      for item in bag:
          name = item["item"]
          amount = item["amount"]

          em.add_field(name = name, value = amount)    

      await ctx.send(embed = em)  





  @commands.command()
  async def sell(self,ctx,item,amount = 1):
      await self.open_account(ctx.author)

      res = await self.sell_this(ctx.author,item,amount)

      if not res[0]:
          if res[1]==1:
              await ctx.send("That Object isn't there!")
              return
          if res[1]==2:
              await ctx.send(f"You don't have {amount} {item} in your bag.")
              return
          if res[1]==3:
              await ctx.send(f"You don't have {item} in your bag.")
              return

      await ctx.send(f"You just sold {amount} {item}.")

  async def sell_this(self,user,item_name,amount,price = None):
      item_name = item_name.lower()
      name_ = None
      for item in self.mainshop:
          name = item["name"].lower()
          if name == item_name:
              name_ = name
              if price==None:
                  price = 0.9* item["price"]
              break

      if name_ == None:
          return [False,1]

      cost = price*amount

      users = await self.get_bank_data()

      bal = await self.update_bank(user)


      try:
          index = 0
          t = None
          for thing in users[str(user.id)]["bag"]:
              n = thing["item"]
              if n == item_name:
                  old_amt = thing["amount"]
                  new_amt = old_amt - amount
                  if new_amt < 0:
                      return [False,2]
                  users[str(user.id)]["bag"][index]["amount"] = new_amt
                  t = 1
                  break
              index+=1 
          if t == None:
              return [False,3]
      except:
          return [False,3]    

      with open("mainbank.json","w") as f:
          json.dump(users,f)

      await self.update_bank(user,cost,"wallet")

      return [True,"Worked"]


  @commands.command(aliases = ["creditTop"])
  async def baltop(self, ctx, x = 10):
      users = await self.get_bank_data()
      leader_board = {}
      total = []
      for user in users:
          name = int(user)
          total_amount = users[user]["wallet"] + users[user]["bank"]
          leader_board[total_amount] = name
          total.append(total_amount)

      total = sorted(total,reverse=True)    

      em = discord.Embed(title = f"Top {x} Richest People" , description = "This is decided on the basis of raw money in the bank and wallet",color = discord.Color(0xfa43ee))
      index = 1
      for amt in total:
          id_ = leader_board[amt]
          member = self.bot.get_user(id_)
          name = member
          em.add_field(name = f"{index}. {name}" , value = f"{amt}",  inline = False)
          if index == x:
              break
          else:
              index += 1

      await ctx.send(embed = em)









#tells in console if cog has been loaded
def setup(bot):
    bot.add_cog(eco(bot))
    cprint(colored("""Cog: Economy
Status: Loaded""", __colors__.blue))