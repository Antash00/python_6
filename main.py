import requests

heroList = ['Thanos', 'Hulk', 'Captain America']


def whoSmarter(heroList):
    heroName = ''
    intellect = 0
    for hero in heroList:
        url = 'https://superheroapi.com/api/2619421814940190/search/' + hero
        resp = requests.post(url).json()
        if int(resp['results'][0]['powerstats']['intelligence']) > intellect:
            heroName = resp['results'][0]['name']
            intellect = int(resp['results'][0]['powerstats']['intelligence'])

    return heroName


print(whoSmarter(heroList))
