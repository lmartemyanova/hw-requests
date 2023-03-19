import requests

class Superheroes:

    def __init__(self, name):
        self.url = 'https://cdn.jsdelivr.net/gh/akabab/superhero-api@0.3.0/api'
        self.name = name
        return

    def get_id(self):
        '''
        GET superhero id by name
        :return: id
        '''
        url = self.url + "/all.json"
        response = requests.get(url)
        all_info = response.json()
        for person in all_info:
            if person['name'] == self.name:
                self.id = person['id']
                return self.id

    def get_powerstats(self):
        '''
        GET superhero powerstats
        :return: powerstats
        '''
        self.get_id()
        url = self.url + "/powerstats/" + str(self.id) + ".json"
        response = requests.get(url)
        powerstats = response.json()
        return powerstats


def compare_intelligence(*args):
    intelligences = {}
    for superhero in [*args]:
        intelligence = superhero.get_powerstats()['intelligence']
        intelligences[superhero.name] = intelligence
    max_intelligence = max(intelligences.values())
    max_hero = ''.join([key for key, value in intelligences.items() if value == max_intelligence])
    res = f'Наибольший интеллект у супергероя {max_hero}: {max_intelligence}'
    return res
