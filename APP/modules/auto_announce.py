import discord
from discord.ext import commands
from datetime import datetime

class AutoAnnounce():

    async def auto_disp_button(bot : commands.Bot, CHANNEL_ID : int):
        print("1")
        ch = bot.get_channel(CHANNEL_ID)
        if ch is None:
            print("チャンネルが見つかりません。CHANNEL_IDが正しいか確認してください。")
            return
        print("2")
        JST_time = datetime.now()
        now = str (JST_time).split(" ")[1].split(".")[0].split(":")[0] + str (JST_time).split(" ")[1].split(".")[0].split(":")[1]
        if(now != "2241"):
            await ch.send(now)
            button_embed = discord.Embed(title="今日、明日が期限の予定を表示します")
            await ch.send(embed=button_embed)
            button = discord.ui.Button(label="確認",style=discord.ButtonStyle.primary,custom_id="check")
            view = discord.ui.View()
            view.add_item(button)
            await ch.send(view=view)
            print("3")

    async def on_button_click(inter:discord.Interaction):
        custom_id = inter.data["custom_id"]
        if custom_id == "check":
            task_embed = discord.Embed(
                title = "今日明日が期限のタスク",
                description = "ユーザー名 : " + inter.user.name,
                color = 0x0000ff
            )
            await inter.response.send_message(embed=task_embed,ephemeral=True)