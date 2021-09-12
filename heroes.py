import requests


class Hero:
    def __init__(self, token: str):
        self.token = token

    def max_hero_int(self, hero_list):
        url = 'https://superheroapi.com/api/' + self.token + '/search/'
        max_int = 0
        hero_name = ''
        for hero in hero_list:
            response = requests.get(url + hero)
            data = response.json()
            for elm in data['results']:
                if int(elm['powerstats']['intelligence']) > max_int:
                    max_int = int(elm['powerstats']['intelligence'])
                    hero_name = elm['name']
        print(f'{hero_name} - герой с наибольшим интелектом({max_int})')