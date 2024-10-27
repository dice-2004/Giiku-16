import discord
from discord import app_commands
from discord.ext import commands
import asyncio

class Register(commands.Cog):  # Cogクラスの継承を修正
    def __init__(self, bot):
        self.bot = bot
        self.tree = bot.tree  # デフォルトの CommandTree を使用

    @commands.Cog.listener()
    async def on_ready(self):
        await self.tree.sync()  # Botが準備完了したときにコマンドを同期

    @app_commands.command(name="register", description="notionのユーザー名の登録")
    async def register(self, interaction: discord.Interaction):
        await interaction.response.defer(thinking=True, ephemeral=True)
        ch = interaction.channel
        await interaction.followup.send("notionのユーザー名を登録します", ephemeral=True)
        def check(m):
            return m.content != None and m.channel == ch
        
        try:
            print("a")
            # wait_forを用いて、イベントが発火し指定した条件を満たすまで待機する
            msg = await self.bot.wait_for('register', check=check, timeout=30)
            # wait_forの1つ目のパラメータは、イベント名の on_がないもの
            # 2つ目は、待っているものに該当するかを確認する関数 (任意)
            # 3つ目は、タイムアウトして asyncio.TimeoutError が発生するまでの秒数
            
        # asyncio.TimeoutError が発生したらここに飛ぶ
        except asyncio.TimeoutError:
            print("e")
            await interaction.followup.send(f'{interaction.author.mention}さん、時間切れです', ephemeral=True)
        else:
            # メンション付きでメッセージを送信する。
            print("b")
            await interaction.followup.send(f'{msg.author.mention}さんを{msg.context}で登録します', ephemeral=True)


async def setup(bot):
    await bot.add_cog(Register(bot))  # ボットにCogを追加