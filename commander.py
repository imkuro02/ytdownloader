# commander.py returns small letters, and int or str

def command(command):
    
    try:
        command = int(command)
    except:
        pass

    if isinstance(command,int): 
        command = int(command)
    else:
        command = command.lower()

    return command
