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


def getUsersForAttack():
    """
    :return: (completed: bool, users: dict)
    """
    from _attack import getShieldInactiveTimeByID, checkIfActiveShieldByID

    returnDictionary = dict()
    for user in getUsersByQuery("SELECT ID_,username,shield,coins,validated,diamonds FROM users")[1]:
        if user[4] == 1:
            returnDictionary[user[0]] = {
                "ID_": user[0],  # USER ID INDEX
                "username": user[1],  # USER NAME INDEX
                "shield": user[2],  # USER SHIELD INDEX
                "shield_inactive": "-".join(getShieldInactiveTimeByID(user[0])[1]),  # USER SHIELD INACTIVE TIME
                "can_attack": not checkIfActiveShieldByID(user[0]),  # USER SHIELD ACTIVE
                "coins": user[3],  # USER COINS INDEX
                "diamonds": user[-1]  # USER DIAMONDS INDEX
            }

    return True, returnDictionary
