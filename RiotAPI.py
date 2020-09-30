import requests # used for making requests to the riot API

class RiotAPI:
    server = "https://euw1.api.riotgames.com"

    def __init__(self, token):
        self.token = {"api_key": token}

    def _createMessage(self, response):
        errors = {
            400: "Bad request",
            401: "Unauthorized",
            403: "Forbidden",
            404: "Data not found",
            405: "Method not allowed",
            415: "Unsupported media type",
            429: "Rate limit exceeded",
            500: "Internal server error",
            502: "Bad gateway",
            503: "Service unavailable",
            504: "Gateway timeout"
        }
        # response received without errors
        ok_message_code = 200
        if response.status_code == ok_message_code:
            return response.json()
        else:
            return errors[response.status_code]

    def _getResponse(self, suffix):

        url = f"{self.server}{suffix}"
        response = requests.get(url, params=self.token)

        message = self._createMessage(response)
        return response.json()


    # SUMMONER-V4
    def summoner_by_account(self, encryptedAccountId):
        response = self._getResponse(f"/lol/summoner/v4/summoners/by-account/{encryptedAccountId}")
        return response

    def summoner_by_name(self, summonerName):
        response = self._getResponse(f"/lol/summoner/v4/summoners/by-name/{summonerName}")
        return response

    def summoner_by_puuid(self, encryptedPUUID):
        response = self._getResponse(f"/lol/summoner/v4/summoners/by-puuid/{encryptedPUUID}")
        return response

    def summoner(self, encryptedSummonerId):
        response = self._getResponse(f"/lol/summoner/v4/summoners/{encryptedSummonerId}")
        return response


    # CHAMPION-MASTERY-V4
    def all_champion_mastery(self, encryptedSummonerId):
        response = self._getResponse(f"/lol/champion-mastery/v4/champion-masteries/by-summoner/{encryptedSummonerId}")
        return response

    def champion_mastery(self, encryptedSummonerId, championId):
        response = self._getResponse(f"/lol/champion-mastery/v4/champion-masteries/by-summoner/{encryptedSummonerId}/by-champion/{championId}")
        return response

    def total_mastery(self, encryptedSummonerId):
        response = self._getResponse(f"/lol/champion-mastery/v4/scores/by-summoner/{encryptedSummonerId}")
        return response

    # CHAMPION-V3
    def champion_rotations(self):
        response = self._getResponse(f"/lol/platform/v3/champion-rotations")
        return response


    # LOL-STATUS-V3
    def shard_data(self):
        response = self._getResponse(f"/lol/status/v3/shard-data")
        return response


    # LOR-RANKED-V1
    def leaderboards(self):
        response = self._getResponse(f"/lor/ranked/v1/leaderboards")
        return response


    # ACCOUNT-V1
    def account(self, puuid):
        response = self._getResponse(f"/riot/account/v1/accounts/by-puuid/{puuid}")
        return response

    def account_by_riot_id(self, gameName, tagLine):
        response = self._getResponse(f"/riot/account/v1/accounts/by-riot-id/{gameName}/{tagLine}")
        return response

    def shard_by_puuid(self, game, puuid):
        response = self._getResponse(f"/riot/account/v1/active-shards/by-game/{game}/by-puuid/{puuid}")
        return response
