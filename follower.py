#!/usr/bin/python
#
# Auto-following/reading bot written in Python 2 that has a mission to safe distributed data shared in the twister network
# (https://github.com/twisterarmy/twister-data-guard)
# This script based on the official usernameCrawler
# (https://github.com/miguelfreitas/twister-core/blob/master/contrib/usernameCrawler.py)
#
# Downloaded data is cached in a python pickle file, so it may be executed
# again and it won't need to get everything all over again (you may run it
# from cron scripts, for example)

import sys, cPickle

dbFileName   = "twisterDataGuard.pickle"
nodeUserName = "twisterdataguard"
blocksInStep = 100

class MyDb:
    lastBlockHash = 0
    dataLock = False

try:
    from bitcoinrpc.authproxy import AuthServiceProxy
except ImportError as exc:
    sys.stderr.write("Error: install python-bitcoinrpc (https://github.com/jgarzik/python-bitcoinrpc)\n")
    exit(-1)

serverUrl = "http://user:pwd@127.0.0.1:28332"
if len(sys.argv) > 1:
    serverUrl = sys.argv[1]

twister = AuthServiceProxy(serverUrl)

try:
    db = cPickle.load(open(dbFileName))
    nextHash = db.lastBlockHash
    dataLock = db.dataLock
except:
    db = MyDb()
    nextHash = twister.getblockhash(0)
    dataLock = db.dataLock

if not dataLock:

    db.dataLock = True
    cPickle.dump(db, open(dbFileName, "w"))

    print "blockchain reading..."

    while True:

        block = twister.getblock(nextHash)
        db.lastBlockHash = block["hash"]

        blocksInStep = blocksInStep - 1
        if blocksInStep < 0:
            db.dataLock = False
            break

        print "read block", str(block["height"])# + "\r",

        for u in block["usernames"]:
            print "follow", u
            twister.follow(nodeUserName, [u])
        if block.has_key("nextblockhash"):
            nextHash = block["nextblockhash"]
        else:
            print "database is up to date..."
            break

    cPickle.dump(db, open(dbFileName, "w"))

    print "task completed."

else:
    print "operation locked by the running process."
