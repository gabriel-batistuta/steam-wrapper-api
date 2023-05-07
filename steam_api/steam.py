import json
import requests
import xml.etree.ElementTree as ET

'''
Hello, this is a unofficial wrapper library for steam API

the documentation of API can be found in: https://developer.valvesoftware.com/wiki/Steam_Web_API#Formats

'''

class Steam:

    def __init__(self, api_key: str, standard_format=None):
        '''

        API_KEY
        the api_key is your api_key of steam, can be found in https://steamcommunity.com/dev/apikey

        STANDART_fORMAT
        the standard_format is the format you want from the api, the default is JSON but this library support JSON and XML formats

        '''
        self.api_key = api_key
        if standard_format != None:
            self.standard_format = standard_format
        else:
            self.standard_format = 'json'

    def _get_content(self, url):
        response = requests.get(url)
        if response.content:
            content = response.content

            return content
        else:
            raise Exception('bad request, status_code: {0}'.format(response))

    def _set_format(self, format):
        if format == None:
            format = self.standard_format
        return format

    def _update_with_language(self, url, language):
        if language != None:
            url += f'&l={language}'
        
        return url

    def _check_format(self, content):
        try:
            json.loads(content)
            return 'json'
        except ValueError:
            try:
                ET.fromstring(content)
                return 'xml'
            except ValueError:
                raise Exception(f'format with error {ValueError}')

    def write_content(self, content, file_path):
        with open(file_path, 'w', encoding='utf-8') as file:
            if self._check_format(content) == 'json':
                content = json.loads(content)
                json.dump(content, file, indent=4)

            elif self._check_format(content) == 'xml':
                xml = ET.fromstring(content)
                ET.indent(xml)
                file_path.write(xml)

    def get_news_game(self, app_id, count=3, max_length=300, format=None):
        format = self._set_format(format)

        url = f'http://api.steampowered.com/ISteamNews/GetNewsForApp/v0002/?appid={app_id}&count={count}&maxlength={max_length}&format={format}'
        news_game = self._get_content(url)

        return news_game

    def get_global_achievement_percentages_for_app(self, game_id, format=None):
        format = self._set_format(format)

        url = f'http://api.steampowered.com/ISteamUserStats/GetGlobalAchievementPercentagesForApp/v0002/?gameid={game_id}&format={format}'
        achievement_percentages = self._get_content(url)

        return achievement_percentages

    def get_player_summaries(self, steam_id):
        url = f'http://api.steampowered.com/ISteamUser/GetPlayerSummaries/v0002/?key={self.api_key}&steamids={steam_id}'
        player_summaries = self._get_content(url)

        return player_summaries

    def get_friend_list(self, steam_id, format=None):
        format = self._set_format(format)

        url = f'http://api.steampowered.com/ISteamUser/GetFriendList/v0001/?key={self.api_key}&steamid={steam_id}&relationship=friend&format={format}'
        friend_list = self._get_content(url)

        return friend_list
    
    def get_player_achievements(self, steam_id, app_id, language=None):
        url = f'http://api.steampowered.com/ISteamUserStats/GetPlayerAchievements/v0001/?appid={app_id}&key={self.api_key}&steamid={steam_id}'
        
        url = self._update_with_language(url, language)
        player_achievements = self._get_content(url)

        return player_achievements
    
    def get_user_stats_for_game(self, steam_id, app_id):
        url = f'http://api.steampowered.com/ISteamUserStats/GetUserStatsForGame/v0002/?appid={app_id}&key={self.api_key}&steamid={steam_id}'
        user_stats_for_game = self._get_content(url)

        return user_stats_for_game
    
    def get_owned_games(self, steam_id, include_appinfo=False, include_played_free_games=False,  format=None):
        format = self._set_format(format)
        url = f'http://api.steampowered.com/IPlayerService/GetOwnedGames/v0001/?key={self.api_key}&steamid={steam_id}&format={format}'
        if include_appinfo == True:
            url += '&include_appinfo'
        if include_played_free_games == True:
            url+= '&include_played_free_games'
        owned_games = self._get_content(url)

        return owned_games
    
    def get_recently_played_games(self, steam_id, count=None, format=None):
        format = self._set_format(format)
        url = f'http://api.steampowered.com/IPlayerService/GetRecentlyPlayedGames/v0001/?key={self.api_key}&steamid={steam_id}&format={format}'
        if count != None:
            url += f'&count={count}'
        recently_played_games = self._get_content(url)

        return recently_played_games