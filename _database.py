from sqlite3 import connect

CONNECTION = connect("data/vhack3", check_same_thread=False)
CURSOR = CONNECTION.cursor()
