import discord
from discord.ext import commands
from datetime import datetime

class AutoAnnounce():

    #表示すべきタスクかの判断
    def is_display(task, notion_name, until):
        JST_time = datetime.now()
        today = int (str (JST_time).split(" ")[0].replace("-", ""))
        deadline = int (task.get("timeschedule").replace("/", ""))
        if deadline + until > today and task.get("dead_line_exceed") == False:
            if notion_name not in task.get("person", []):
                return True
        return False
    
    #指定された時間に確認のボタンを表示する
    async def auto_disp_button(bot : commands.Bot, CHANNEL_ID : int, time : str):
        ch = bot.get_channel(CHANNEL_ID)
        if ch is None:
            print("チャンネルが見つかりません。CHANNEL_IDが正しいか確認してください。")
            return
        JST_time = datetime.now()
        now = str (JST_time).split(" ")[1].split(".")[0].split(":")[0] + str (JST_time).split(" ")[1].split(".")[0].split(":")[1]
        if(now == time):
            await ch.send(now)
            button_embed = discord.Embed(title="今日、明日が期限の予定を表示します")
            await ch.send(embed=button_embed)
            button = discord.ui.Button(label="確認",style=discord.ButtonStyle.primary,custom_id="check")
            view = discord.ui.View()
            view.add_item(button)
            await ch.send(view=view)

    #ボタンが押されたときの処理
    async def on_button_click(inter:discord.Interaction, database_id : str, notion):
        await inter.response.defer(thinking=True, ephemeral=True)
        custom_id = inter.data["custom_id"]
        all_data = notion.get_notion_data(database_id)

        #どのボタンが押されたか判定？
        if custom_id == "check":
            until = 2
        
        #仮ユーザー登録
        if inter.user.name == "kwat0_0d065":
            notion_name = "川崎友輝"
        if inter.user.name == "._.dice._.":
            notion_name = "dice"
        if inter.user.name == "naomi_1156":
            notion_name = "1828 NAoMi"
        if inter.user.name == "chog29.":
            notion_name = "chog29"
        
        #embedsを使うならこれ
        task_embeds = []
        for task in all_data:
            if AutoAnnounce.is_display(task, notion_name, until):
                if task.get("select") == None:
                    select = ""
                else :
                    select = task.get("select")

                task_embed = discord.Embed(
                    title = task.get("title"),
                    description = "期限: " + task.get("timeschedule") + "\nセレクト: " + select
                )
                task_embeds.append(task_embed)
        user_embed = discord.Embed(
            title = "今日明日が期限のタスク",
            description = "ユーザー名 : " + inter.user.name,
            color = 0x0000ff,
        )
        await inter.followup.send(embed=user_embed,ephemeral=True)
        await inter.followup.send(embeds=task_embeds,ephemeral=True)
