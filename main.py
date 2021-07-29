from sys import argv

from _flaskserver import SERVER, SETTINGS

if __name__ == '__main__':
    if not len(argv) > 1: argv.append("_")

    SERVER.run(host="0.0.0.0", port=SETTINGS["SERVER_PORT"])
