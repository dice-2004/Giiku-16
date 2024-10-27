import discord
from discord import app_commands
from discord.ext import commands
from datetime import datetime, date, timedelta
from modules import fetch_class
from modules import notion_class
import random

fetch = fetch_class.fetcher()
config_data = fetch.fetch()

database_id = config_data["database_id"]
notion_token = config_data["notion_token"]

nc = notion_class.Notion(notion_token)

cat =[
    "https://media1.tenor.com/m/b7K75WzKjssAAAAd/huh-cat-huh-m4rtin.gif",
    "https://media1.tenor.com/m/_gRELTssBRUAAAAd/%E7%8C%AB%E3%83%9F%E3%83%BC%E3%83%A0.gif",
    "https://media1.tenor.com/m/8dGugqxC4sAAAAAd/shocked-surprised.gif",
    "https://media1.tenor.com/m/kOfiGkhc-5kAAAAC/kitty-smiley-kitty.gif",
    "https://media1.tenor.com/m/QlGLLu2y6t4AAAAC/hi-dane-meow.gif",
    "https://media1.tenor.com/m/1kf4J-xC_68AAAAd/cat.gif",
    "https://media1.tenor.com/m/sJIQXhKPb1YAAAAd/sad-cat.gif",
    "https://media1.tenor.com/m/SUv_UTpCX10AAAAd/womp-womp.gif",
    "https://media1.tenor.com/m/7_ZYPubPKuoAAAAd/kixlike-look-here.gif"
]

class show_schedule(commands.Cog):  # Cogクラスの継承を修正
    def __init__(self, bot):
        self.bot = bot
        self.tree = bot.tree  # デフォルトの CommandTree を使用

    @commands.Cog.listener()
    async def on_ready(self):
        print("Botが準備完了")
        print("コマンド同期開始")
        try:
            await self.tree.sync()
            print("コマンド同期完了")
        except Exception as e:
            print(f"コマンド同期中にエラーが発生しました: {e}")

    @app_commands.command(name="show_schedule", description="引数で日数指定")
    async def show_schedule(self, interaction: discord.Interaction, until_days_later_is: int = 1):
        if interaction.user.name == "kwat0_0d065":
            notion_name = "川崎友輝"
        if interaction.user.name == "._.dice._.":
            notion_name = "dice"
        if interaction.user.name == "naomi_1156":
            notion_name = "1828 NAoMi"
        if interaction.user.name == "chog29.":
            notion_name = "chog29"


        data = nc.get_notion_data(database_id)
        sorted_data_timeschedule = sorted(data, key=lambda x: datetime.strptime(x["timeschedule"], "%Y/%m/%d"), reverse=False)
        filter_data_deadline = list(filter(lambda x: x["dead_line_exceed"] == False, sorted_data_timeschedule))
        # filter_data = list(filter(lambda x: notion_name in x["person"], filter_data_deadline))
        
        # for i in filter_data_deadline:
        #     print(notion_name in i["person"])

        # Embedの作成
        embed = discord.Embed(title=f'直近 {until_days_later_is} 日の予定を表示します。', description="", color=discord.Color.blue())
        
        # フィールドを追加
        for i in range(min(until_days_later_is, len(filter_data_deadline))):
            timeschedul = datetime.strptime(filter_data_deadline[i]["timeschedule"], "%Y/%m/%d").date()
            if date.today() < timeschedul <= date.today() + timedelta(days=until_days_later_is):
                if not notion_name in filter_data_deadline[i]["person"]:
                    embed.add_field(
                        name=f'`{filter_data_deadline[i]["timeschedule"]}  {filter_data_deadline[i]["select"]}  {filter_data_deadline[i]["title"]}`',
                        value="",
                        inline=False
                    )


        embed.set_thumbnail(url=random.choice(cat))
        # embed.set_author(name=f'{interaction.user.display_name}', icon_url="https://media1.tenor.com/m/4poLNzFGYTwAAAAC/suneo-dance-dance.gif", url="https://www.notion.so/schedule-af2f277686974b18bf885570e0e54275")

        # Embedを送信
        await interaction.response.send_message(embed=embed, ephemeral=True)

async def setup(bot):
    await bot.add_cog(show_schedule(bot))  # ボットにCogを追加