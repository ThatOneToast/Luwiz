




    users = await self.get_bank_data()

    if str(user.id) in users:
      return False
    else:
      
      users[str(user.id)] = {}
  asynusersdef open_account(self, user):
      users[str(user.id)]["wallet"] = 5555

    with open("mainbank.json", "w") as f:
      json.dump(users,f)
    return True

  async def get_bank_data(self):
    with open("mainbank.json", "r") as f:
      users = json.load(f)
        
      return users
del db["key"]db[str(user.id)]["bank"] = 0
      

  @commands.command()
  async def withdraw(self,ctx,amount = None):
    await self.open_account(ctx.author)

    if amount == None:
      await ctx.send("Please enter an amount to withdraw")
      return
    bal = await self.update_bank(ctx.author)

    amount = int(amount)

    if amount>bal[1]:
      await ctx.send("You don't have enough funds")
      return
    if amount<0:
      await ctx.send("Amount must be positive!")
      return

    await self.update_bank(ctx.author,amount, "wallet")
    await self.update_bank(ctx.author,-1*amount, "bank")

    await ctx.send(f"{ctx.author} withdrew ****💰{amount}💰****")

  @commands.command(aliases=['depo'])
  async def deposit(self,ctx,amount = None):
    await self.open_account(ctx.author)

    if amount == None:
      await ctx.send("Please enter an amount to withdraw")
      return
    bal = await self.update_bank(ctx.author)

    amount = int(amount)

    if amount>bal[0]:
      await ctx.send("You don't have enough funds💰")
      return
    if amount<0:
      await ctx.send("Amount must be positive!")
      return

    await self.update_bank(ctx.author,-1*amount)
    await self.update_bank(ctx.author,amount, "bank")

    await ctx.send(f"{ctx.author} deposited {amount} 💰")





  @commands.command()
  async def pay(self, ctx, member:discord.Member, amount = None):
    await self.open_account(ctx.author)
    await self.open_account(member)

    if amount == None:
      await ctx.send("Please enter an amout of 💰 to withdraw")
      return
    bal = await self.update_bank(ctx.author)

    amount = int(amount)

    if amount>bal[1]:
      await ctx.send("You don't have enough 💰 funds")
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
      await self.update_bank(ctx.author,3*amount, "bank")
      await ctx.send("you won TRIPPLE!!!")
    else:
      await self.update_bank(ctx.author,-1*amount, "bank")
      await ctx.send("You lost what a bumber try again :)")





  @commands.command(aliases=['balance', 'money', 'credits', 'coins'])
    users = await self.get_bank_data()
  async def bal(self, ctx):
    await self.opusers_account(ctx.author) # Again, want to check the output of this
users
    wallet_amt = db[str(ctx.author.id)]["wallet"]
    bank_amt = db[str(ctx.author.id)]["bank"]

    embed = discord.Embed(title=f"{ctx.author.name}'s balance ", color = discord.Color.gold())
    embed.add_field(name="wallet balance", value = f"💰{wallet_amt}💰")
    embed.add_field(name="bank balance", value = f"💰{bank_amt}💰")
    await ctx.send(embed=embed)


    users = await self.get_bank_data()
userusers

    with open("mainbank.json", "w") as f:
      json.dump(users,f)

  async defuserspdate_bank(self,user,changusers= 0,mode = "wallet"):
