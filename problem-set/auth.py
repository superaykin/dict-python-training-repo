import filemngr


def authenticateUser(userName:str, passKey:str) :
    config = filemngr.readDB()
    savedUser = config.get('user')
    savedKey = config.get('key')

    if userName == savedUser and passKey == savedKey :
        return True
    return False
