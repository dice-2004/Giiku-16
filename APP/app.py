from modules import fetch_class, notion_class
# # from discord import Intents,Bot
# import time
# import discord
# from discord import app_commands
# from discord.ext import commands

# #################################################################################################################################################################
fetch = fetch_class.fetcher()
config_data = fetch.fetch()
# # notion = notion_class.Notion(config_data["notion_token"])

# # # print(config_data)
# # str = notion.get_pages(config_data["database_id"])
# # print(str)
# #################################################################################################################################################################


# intents =discord.Intents.default()
# client = discord.Client(intents=intents)
# tree = app_commands.CommandTree(client)


# bot=commands.Bot(
#         command_prefix="!",
#         intents=intents,
#         activity=discord.Game("いまうごいたわ"),
# )

# async def load_extensions():
#     await bot.load_extension("cogs.botton")  # Cogファイルのロード

# @bot.event
# async def on_ready():
#     await load_extensions()
#     print("Bot is ready")


# client.run(config_data["discord_token"])


import discord
from discord.ext import commands

intents = discord.Intents.default()
bot = commands.Bot(command_prefix="!", intents=intents)

@bot.event
async def on_ready():
    print(f"Logged in as {bot.user}")

async def load_extensions():
    await bot.load_extension("cogs.botton")
    await bot.load_extension("cogs.template")

async def main():
    async with bot:
        await load_extensions()
        await bot.start(config_data["discord_token"])

import asyncio
asyncio.run(main())