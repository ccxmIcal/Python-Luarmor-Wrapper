import requests
import json

with open("configuration\data.json", "r") as f:
    cfgdata = json.loads(f.read())
    APIKEY = cfgdata["api-key"]
    PROJECTID = cfgdata["project-id"]



class Luarmor:
    def __init__(self):
        self._base_url = 'https://api.luarmor.net'
        self._key_details = self._base_url + '/v3/keys/{}/details'.format(APIKEY)
        self._key_stats   = self._base_url + '/v3/keys/{}/stats'.format(APIKEY)
        self._user_end    = self._base_url + '/v3/projects/{}/users'.format(PROJECTID)
        self._headers     = {"Authorization": APIKEY}

    def get_key_stats(self):
        return requests.get(self._key_stats).json()
    
    def get_key_details(self):
        return requests.get(self._key_details).json()

    def get_entry(self, user = None):
        if isinstance(user, str) and user != None:
            data = requests.get(self._user_end + '?discord_id={}'.format(str(user)), headers = self._headers)
            if data.status_code != 200:
                return False
            data = data.json()
            data = data["users"][0]
            return data
        else:
            data = requests.get(self._user_end, headers = self._headers)
            if data.status_code != 200:
                return False
            return data

    def create_entry(self, jsondata = None):
        if jsondata == None:
            jsondata = {}
        data = requests.post(self._user_end, headers = self._headers, json = jsondata)
        if data.status_code != 200:
            return False
        data = data.json()
        data = data['user_key']
        return data

    def set_entry(self, jsondata):
        data = requests.patch(self._user_end, headers = self._headers, json = jsondata)
        if data.status_code != 200:
            return False
        return data

    def del_entry(self, key):
        data = requests.delete(self._user_end + '?user_key={}'.format(str(key)), headers = self._headers)
        if data.status_code != 200:
            return False
        return data

    def reset_hwid(self, key):
        body = {"user_key": str(key), "force": True}
        data = requests.post(self._user_end + '/resethwid', headers = self._headers, json = body)
        if data.status_code != 200:
            return False
        return data

    def link_discord(self, key, discordid):
        body = {"user_key": str(key), "discord_id": str(discordid), "force": True}
        data = requests.post(self._user_end + '/linkdiscord', headers = self._headers, json = body)
        if data.status_code != 200:
            return False
        return data