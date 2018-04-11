#!/usr/bin/env python

import sys
from socialpy.funcs.setup import run
from socialpy.funcs.data import runserver, deletedatabase, setupdatabase

FUNCS = {
    'setup': run,
    'runserver': runserver,
    'deletedb': deletedatabase,
    'setupdb': setupdatabase
}

def print_help():
    print("""
    The funcs module
    ----------------
    This is all for scripting from the command-line.

    help      - display this text
    setup     - setup the gateway
    runserver - run the data-server
    setupdb   - setup db
    deletedb  - delete the db
    """)



if len(sys.argv) != 2 or sys.argv[1] not in FUNCS:
    print_help()
    exit()

FUNCS[sys.argv[1]]()
