import discord
from discord import app_commands
from discord.ext import commands

class YOUR_CLASS_NAME(commands.Cog):  # Cogクラスの継承を修正
    def __init__(self, bot):
        self.bot = bot
        self.tree = bot.tree  # デフォルトの CommandTree を使用

    @commands.Cog.listener()
    async def on_ready(self):
        await self.tree.sync()  # Botが準備完了したときにコマンドを同期

    @app_commands.command(name="template", description="テンプレです")
    async def template(self, interaction: discord.Interaction):
        await interaction.response.send_message("テンプレです。")

async def setup(bot):
    await bot.add_cog(YOUR_CLASS_NAME(bot))  # ボットにCogを追加