import json

# the api_key can be found in: https://steamcommunity.com/dev/apikey

def create_auth_json(api_key):
    obj = {
        "api_key":api_key
    }

    with open('./API_steam.json', 'w') as file_path:
        json.dump(obj, file_path, indent=4)

def load_auth_json():
    with open('./API_steam.json', 'r') as file:
        try:
            api_key = json.load(file)['api_key']
            return api_key
        except:
            raise Exception(f'no have a api_key in {file.name}')

if __name__ == '__main__':
    api_key = input('write api_key here: ')
    create_auth_json(api_key)