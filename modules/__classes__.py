# -*- coding: utf-8 -*-
import os, sys, termcolor, discord, asyncio, random, datetime
from termcolor import colored 
from termcolor import cprint 
from discord.ext import commands
from discord.ext.commands import Bot
from discord.utils import get
from discord.ext import tasks
from discord.ext.tasks import loop
from discord import Member, Role
from random import *

class __colors__:
  red = "red"
  blue = "blue"
  green = "green"
  cyan = "cyan"
  grey = "grey"
  yellow = "yellow"
  magenta = "magenta"
  white = "white"
  
class __highlights__:
  grey = "on_grey"
  red = "on_red"
  green = "on_green"
  yellow = "on_yellow"
  blue = "on_blue"
  magenta = "on_magenta"
  cyan = "on_cyan"
  white = "on_white"
  
class __attributes__:
  bold = ["bold"]
  dark = ["dark"]
  underline = ["underline"]
  blink = ["blink"]
  reverse = ["reverse"]
  concealed = ["concealed"]
  
class __credits__():
  __credit__ = """
.
"""
   
class __version__():
  version = """2.9.3"""
  

  
