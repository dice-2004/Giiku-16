import discord

async def test_ephe(message):
    if message.author.bot:
        return

    #embedの表示
    author = message.author
    embed = discord.Embed(title="踊れスネ夫!", description="Here you are", color=0xff0000)
    embed.set_image(url='https://images-ext-1.discordapp.net/external/2EYEX2fHQoHNLdgfjYjMqAwY5CnADNx01IiIyBr49k4/https/media1.tenor.com/m/4poLNzFGYTwAAAAC/suneo-dance-dance.gif?width=655&height=655')
    embed.set_author(name=author)
    await message.channel.send(embed = embed)

    #ephemeral messageの送信
    interaction_response = discord.InteractionResponse()
    await interaction_response.send_message(embed = embed, ephemeral = True)