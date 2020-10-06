from RiotAPI import RiotAPI  # Used for riot command
from LoLConstants import LoLConstants  # Used for seasons, maps and modes commands
from DataDragon import DataDragon

from discord.ext.commands import Bot  # Used to create the bot and allowing custom commands
import json  # Used for getting keys from keys.json file
import os  # Used for checking if keys.json exist


def get_key(filename, key_name):
    """ Opens json file and returns data from given key_name.
        Quits when file or key not found"""
    if os.path.exists(filename):
        with open(filename, 'r') as json_file:
            api_keys = json.load(json_file)
            if key_name in api_keys and api_keys[key_name] != "KEY":
                return api_keys[key_name]
            else:
                print(f"{key_name} not found")
                quit()
    else:
        print("{} doesn't exist.".format(filename))
        quit()


Riot_key = get_key("keys.json", "RiotAPIKey")
Discord_key = get_key("keys.json", "DiscordAPIKey")

Riot = RiotAPI(Riot_key)
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


bot.run(Discord_key)
