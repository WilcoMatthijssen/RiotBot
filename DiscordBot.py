from RiotAPI import RiotAPI #used to call to riot api
from discord.ext.commands import Bot


Riot = RiotAPI("{KEY}")
bot = Bot(command_prefix="!")


@bot.event
async def on_ready():
    print("----------------------")
    print("Logged In As")
    print("Username: %s" % bot.user.name)
    print("ID: %s" % bot.user.id)
    print("----------------------")


@bot.command()
async def riot(ctx, playername):
    response = dict(Riot.summoner_by_name(playername))
    text = ""
    for key, value in zip(response.keys(), response.values()):
        text += f"**{key}**: {value}\n"

    await ctx.send(text)



bot.run("KEY")
