def login(token: str = None, password: str = None):
    """
    :param token: Login User Token
    :param password: Login User Password
    :return: (logged: bool, reason: list)
    """
    if not token or password: return False, ["Invalid Arguments"]

    from _database import CURSOR
    for user in CURSOR.execute("SELECT * FROM users WHERE token='{0}'".format(token)): return True, ["Logged-In"] if user[2] == password else False, ["Invalid Password", "Invalid Token"]
