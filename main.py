import discord
from discord.ext import commands
intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='$', intents=intents)
@bot.event
async def on_ready():
    print(f'{bot.user} olarak giriş yaptık')
@bot.command()
async def geri_donusum(ctx,*,malzeme):
    atiklar={
        "domates kabukları":"organic.jpg",
        "karton kutu":"paper.jpg",
        "cam şişe":"glass.jpg",
        "konserve kutusu":"metal.jpg",
        "pet şişe":"plastic.png",
        "maydonoz sapı":"organic.jpg"
    }
    if malzeme in atiklar:
        resim=atiklar[malzeme]
        await ctx.send("Bu malzeme için önerilen kutu:")
        with open(f"images/{resim}","rb") as f:
            await ctx.send(file=discord.File(f))
    else:
        await ctx.send("Bu malzemeyi tanımıyorum.")
    bot.run("Token burda bak")
