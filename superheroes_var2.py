import requests

def compare_intelligence(*args):
    url = 'https://cdn.jsdelivr.net/gh/akabab/superhero-api@0.3.0/api/all.json'
    response = requests.get(url).json()
    intelligences = {}
    for superhero in response:
        for name in [*args]:
            if name == superhero['name']:
                intelligence = superhero['powerstats']['intelligence']
                intelligences[name] = intelligence
    max_intelligence = max(intelligences.values())
    max_hero = ''.join([key for key, value in intelligences.items() if value == max_intelligence])
    res = f'Наибольший интеллект у супергероя {max_hero}: {max_intelligence}'
    return res


print(compare_intelligence('Hulk', 'Captain America', 'Thanos'))
