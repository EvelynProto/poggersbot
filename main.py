import os
from keep_alive import keep_alive
import discord, random, datetime, os, traceback
import asyncio
import functools
import itertools
import math
import youtube_dl
from async_timeout import timeout
from discord.ext import commands
from send import banlist, sendm

bot = commands.AutoShardedBot(command_prefix = '.', description = "it fights dummy",case_insensitive=True)
bot.remove_command('help')
IgnoreImport = []

for Extension in [f.replace('.py', '') for f in os.listdir("Cogs") if os.path.isfile(os.path.join("Cogs", f))]:
	if Extension in IgnoreImport:
		continue
	try:
		print(f"Loading extension {Extension}")
		bot.load_extension(f"Cogs.{Extension}")
		print(f"Extension {Extension} loaded.")
	except (discord.ClientException, ModuleNotFoundError, commands.errors.ExtensionFailed):
		print(f'Failed to load extension {Extension}.')
		traceback.print_exc()

@bot.event
async def on_ready():
	print('my body is ready')
	await bot.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name="your mom lmao"))

keep_alive()
token = os.environ.get("TOKEN")
bot.run(token)