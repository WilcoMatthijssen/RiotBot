from RiotAPI import RiotAPI #used to call to riot api
from LoLConstants import LoLConstants
from DataDragon import DataDragon
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


@bot.command()
async def season(ctx):
    curr_season = LoLConstants.seasons()[-1]["season"]
    text = f"The current League of Legends season is: {curr_season}"
    await ctx.send(text)

@bot.command()
async def maps(ctx):
    maps_info = LoLConstants.maps()
    text = "**League of legends has the following maps:**\n\n"
    for i, map_info in enumerate(maps_info, start=1):
        text += "{}. **{}** : {}\n".format(i, map_info["mapName"], map_info["notes"])
    await ctx.send(text)


@bot.command()
async def modes(ctx):
    modes_info = LoLConstants.gameModes()
    text = "**League of legends has the following game modes:**\n\n"
    for i, mode_info in enumerate(modes_info , start=1):
        text += "{}. **{}** : {}\n".format(i, mode_info["gameMode"], mode_info["description"])
    await ctx.send(text)

bot.run("KEY")
