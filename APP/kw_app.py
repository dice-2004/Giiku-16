from modules import fetch_class, notion_class
# from discord import Intents,Bot
import time
import discord
from discord import app_commands
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
client = discord.Client(intents=intents)
tree = app_commands.CommandTree(client)

bot=commands.Bot(
    command_prefix="/",
    intents=intents,
    application_id=config_data[client.id],  # application_idを指定
    activity=discord.Game("hogehoge"),
)

class DispButton(discord.ui.View):
    def __init__(self, timeout=180):
        super().__init__(timeout=timeout)

@bot.event
async def on_ready():
    print("Bot is ready")
    new_activity = f"kwテスト中"
    await tree.sync()
    await bot.change_presence(activity=discord.Game(new_activity))


@tree.command(name="button", description="Display Button")
async def disp_button(interaction: discord.Interaction):
    # embedの表示
    author = interaction.user
    embed = discord.Embed(title="踊れスネ夫!", description="Here you are", color=0xff0000)
    embed.set_image(url='https://images-ext-1.discordapp.net/external/2EYEX2fHQoHNLdgfjYjMqAwY5CnADNx01IiIyBr49k4/https/media1.tenor.com/m/4poLNzFGYTwAAAAC/suneo-dance-dance.gif?width=655&height=655')
    embed.set_author(name=author)
    await interaction.response.send_message(embed=embed)



@bot.command()
async def time_fetch(ctx):
    await ctx.send(f"{time.ctime()}")

@bot.event
async def on_message(message):
    # メッセージが/time_fetchだった場合:

    if message.author.bot:
        return
    await bot.process_commands(message)
    await message.channel.send(message.content)

    

bot.run(config_data["discord_token"])
