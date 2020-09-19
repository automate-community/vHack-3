def attack(userTK: int = None, objectiveID: int = None, force: bool = False):
    """
    :param userTK: User Token
    :param objectiveID: Objective numeric ID
    :param force: Force attack
    :return: (completed: bool, reason: list)
    """

    if not userTK or not objectiveID: return False, ["Invalid Arguments"]

    from _database import CURSOR, CONNECTION
    from random import randint
    from _users import getUserCoinsByID

    if (randint(0, 100) == randint(0, 10)) or force:
        if checkIfActiveShieldByID(objectiveID) and not force: return False, ["Active Shield"]

        try:
            if not getUserCoinsByID(objectiveID)[0]: return False, ["Not Enought Coins"]
            stealAmount = randint(1, getUserCoinsByID(objectiveID)[1] if getUserCoinsByID(objectiveID)[0] else 2)

            CURSOR.execute("UPDATE users SET coins=coins+{1} WHERE token='{0}'".format(userTK, stealAmount))
            CURSOR.execute("UPDATE users SET coins=coins-{1} WHERE ID_={0}".format(objectiveID, stealAmount))
            CONNECTION.commit()

            return createShield(objectiveID, 3600 if (stealAmount > 10000) else 1800 if (5000 < stealAmount < 10000) else 900)

        except:
            pass

    return False, ["Unlucky", "Internal Error"]


def createShield(objectiveID: int = None, duration: int = None):
    """
    :param objectiveID: Objective numeric ID
    :param duration: Shield duration in seconds
    :return: (created: bool, reasons: list)
    """
    if not duration or not objectiveID: return False, ["Invalid Arguments"]

    from _database import CURSOR, CONNECTION
    from time import time

    try:
        CURSOR.execute("UPDATE users SET shield={1} WHERE ID_={0}".format(objectiveID, time() + duration))
        CONNECTION.commit()
        return True, ["Attacked"]

    except:
        pass

    return False, ["Shield Error"]


def checkIfActiveShieldByID(objectiveID: int = None):
    """
    :param objectiveID: Objective Numeric ID to search
    :return: (active: bool)
    """

    if not objectiveID: return False, ["Invalid Arguments"]

    from _database import CURSOR

    from time import time

    for userShield in CURSOR.execute("SELECT shield FROM users WHERE ID_={0}".format(objectiveID)): return False if time() >= userShield[0] else True


def getShieldInactiveTimeByID(objectiveID: int = None):
    """
    :param objectiveID: Objective Numeric ID to search
    :return: (completed: bool, Objective Shield Data: list)
    """
    if not objectiveID: return False, ["Invalid Arguments"]

    from _database import CURSOR
    from time import ctime

    for userShield in CURSOR.execute("SELECT shield FROM users WHERE ID_={0}".format(objectiveID)): return True, ctime(userShield[0]).split(" ")[1:5]
