import requests  # used to make requests to the riot api


class DataDragon:
    """ Data Dragon is a collection of League of Legends game data and assets,
        including champions, items, runes, summoner spells, and profile icons."""

    def __init__(self):
        self.api_info = self.regions()

    domain = "https://ddragon.leagueoflegends.com/"
    docs = "https://developer.riotgames.com/docs/lol#data-dragon"

    @staticmethod
    def _get(url):
        """ Request data from the given url which is a json that gets interpreted as a list of dicts. """
        return requests.get(url).json()

    @staticmethod
    def versions():
        """ Returns a list of all DataDragon API versions new to old. """
        url = f"{DataDragon.domain}api/versions.json"
        return DataDragon._get(url)

    @staticmethod
    def regions():
        """ DataDragon versions aren't always equivalent to the League of Legends client version.
            This function returns the current DataDragon versions. """
        url = f"{DataDragon.domain}realms/na.json"
        return DataDragon._get(url)

    def languages(self):
        """ Returns a list containing languages supported by the League of Legends client. """
        site = self.api_info["cdn"]
        url = f"{site}/languages.json"
        return DataDragon._get(url)

    def champions(self):
        site = self.api_info["cdn"]
        version = self.api_info["n"]["champion"]
        url = f"{site}/{version}/data/en_US/champion.json"
        return self._get(url)

    def items(self):
        site = self.api_info["cdn"]
        version = self.api_info["n"]["item"]
        url = f"{site}/{version}/data/en_US/item.json"
        return self._get(url)

    def summoners(self):
        site = self.api_info["cdn"]
        version = self.api_info["n"]["summoner"]
        url = f"{site}/{version}/data/en_US/summoner.json"
        return self._get(url)

    def profileicons(self):
        site = self.api_info["cdn"]
        version = self.api_info["n"]["profileicon"]
        url = f"{site}/{version}/data/en_US/profileicon.json"
        return self._get(url)


if __name__ == "__main__":
    d = DataDragon()
    print(d.versions())
    print(d.regions())
    print(d.languages())
    print(d.champions())
    print(d.items())
    print(d.summoners())
    print(d.profileicons())
