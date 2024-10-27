import discord
from discord import app_commands
from discord.ext import commands
from datetime import date

notion_data = [
    {"title" : "java", "select" : "aa", "timeSchedule" : "2024-10-20", "okPerson" : "@naomi_1156"},
    {"title" : "情報数学", "select" : "ii", "timeSchedule" : "2024-10-20", "okPerson" : "@chog29."},
    {"title" : "情報科学演習", "select" : "uu", "timeSchedule" : "2024-10-25", "okPerson" : "@._.dice._."},
    {"title" : "肥満", "select" : "ee", "timeSchedule" : "2024-10-25", "okPerson" : "@kwat0_0d065"}
]

class test_notion(commands.Cog):  # Cogクラスの継承を修正
    def __init__(self, bot):
        self.bot = bot
        self.tree = bot.tree  # デフォルトの CommandTree を使用

    @commands.Cog.listener()
    async def on_ready(self):
        await self.tree.sync()  # Botが準備完了したときにコマンドを同期
        print("コマンド同期完了")

    @app_commands.command(name="template", description="テンプレです")
    async def template(self, interaction: discord.Interaction):
        await interaction.response.send_message("aaa")

    @app_commands.command(name="show_data", description="test")
    async def template(self, interaction: discord.Interaction):
        global notion_data
        today = date.today()

        for nd in notion_data:
            nd_yaer, nd_month, nd_day = map(int, nd["timeSchedule"].split("-"))
            noda = date(nd_yaer, nd_month, nd_day)

            if today > noda:
                await interaction.channel.send(f'予定超過 : {nd["title"]}, {nd["select"]}, {nd["timeSchedule"]}, {nd["okPerson"]}')
            else:
                await interaction.channel.send(f'予定内 : {nd["title"]}, {nd["select"]}, {nd["timeSchedule"]}, {nd["okPerson"]}')

async def setup(bot):
    await bot.add_cog(test_notion(bot))  # ボットにCogを追加