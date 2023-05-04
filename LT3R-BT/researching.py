import fandom as fd
from bs4 import BeautifulSoup
import requests as rq

def getSum(url)->str:
    retval =""
    request = rq.get(url)
    soup = BeautifulSoup(request.content, "html.parser")
    pagePart = soup.find(class_= "mw-parser-output")
    deleteList = pagePart.find_all(["table","dl", "aside", "h2", "ul"])
    for i in deleteList:
        i.decompose()
    splitter = pagePart.get_text().lstrip("\n").split("\n")
    retval = splitter[0]
    return retval

def research(weapon,  game,  set)->str:
    page = ""
    splits = game.split(' ')
    parenthesis = "(" + game + ")"
    if len(splits) > 1:
        if splits[0].lower() == "the":
            fd.set_wiki(splits[0].lower()+splits[1].lower())
        else:
            fd.set_wiki(splits[0].lower())
        pages = fd.search(weapon, splits[0].lower())
        for i in pages:
            if i[0].find(parenthesis) > -1 and i[0].find(weapon) > -1:
                page = fd.page(pageid = i[1])
                break
            else:
                page = fd.page(pageid = pages[0][1])
    else:
        fd.set_wiki(game)
        pages = fd.search(weapon,  game)
        for i in pages:
            if i[0].find(parenthesis) > -1 and i[0].find(weapon) > -1:
                page = fd.page(pageid = i[1])
                break
            else:
                page = fd.page(pageid = pages[0][1])
        
    summary = getSum(page.url)
        
    if set == 1:
        retstr = str(summary) +"\n\n" + str(page.section("Special Weapon Effects"))
        retstr.replace('\'', '')
        retstr.rstrip("\n")
    elif set == 0:
        retstr = str(summary) +"\n\n" + str(page.section("Special Weapon Effects")) + "\n\n" + str(page.section("Usage & Description")) + "\n\n" + str(page.section("Notes"))
        retstr.replace('\'', '')
        retstr.rstrip("\n")
    else:
        return "Invalid Setting, please use either \"Simple\" or \"Full\"."
    return retstr
