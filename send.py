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

banlist=[738052976723099751, 746241690028736582, 745686303479169105, 741919727110062198, 754459212658114698, 751614817412055081, 738064884159348848, 738064841658335283, 748977999285714996, 753064737721286836, 738064786218025111, 743875265532264479, 741303074857156658, 742386914383888456, 755854291063013539]
async def sendm(banlist, ctx, text=""):
	if(ctx.channel.id in banlist):
		return
	else:
		await ctx.send(text)