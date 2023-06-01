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
        if page.section("Special Weapon Effects"):
            spcWepEff = page.section("Special Weapon Effects")
        else:
            spcWepEff = "No special effect could be found."
        retstr = str(summary) +"\n\n" + spcWepEff
        retstr.replace('\'', '')
        retstr.rstrip("\n")

    elif set == 0:
        if page.section("Special Weapon Effects"):
            spcWepEff = page.section("Special Weapon Effects")
        else:
            spcWepEff = "No special effect could be found."
    
        if page.section("Usage & Description"):
            usgDsc1 = page.section("Usage & Description")
            usgDsc = usgDsc1[:usgDsc1.find("Expert")-10]
        else:
            usgDsc = "No information on recommended use could be found."
    
        if page.section("Notes"):
            notes = page.section("Notes")
        else:
            notes = "No special information could be found."
        
        retstr = str(summary) +"\n\n" + str(spcWepEff)+ "\n\n" + str(usgDsc) + "\n\n" + str(notes)
        retstr.replace('\'', '')
        retstr.rstrip("\n")
    else:
        return "Invalid Setting, please use either \"Simple\" or \"Full\"."
    return retstr
