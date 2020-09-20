from sys import argv

from _flaskserver import SERVER, SETTINGS

if __name__ == '__main__':
    if not len(argv) > 1: argv.append("_")

    SERVER.run(host=SETTINGS["SERVER_ADDR"] if not argv[1] in ["d", "debug"] else SETTINGS["SERVER_ADDR_DEBUG"], port=SETTINGS["SERVER_PORT"] if not argv[1] in ["d", "debug"] else SETTINGS["SERVER_PORT_DEBUG"])
