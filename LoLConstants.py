import requests # used to make requests to the riot api


class LoLConstants:
    """ Access constants for the game League of Legends.
        API made by Riot Games.
        Class made by Wilco Matthijssen. """

    @staticmethod
    def _get(filename):
        """ Adds the given filename to the riot api url.
            It requests information from that url which is a json that gets interpreted as a list of dicts. """
        url = f"http://static.developer.riotgames.com/docs/lol/{filename}"
        return requests.get(url).json()

    @staticmethod
    def seasons():
        """ Returns a list containing most of league of legends seasons.
            A season is represented as a dict containing an id and a season. """
        filename = "seasons.json"
        return LoLConstants._get(filename)

    @staticmethod
    def queues():
        """ Returns a list containing league of legends queues of which many are not available to players.
            A queue is represented as a dict containing a queueId, map, description and notes. """
        filename = "queues.json"
        return LoLConstants._get(filename)

    @staticmethod
    def maps():
        """ Returns a list containing league of legends maps of which many are not available to players.
            A map is represented as a dict containing a mapId, mapName and notes. """
        filename = "maps.json"
        return LoLConstants._get(filename)

    @staticmethod
    def gameModes():
        """ Returns a list containing league of legends gameModes of which many are not available to players.
            A gameMode is represented as a dict containing a gameMode and a description. """
        filename = "gameModes.json"
        return LoLConstants._get(filename)

    @staticmethod
    def gameTypes():
        """ Returns a list containing league of legends gameTypes of which many are not available to players.
            A gameType is represented as a dict containing a gameType and a description. """
        filename = "gameTypes.json"
        return LoLConstants._get(filename)


if __name__ == "__main__":
    print(LoLConstants.seasons())
    print(LoLConstants.queues())
    print(LoLConstants.maps())
    print(LoLConstants.gameModes())
    print(LoLConstants.gameTypes())


