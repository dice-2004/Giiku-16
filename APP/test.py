import discord
from discord.ext import commands
from discord import app_commands
from modules import fetch_class

# インテントの設定
intents = discord.Intents.default()
intents.message_content = True

# Botの設定
bot = commands.Bot(command_prefix='!', intents=intents)  # プレフィックスを'!'に変更

fetch = fetch_class.fetcher()
config_data = fetch.fetch()

@bot.event
async def on_ready():
    print(f"{bot.user} として起動完了")
    try:
        # スラッシュコマンドの同期
        synced = await bot.tree.sync()
        print(f"スラッシュコマンドを同期しました: {len(synced)} コマンド")
    except Exception as e:
        print(f"同期中にエラーが発生: {e}")

# スラッシュコマンドの定義
@bot.tree.command(name="test", description="テストコマンドです")
async def test(interaction: discord.Interaction, text: str):
    await interaction.response.send_message(f'てすと！{text}', ephemeral=True)

@bot.tree.command(name="suneo",description="テストコマンドです。")
async def suneo_dance(interaction: discord.Interaction):
    embed = discord.Embed(
        title = "Let's dance!",
        color = discord.Color.blue()
    )

    embed.set_image(url="https://media1.tenor.com/m/4poLNzFGYTwAAAAC/suneo-dance-dance.gif")
    await interaction.response.send_message(embed=embed)



# 通常のコマンドの例（!testで動作）
@bot.command()
async def test_normal(ctx):
    await ctx.send("これは通常のコマンドのテストです！")

bot.run(config_data["discord_token"])