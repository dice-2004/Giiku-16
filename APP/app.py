from modules import fetch_class, notion_class
# from discord import Intents,Bot
import time
import discord
from discord.ext import commands

#################################################################################################################################################################
fetch = fetch_class.fetcher()
config_data = fetch.fetch()
# notion = notion_class.Notion(config_data["notion_token"])

# # print(config_data)
# str = notion.get_pages(config_data["database_id"])
# print(str)
#################################################################################################################################################################


intents =discord.Intents.default()
intents.members = True
intents.message_content = True


bot=commands.Bot(
        command_prefix="/",
        intents=intents,
        activity=discord.Game("いまうごいたわ"),
)



@bot.event
async def on_ready():
    await bot.load_extension("cogs.comandsss")
    await bot.load_extension("cogs.comandss")
    print("Bot is ready")


bot.run(config_data["discord_token"])
