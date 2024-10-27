from modules import fetch_class
import discord  # ver.2.3.2
from discord.ext import commands, tasks
from APP.modules.auto_announce import AutoAnnounce

fetch = fetch_class.fetcher()
config_data = fetch.fetch()



intents = discord.Intents.default()
bot = commands.Bot(command_prefix="!", intents=intents)

CHANNEL_ID = 1297908587141791845
#client = discord.Client(intents=intents)

@tasks.loop(seconds=60)
async def loop():
    await AutoAnnounce.auto_disp_button(bot,CHANNEL_ID)

@bot.event
async def on_ready():
    print(f"Logged in as {bot.user}")
    if not loop.is_running():  # ループが動いていない場合のみ開始
        print("loopstart")
        loop.start()

@bot.event
async def on_interaction(inter:discord.Interaction):
    try:
        if inter.data['component_type'] == 2:
            await AutoAnnounce.on_button_click(inter)
    except KeyError:
        pass

async def load_extensions():
    await bot.load_extension("cogs.botton")
    await bot.load_extension("cogs.template")
    await bot.load_extension("cogs.test_notion")

async def main():
    async with bot:
        await load_extensions()
        await bot.start(config_data["discord_token"])

import asyncio

if __name__ == "__main__":
    try:
        asyncio.run(main())        
    except KeyboardInterrupt:
        exit()
    except Exception as e:
        print(e)
        exit()