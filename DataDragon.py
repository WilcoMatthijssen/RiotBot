import requests  # used to make requests to the riot api


class DataDragon:
    """ Data Dragon is a collection of League of Legends game data and assets,
        including champions, items, runes, summoner spells, and profile icons."""

    domain = "https://ddragon.leagueoflegends.com/"
    docs = "https://developer.riotgames.com/docs/lol#data-dragon"

    @staticmethod
    def _get(url):
        """ Request data from the given url which is a json that gets interpreted as a list of dicts. """
        return requests.get(url).json()

    @staticmethod
    def versions():
        """ Returns a list of all DataDragon API versions, new to old. """
        url = f"{DataDragon.domain}api/versions.json"
        return DataDragon._get(url)

    @staticmethod
    def regions():
        """ DataDragon versions aren't always equivalent to the League of Legends client version.
            This function returns the current DataDragon versions. """
        url = f"{DataDragon.domain}realms/na.json"
        return DataDragon._get(url)

    @staticmethod
    def languages():
        """ Returns a list containing languages supported by the League of Legends client. """

        site = DataDragon.regions()["cdn"]
        url = f"{site}/languages.json"
        return DataDragon._get(url)

    @staticmethod
    def champions():
        """ Returns all champions in League of Legends. """
        version_info = DataDragon.regions()
        site = version_info["cdn"]
        version = version_info ["n"]["champion"]
        url = f"{site}/{version}/data/en_US/champion.json"
        return DataDragon._get(url)

    @staticmethod
    def items():
        """ Returns all items in League of Legends. """
        version_info = DataDragon.regions()
        site = version_info["cdn"]
        version = version_info["n"]["item"]
        url = f"{site}/{version}/data/en_US/item.json"
        return DataDragon._get(url)

    @staticmethod
    def summoners():
        """ Returns all summoners in League of Legends. """
        version_info = DataDragon.regions()
        site = version_info["cdn"]
        version = version_info["n"]["summoner"]
        url = f"{site}/{version}/data/en_US/summoner.json"
        return DataDragon._get(url)

    @staticmethod
    def profileicons():
        """ Returns all profileicons in League of Legends. """
        version_info = DataDragon.regions()
        site = version_info["cdn"]
        version = version_info["n"]["profileicon"]
        url = f"{site}/{version}/data/en_US/profileicon.json"
        return DataDragon._get(url)


if __name__ == "__main__":
    d = DataDragon()
    print(d.versions())
    print(d.regions())
    print(d.languages())
    print(d.champions())
    print(d.items())
    print(d.summoners())
    print(d.profileicons())
