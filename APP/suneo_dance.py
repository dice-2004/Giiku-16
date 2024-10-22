from modules import fetch_class, notion_class
# from discord import Intents,Bot
import time
import discord
from discord.ext import commands


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

@bot.command()
async def mention_user(ctx, member: discord.Member = None):
    if member is None:
        member = ctx.author
    await ctx.send(f'hello {member.mention}!')


@bot.command()
async def suneo_dance(ctx, member: discord.Member = None):
    if member is None:
        member = ctx.author

    kWat0 = await bot.fetch_user(965208013340311633)

    embed = discord.Embed(
        title = "Let's dance!",
        description = f'FROM 「{kWat0.display_name}」 TO 「{member.mention}」',
        color = discord.Color.blue()
    )

    # embed.add_field(name="Let's dance!", value="https://media1.tenor.com/m/4poLNzFGYTwAAAAC/suneo-dance-dance.gif", inline = False)
    embed.set_image(url="https://media1.tenor.com/m/4poLNzFGYTwAAAAC/suneo-dance-dance.gif")

    await ctx.send(embed=embed)



@bot.event
async def on_message(message):
    # メッセージが/time_fetchだった場合:

    if message.author.bot:
        return

    user_id = await bot.fetch_user(965208013340311633)
    await bot.process_commands(message)
    if user_id == message.author:
        await message.channel.send(f'{user_id.mention} shut up!')

bot.run(config_data["discord_token"])
