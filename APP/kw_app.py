from modules import fetch_class, notion_class
# from discord import Intents,Bot
import time
import discord
from discord.ext import commands
import test_ephemeral_msg as ttt


fetch = fetch_class.fetcher()
config_data = fetch.fetch()
# notion = notion_class.Notion(config_data["notion_token"])

# # print(config_data)
# str = notion.get_database(config_data["database_id"])
# print(str)

intents =discord.Intents.default()
intents.members = True
intents.message_content = True


bot=commands.Bot(
        command_prefix="/",
        intents=intents,
        activity=discord.Game("hogehoge"),
)

@bot.event
async def on_ready():
    print("Bot is ready")



@bot.command()
async def time_fetch(ctx):
    await ctx.send(f"{time.ctime()}")

@bot.event
async def on_message(message):
    # メッセージが/time_fetchだった場合:
    await ttt.test_ephe(message)
    
bot.run(config_data["discord_token"])
