import discord
from discord.ext import commands

class Mycommands(commands.Cog):
    def __init__(self,bot):
        self.bot = bot

    @commands.command()
    async def piiing(self,ctx):
        await ctx.send("aho")

async def setup(bot):
    await bot.add_cog(Mycommands(bot))
