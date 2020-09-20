def getUserCoinsByID(userID: int = None):
    """
    :param userID: Search User ID
    :return: (completed: bool, coins: int)
    """
    if not userID: return False, ["Invalid Arguments"]

    from _database import CURSOR
    for coins in CURSOR.execute("SELECT coins FROM users WHERE ID_={0}".format(userID)): return True if coins[0] > 0 else False, coins[0] if coins[0] > 0 else 1


def getUsersByQuery(query: str = None):
    """
    :return: (completed: bool, users: list)
    """
    if not query: return False, ["Invalid Arguments"]

    from _database import CURSOR

    returnUsersArray = list()
    for user in CURSOR.execute(query): returnUsersArray.append(user)
    return True, returnUsersArray
