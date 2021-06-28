#!/usr/bin/python
#
# Auto-following/reading bot written in Python 2 has a mission to safe distributed data shared in the twister network
# (https://github.com/twisterarmy/twister-data-guard)
# This script based on the official usernameCrawler
# (https://github.com/miguelfreitas/twister-core/blob/master/contrib/usernameCrawler.py)
#
# Downloaded data is cached in a python pickle file, so it may be executed
# again and it won't need to get everything all over again (you may run it
# from cron scripts, for example)

import sys, cPickle

dbFileName = "twisterDataGuard.pickle" # service database file

class MyDb:
    lastBlockHash = 0
    dataLock = False

try:
    db = cPickle.load(open(dbFileName))
    db.dataLock = False
    cPickle.dump(db, open(dbFileName, "w"))
    print "indexing uclocked."
except:
    print "database not created yet."
