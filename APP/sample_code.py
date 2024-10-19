import dotenv
import os
import discord
import random

dotenv.load_dotenv()
token = str(os.getenv("TOKEN"))
print(token)

# botに機能を詰め込む　＝　オブジェクト化
bot =discord.Bot(
        intents=discord.Intents.all(),  # 全てのインテンツを利用できるようにする
        activity=discord.Game("hogehoge"),
)

@bot.event#初期設定
async def on_ready():
    print("XXX")

# @bot.event#オウム返し
# async def on_message(message: discord.Message):
#     if message.author == bot.user:
#         return

#     await message.channel.send(message.content)

@bot.slash_command()#discordのコマンド
async def ping(ctx: discord.ApplicationContext):
    await ctx.respond(f"pog to {ctx.author.mention}")


def change_hand(hand):
    if(hand=="グー"):
        return 1
    elif(hand=="チョキ"):
        return 2
    elif(hand=="パー"):
        return 3
    else:
        return 0



@bot.slash_command(name="jyanken")
async def jangken(ctx: discord.ApplicationContext,hand: discord.Option(str,"手を入力してください")):
    hands = ["グー","チョキ","パー"]
    player = change_hand(hand)
    hand = int(random.uniform(1,3))#1グー　2チョキ　３パー
    print(f"{hand},{player}")
    if(player == 0):
        await ctx.respond(f"error")
    elif(player == hand):
        await ctx.respond(f"{hands[hand-1]} あいこ")
    elif(player > hand and (player==3 and hand==1)):#player_win
        await ctx.respond(f"{hands[hand-1]} 勝ち")
    elif(player < hand and (player==1 and hand==3)):#hand_win
        await ctx.respond(f"{hands[hand-1]} 負け")


bot.run(token)
