import discord
from discord import app_commands
from discord.ext import commands
from discord.ui import TextInput, Modal
from modules import fetch_class as fet

class Register(commands.Cog):  # Cogクラスの継承を修正
    def __init__(self, bot):
        self.bot = bot
        self.tree = bot.tree  # デフォルトの CommandTree を使用

    @commands.Cog.listener()
    async def on_ready(self):
        print("1")
        await self.tree.sync()  # Botが準備完了したときにコマンドを同期
        print("2")

    @app_commands.command(name="register", description="notionのユーザー名の登録")
    async def register(self, interaction: discord.Interaction):
        modal = Question("notionのユーザー名の登録")
        print("c")
        await interaction.response.send_modal(modal)
        print("d")

async def setup(bot):
    await bot.add_cog(Register(bot))  # ボットにCogを追加

class Question(Modal):
    def __init__(self, title: str) -> None:
        super().__init__(title=title)
        self.answer = TextInput(label="notionのユーザー名を入力してください", style=discord.TextStyle.long)
        self.add_item(self.answer)

    async def on_submit(self, interaction: discord.Interaction) -> None:
        await interaction.response.send_message(
            f"{interaction.user} さんのnotionのユーザー名を {self.answer.value} で登録します", ephemeral=True
        )
        fet.write_config(self, interaction.user, self.answer.value)