def register(username: str = None, password: str = None, mail: str = None):
    """
    :param username: Register Username
    :param password: Register User Password
    :param mail: Register User Mail
    :return: (registered: bool, reason: list)
    """
    if not username or not password or not mail: return False, ["Invalid Arguments"]

    from os import urandom
    from _database import CONNECTION, CURSOR

    if checkRegisterByName(username): return False, ["In-use Username"]

    try:
        token = urandom(11).hex()

        CURSOR.execute("INSERT INTO users (username, password, token, mail) VALUES ('{0}','{1}','{2}','{3}')".format(username, password, token, mail))
        CONNECTION.commit()

        return True, ["Created succesfully", [username, password, token, mail]]

    except:
        pass

    return False, ["Register Error"]


def checkRegisterByName(checkName: str = None):
    """
    :param checkName: Name to check
    :return: (exists: bool)
    """
    if not checkName: return False

    from _database import CURSOR

    for user in CURSOR.execute("SELECT token FROM users WHERE username='{0}'".format(checkName)): return True if len(user) == 1 else False
