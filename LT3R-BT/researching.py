import requests as rq
from bs4 import BeautifulSoup

def lookUp(weapon,  game)->str:
    game.lower()
    url = 'http://' + game+'.fandom.com/wiki/'+weapon
    resp = rq.get(url)
    
    if resp.status_code == 403:
        return "Unable to access page: Access Restricted."
    elif resp.status_code == 404:
        return "Unable to access page: Page does not exist."
    elif resp.status_code == 200:
        soup = BeautifulSoup(resp.text, 'html.parser')
        
