from modules import fetch_class, notion_class
import discord  # ver.2.3.2
from discord.ext import commands

#自動通知機能で使用
from discord.ext import commands, tasks
from modules.auto_announce import AutoAnnounce

#config.ini内のデータの取得
fetch = fetch_class.fetcher()
config_data = fetch.fetch()
notion = notion_class.Notion(config_data["notion_token"])

intents = discord.Intents.default()
bot = commands.Bot(command_prefix="!", intents=intents)

CHANNEL_ID = 1297908587141791845
TIME = "0900"

#指定時間で通知するためのループ
@tasks.loop(seconds=60)
async def loop():
    await AutoAnnounce.auto_disp_button(bot,CHANNEL_ID,TIME)

@bot.event
async def on_ready():
    print(f"Logged in as {bot.user}")
    
    #指定時間で通知するためのループを開始
    if not loop.is_running():
        print("loopstart")
        loop.start()

#自動通知機能でボタンが押されたときの処理
@bot.event
async def on_interaction(inter:discord.Interaction):
    try:
        if inter.data['component_type'] == 2:
            await AutoAnnounce.on_button_click(inter, config_data["database_id"], notion)
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