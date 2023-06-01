import researching
import creator

def handle_response(message) -> str:
    supported_games = ["borderlands"]
    supported = False
    p_message = message.lower()
    splitted = message.split("\n")
    
    if p_message == '!help':
        return "`Commands:\n/search - Has it search for the weapon you want to know about depending if you want the full relevant information or a short summary. The proper way to ask is in this format:\n\t\"/search\n\t[weapon]\n\t[game]\n\t[full/simple]\"\n\nPlease note that the weapon and game fields are case sensitive.\nTo create a new line use shift+enter or, if on mobile, use enter.\nIf you want the message to be a direct message then use (?) before the command. [?/search]\n\n?creator - Gives information about the creator of the bot in a private message.`"
    
    if p_message == 'creator':
        return creator.description()

    for i in supported_games:
        if splitted[2].lower().find(i) > -1:
            supported = True
    if supported == False:
        return "Game is not supported. Please inquire about these games:\n\t-Borderlands series"
    
    set = None
    if len(splitted) == 4:
        if splitted[3].lower() == 'simple':
            set = 1
        elif splitted[3].lower() == 'full':
            set = 0
    
    if splitted[0].lower() == '/search':
        return researching.research(splitted[1],  splitted[2],  set)
        
    return ""