value = db[user"]mode
    db[str(user.iduserwallet"] += changectx.auuser
    bal = [db[str(user.id)]["wallet"], db[str(user.id)]["bank"]]
    return bal


  @commands.command()
    users = await self.get_bank_data()
  @commands.cooldown(1, 300, BucketType.user)
  async def beg(self, ctx):
    usersait self.open_acrandrange(401)
    with open("mainbank.json", "w") as f:
      json.dump(users,f)
    earnings = random.randint(100,1000)
    await ctx.send(f"Someone gave you 💰****${earnings}****💰")
    db[str(ctx.author.id)]["wallet"] += earnings


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









#<----------------------Premium ECO commands here----------------->

    users = await self.get_bank_data()
  @commands.Cog.listener()
  asusersc def on_message(self,ctx):
    with open("mainbank.json", "w") as f:
      json.dump(users,f)

    await self.open_account(ctx.author)
    earnings = random.randrange(10)
    db[str(ctx.author.id)]["wallet"] += earnings
    await self.bot.process_commands(message)


  @commands.command(aliases=['gp', 'gun'])
  @commands.cooldown(1, 3600, BucketType.user)
  @commands.has_role(83497711027945
4722)
  async def gunpoint(self,ctx,member:dis
cord.Member):
    await self.open_account(ctx.author)
    await self.open_account(member)
    bal = await self.update_bank(member)
    if bal[0]<1000:
      await ctx.send("Robing the poor isn't nice... I'll let you. For now😇.")
      return

    earnings = random.randrange(0, bal[0])

    await self.update_bank(ctx.author,3*earnings, "wallet")
    await self.update_bank(member, -1*earnings, "wallet")
    await ctx.send(f"You held {member} at gunpoint and got 💰****${earnings}****💰")



  



#<------------------------End Of Premium Command Here------------------------->


  mainshop = [{"name":"TimeMachine", "price":100000000, "description":"Go back in time"},
              {"name":"Lambo", "price":850000, "description":"A fancy car"},
              {"name":"robot", "price":340000, "description":"have someone cook, clean, and do everything for you"},
              {"name":"Nuke", "price":704200, "description":"buy a nuke(fake)"},
              {"name":"candy", "price":1, "description":"buy a piece of candy"}]


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

      users = await self.get_bank_data()
          return [False,1]

      cost = price*amount

      bal = await self.update_bank(user)

      if bal[0]<cost:
          return [False,2]


      try:users
          index = 0
          t = None
          for thing in db[str(user.id)]["bag"]:
              n = thing["item"]
              if nusers= item_name:
                  old_amt = thing["amount"]
                  new_amt = old_amt + amount
                  db[str(user.id)]["bag"][index]["amount"] = new_amt
                  t = 1
                  break
              usersdex+=1 
          if t == None:
              obj = {"item":item_name , "amount" : amount}
          users  db[str(user.id)]["bag"].append(obj)

      with open("mainbank.json","w") as f:
          json.dump(users,f)

      except:

          obj = {"item":item_name , "amount" : amount}
          db[str(user.id)]["bag"] = [obj]        
      await self.update_bank(user,cost*-1,"wallet")
      return [True,"Worked"]

  @commands.command()
      users = await self.get_bank_data()
  async def bag(self,ctx):
      await self.open_account(ctx.author)
      user = ctxusersuthor

      try:
          bag = db[str(user.id)]["bag"]
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

      users = await self.get_bank_data()          return [False,1]

      cost = price*amount


      bal = await self.update_bank(user)


      try:users
          index = 0
          t = None
          for thing in db[str(user.id)]["bag"]:
              n = thing["item"]
              if n == item_name:
                  old_amt = thing["amount"]
                  usersw_amt = old_amt - amount
                  if new_amt < 0:
                      return [False,2]
                  db[str(user.id)]["bag"][index]["amount"] = new_amt
                  t = 1
                  break
              index+=1 
          if t == None:

      with open("mainbank.json","w") as f:
          json.dump(users,f)              return [False,3]
      except:
          return [False,3]    


      await self.update_bank(user,cost,"wallet")

      return [True,"Worked"]

      users = await self.get_bank_data()

  @commands.command(aliases = ["lb"])
  async def leaderusers x = 10):
      leader_board = {}
      total = []usersusers
      for user in db[str(user.id)]:
          name = int(user)
          total_amount = db[user]["wallet"] + db[user]["bank"]
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







  @commands.command()
  async def filter(self,ctx):
    await ctx.message.channel.send("Filter has activated.")
    filtermessage()

def filtermessage():

  @commands.Cog.listener()
  async def on_message(self,ctx):
    badwordlist = ["nigger", "niggers", "nigga", "kike", "faggot", "fag", "faggs"]
    text = ctx.message.content.lower()
    text = text.replace("@", "a")
    text = text.replace("4", "a")
    text = text.replace("3", "e")
    text = text.replace("!", "i")
    text = text.replace("1", "i")
    text = text.replace("÷", "&")
    
    for badword in badwordlist:
      if badword in text:
        embed = discord.Embed(color=discord.Colour.red())
        embed.set_author(name="Luwiz Logger")
        embed.add_field(name="Slur", value="bad word", inline=False)
        await ctx.message.channel.send(embed=embed)
        await ctx.message.delete()
        break 






"""  with open("serverlog.json", "w") as f:
    json.dump("guilds",f)



  nlp = spacy.load('en')
  profanity_filter1 = ProfanityFilter(nlps={'en': nlp})
  nlp.add_pipe(profanity_filter1.spacy, last=True)

  @commands.command()
  async def filter_on(self,ctx):
    f.append(ctx.guild)
    await ctx.message.channel.send("Filter Has Been Activated")



  @commands.Cog.listener()
  async def on_message(self,message):
    if message.guild in f:
      doc = nlp(message)
      if doc._.is_profane:
        await message.delete(message)
        await message.send("Profanity in this server is not allowed. Please don't do it again.")"""




@bot.command(aliases=['tempmute'])
async def mute1(ctx, member: discord.Member=None, time=None, *, reason=None):
  if not member:
    await ctx.send("You must mention a member to mute!")
  elif not time:
    await ctx.send("You must mention a time!")
  else:
    if not reason:
        reason="No reason given"
    try:
        seconds = time[:-1] 
        duration = time[-1] 
        if duration == "s":
          seconds = seconds * 1
        elif duration == "m":
          seconds = seconds * 60
        elif duration == "h":
          seconds = seconds * 60 * 60
        elif duration == "d":
          seconds = seconds * 86400
        else:
          await ctx.send("Invalid duration input")
          return
    except Exception as e:
      print(e)
      await ctx.send("Invalid time input")
      return
    guild = ctx.guild
    Muted = discord.utils.get(guild.roles, name="Muted")
    if not Muted:
      Muted = await guild.create_role(name="Muted")

      for channel in guild.channels:
        await channel.set_permissions(Muted, speak=False, send_messages=False, read_message_history=True, read_messages=False)
        await member.add_roles(Muted, reason=reason)
        muted_embed = discord.Embed(title="Muted a user", description=f"{member.mention} Was muted by {ctx.author.mention} for {reason} to {time}")
        await ctx.send(embed=muted_embed)


        await asyncio.sleep(seconds)

        #unmutes after seconds
        await member.remove_roles(Muted)
        unmute_embed = discord.Embed(title="Mute over!", description=f'{ctx.author.mention} muted to {member.mention} for {reason} is over after {time}')
        await ctx.send(embed=unmute_embed)