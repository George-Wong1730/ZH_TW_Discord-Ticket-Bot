#Version: 1.9
#GitHub: https://github.com/George-Wong1730/ZH_TW_Discord-Ticket-Bot/
#

import discord
import json
from discord import *
from discord.ext import commands, tasks
from cogs.ticket_system import Ticket_System
from cogs.ticket_commands import Ticket_Command

#This will get everything from the config.json file
with open("config.json", mode="r") as config_file:
    config = json.load(config_file)

BOT_TOKEN = config["token"]  #Your Bot Token from https://discord.dev
GUILD_ID = config["guild_id"] #Your Server ID aka Guild ID  
CATEGORY_ID1 = config["category_id_1"] #類別 1，機器人應開啟工單選項 1 的工單
CATEGORY_ID2 = config["category_id_2"] #類別 2，機器人應開啟工單選項 2 的工單

bot = commands.Bot(intents=discord.Intents.all())

@bot.event
async def on_ready():
    print(f'Bot Started | {bot.user.name}')
    richpresence.start()

#機器人狀態，計算伺服器中所有開啟的工單。如果您的類別多於或少於 2 個，則需要新增/變更內容
@tasks.loop(minutes=1)
async def richpresence():
    guild = bot.get_guild(GUILD_ID)
    category1 = discord.utils.get(guild.categories, id=int(CATEGORY_ID1))
    category2 = discord.utils.get(guild.categories, id=int(CATEGORY_ID2)) #You need to add/change things if you have more or less than 2 Categories
    await bot.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name=f'Tickets | {len(category1.channels) + len(category2.channels)}'))

bot.add_cog(Ticket_System(bot))
bot.add_cog(Ticket_Command(bot))
bot.run(BOT_TOKEN)
