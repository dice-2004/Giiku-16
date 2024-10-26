import discord
from discord import app_commands
from discord.ext import commands

class TestAuto(commands.Cog):  # Cogクラスの継承を修正
    def __init__(self, bot):
        self.bot = bot
        self.tree = bot.tree  # デフォルトの CommandTree を使用

    @commands.Cog.listener()
    async def on_ready(self):
        await self.tree.sync()  # Botが準備完了したときにコマンドを同期

    @app_commands.command(name="auto", description="auto_test")
    async def template(self, interaction: discord.Interaction):
        #interaction.user = "kWat0_0d65"
        await interaction.response.defer(thinking=True)
        #interaction.message.author = "nontenki._."
        await interaction.followup.send("test", ephemeral=True)

async def setup(bot):
    await bot.add_cog(TestAuto(bot))  # ボットにCogを追加