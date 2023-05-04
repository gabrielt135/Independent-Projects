import researching

def handle_response(message) -> str:
    p_message = message.lower()
    splitted = message.split("\n")
    
    set = None
    if len(splitted) == 4:
        if splitted[3].lower() == 'simple':
            set = 1
        elif splitted[3].lower() == 'full':
            set = 0
    
    if splitted[0].lower() == '/search':
        return researching.research(splitted[1],  splitted[2],  set)
        
    if p_message == '!help':
        return "`This is a help message that you can modify.`"
        
    return ""
