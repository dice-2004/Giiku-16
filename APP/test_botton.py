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

@tree.command(name="test3",description="aaa")
async def test_command3(interaction: discord.Interaction):
    button = discord.ui.Button(label="a",style=discord.ButtonStyle.primary,custom_id="aaa")
    view = discord.ui.View()
    view.add_item(button)
    await interaction.response.send_message(view=view)

@tree.command(name="test2",description="aaa")
async def test_command2(interaction: discord.Interaction):
    select = [
        discord.SelectOption(label="test1",value="1",description="1"),
        discord.SelectOption(label="test2",value="2",description="2")
    ]
    view = discord.ui.View()
    view.add_item(discord.ui.Select(custom_id="iii",options=select))
    await interaction.response.send_message(view=view)


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
    await inter.response.send_message("Button!",ephemeral=True)


async def on_dropdown(inter:discord.Interaction):
    custom_id = inter.data["custom_id"]
    select_values = inter.data["values"]
    print(custom_id)
    await inter.response.send_message("Select!",ephemeral=True)

client.run(config_data["discord_token"])
