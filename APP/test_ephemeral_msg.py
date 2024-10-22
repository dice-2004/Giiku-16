async def test_ephe():
    if message.author.bot:
        return
    author = message.author
    embed = discode.Embed(title="Hi!", description="Here you are", color=0xff0000)
    embed.set_image(url='https://images-ext-1.discordapp.net/external/2EYEX2fHQoHNLdgfjYjMqAwY5CnADNx01IiIyBr49k4/https/media1.tenor.com/m/4poLNzFGYTwAAAAC/suneo-dance-dance.gif?width=655&height=655')
    embed.set_author(name=author)
