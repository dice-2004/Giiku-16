from modules import fetch_class
import discord  # ver.2.3.2
from discord.ext import commands

fetch = fetch_class.fetcher()
config_data = fetch.fetch()



intents = discord.Intents.default()
bot = commands.Bot(command_prefix="!", intents=intents)

@bot.event
async def on_ready():
    print(f"Logged in as {bot.user}")

async def load_extensions():
    await bot.load_extension("cogs.botton")
    await bot.load_extension("cogs.template")
    await bot.load_extension("cogs.test_notion")

async def main():
    async with bot:
        await load_extensions()
        await bot.start(config_data["discord_token"])

import asyncio

try:
    asyncio.run(main())
except KeyboardInterrupt:
    print("停止しますぅぃぅぃぅぃ")
    # bot.close()
    exit()
except Exception as e:
    print(e)
    # bot.close()
    exit()
