import discord
from discord import app_commands
from discord.ext import commands
from modules import fetch_class

intents = discord.Intents.default()
client = discord.Client(intents=intents)
tree = app_commands.CommandTree(client)

fetch = fetch_class.fetcher()
config_data = fetch.fetch()

@client.event
async def on_ready():
    await tree.sync()

@tree.command(name="gif_button",description="GIF画像を送れるよ")
async def test_command3(interaction: discord.Interaction):
    suneo_button = discord.ui.Button(label="スネ夫",style=discord.ButtonStyle.primary,custom_id="suneo")
    nobita_button = discord.ui.Button(label="のび太",style=discord.ButtonStyle.danger,custom_id="nobita")
    shizuka_button = discord.ui.Button(label="しずか",style=discord.ButtonStyle.success,custom_id="shizuka")
    view = discord.ui.View()
    view.add_item(suneo_button)
    view.add_item(nobita_button)
    view.add_item(shizuka_button)
    await interaction.response.send_message(view=view)


@tree.command(name="select_box",description="選択肢があるよ")
async def test_command2(interaction: discord.Interaction):
    select = [
        discord.SelectOption(label="スネ夫",value="suneo",description="dance"),
        discord.SelectOption(label="のび太",value="nobita",description="dance"),
        discord.SelectOption(label="しずか",value="shizuka",description="crazy")
    ]
    view = discord.ui.View()

    dropdown = discord.ui.Select(
        custom_id="select_box",
        options=select,
        min_values=1,
        max_values=1
    )
    view.add_item(dropdown)
    await interaction.response.send_message(view=view)




# =========================スネ夫ダンス=========================
async def suneo_dance(interaction: discord.Interaction):
    embed = discord.Embed(
        title = "Let's dance!",
        color = discord.Color.blue()
    )

    embed.set_image(url="https://media1.tenor.com/m/4poLNzFGYTwAAAAC/suneo-dance-dance.gif")
    await interaction.response.send_message(embed=embed)
# ==============================================================

# =========================のび太ダンス=========================
async def nobita_dance(interaction: discord.Interaction):
    embed = discord.Embed(
        title = "Let's dance!",
        color = discord.Color.red()
    )

    embed.set_image(url="https://media1.tenor.com/m/CGD9ne4mYqIAAAAC/nobita-nobita-dance.gif")
    await interaction.response.send_message(embed=embed)
# ==============================================================

# =========================しずか、は？=========================
async def shizuka_hatena(interaction: discord.Interaction):
    embed = discord.Embed(
        title = "Are you Crazy?",
        color = discord.Color.pink()
    )

    embed.set_image(url="https://media1.tenor.com/m/Tht1rEEUkMgAAAAd/doraemon-shizuka.gif")
    await interaction.response.send_message(embed=embed)
# ==============================================================



#全てのインタラクションを取得
@client.event
async def on_interaction(inter:discord.Interaction):
    try:
        if inter.data['component_type'] == 2:
            await on_button_click(inter)
        elif inter.data['component_type'] == 3:
            await on_dropdown(inter)
    except KeyError:
        pass

## Button,Selectの処理
async def on_button_click(inter:discord.Interaction):
    custom_id = inter.data["custom_id"]
    print(custom_id)
    if custom_id == "suneo":
        await suneo_dance(inter)
    elif custom_id == "nobita":
        await nobita_dance(inter)
    elif custom_id == "shizuka":
        await shizuka_hatena(inter)


async def on_dropdown(inter:discord.Interaction):
    custom_id = inter.data["custom_id"]
    select_values = inter.data["values"]
    print(custom_id)
    if select_values[0] == "suneo":
        await suneo_dance(inter)
    elif select_values[0] == "nobita":
        await nobita_dance(inter)
    elif select_values[0] == "shizuka":
        await shizuka_hatena(inter)

client.run(config_data["discord_token"])
