import discord
from discord import app_commands
from discord.ext import commands
from datetime import datetime, date, timedelta
from modules import fetch_class
from modules import notion_class

fetch = fetch_class.fetcher()
config_data = fetch.fetch()

database_id = config_data["database_id"]
notion_token = config_data["notion_token"]

nc = notion_class.Notion(notion_token)

class show_schedule(commands.Cog):  # Cogクラスの継承を修正
    def __init__(self, bot):
        self.bot = bot
        self.tree = bot.tree  # デフォルトの CommandTree を使用

    @commands.Cog.listener()
    async def on_ready(self):
        print("コマンド同期開始")
        await self.tree.sync()  # Botが準備完了したときにコマンドを同期
        print("コマンド同期完了")

    @app_commands.command(name="show_schedule", description="引数で日数指定")
    async def show_schedule(self, interaction: discord.Interaction, UntilDaysLaterIs: int = 1):
        data = nc.get_notion_data(database_id)
        sorted_data = sorted(data, key=lambda x: datetime.strptime(x["timeschedul"], "%Y/%m/%d"), reverse=False)
        filter_data = list(filter(lambda x: x["dead_line_exceed"] == False, sorted_data))
        
        # for i in filter_data:
        #     print(i["title"])

        # Embedの作成
        embed = discord.Embed(title=f'直近 {UntilDaysLaterIs} 日の予定を表示します。', description="", color=discord.Color.blue())
        
        # フィールドを追加
        for i in range(min(UntilDaysLaterIs, len(filter_data))):
            timeschedul = datetime.strptime(filter_data[i]["timeschedul"], "%Y/%m/%d").date()
            if date.today() < timeschedul <= date.today() + timedelta(days=UntilDaysLaterIs):
                embed.add_field(
                    name=f'`{filter_data[i]["timeschedul"]}  {filter_data[i]["select"]}  {filter_data[i]["title"]}`',
                    value="",
                    inline=False
                )


        # embed.set_thumbnail(url="https://media1.tenor.com/m/4poLNzFGYTwAAAAC/suneo-dance-dance.gif")
        embed.set_author(name=f'{interaction.user.display_name}', icon_url="https://media1.tenor.com/m/4poLNzFGYTwAAAAC/suneo-dance-dance.gif", url="https://www.notion.so/schedule-af2f277686974b18bf885570e0e54275")

        # Embedを送信
        await interaction.response.send_message(embed=embed, ephemeral=True)

async def setup(bot):
    await bot.add_cog(show_schedule(bot))  # ボットにCogを追加