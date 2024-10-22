from modules import fetch_class, notion_class
# from discord import Intents,Bot
import time
import discord
from discord.ext import commands


fetch = fetch_class.fetcher()
config_data = fetch.fetch()
# notion = notion_class.Notion(config_data["notion_token"])

# # print(config_data)
# str = notion.get_pages(config_data["database_id"])
# print(str)

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
    print("Bot is ready")



@bot.command()
async def time_fetch(ctx):
    await ctx.send(f"{time.ctime()}")

@bot.event
async def on_message(message):
    # メッセージが/time_fetchだった場合:
    target_username = "kwat0_0d065"#ユーザー名

    if message.author.bot:
        return
    if message.content:
        target_user = discord.utils.get(message.guild.members, name=target_username)
        if target_user:

            await bot.process_commands(message)
            await message.channel.send(f"{target_user.mention}{target_user.mention}\n{target_user.mention}{target_user.mention}")


bot.run(config_data["discord_token"])
