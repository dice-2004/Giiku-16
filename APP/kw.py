from modules import fetch_class
import discord  # ver.2.3.2
from discord.ext import commands, tasks
from datetime import datetime, timezone

fetch = fetch_class.fetcher()
config_data = fetch.fetch()



intents = discord.Intents.default()
bot = commands.Bot(command_prefix="!", intents=intents)

CHANNEL_ID = 1297908587141791845
#client = discord.Client(intents=intents)

@tasks.loop(seconds=10)
async def loop():
    now = datetime.now(timezone.utc)
    print("1")
    ch = bot.get_channel(CHANNEL_ID)
    if ch is None:
        print("チャンネルが見つかりません。CHANNEL_IDが正しいか確認してください。")
        return
    print("2")
    await ch.send(str(now))
    print("3")

@bot.event
async def on_ready():
    print(f"Logged in as {bot.user}")
    if not loop.is_running():  # ループが動いていない場合のみ開始
        print("loopstart")
        loop.start()

async def load_extensions():
    await bot.load_extension("cogs.botton")
    await bot.load_extension("cogs.template")
    await bot.load_extension("cogs.test_notion")
    await bot.load_extension("cogs.test_auto")

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