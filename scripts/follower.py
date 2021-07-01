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

dbFileName    = "twisterDataGuard.pickle" # service database file
nodeUserName  = "twisterdataguard"        # twister wallet (user)
blocksInStep  = 100                       # blocks processing by the one step
squattersStop = 20                        # max users per block. Reset the blocksInStep on this quantity to prevent CPU overload

class MyDb:
    nextBlockHash = False

try:
    from bitcoinrpc.authproxy import AuthServiceProxy
except ImportError as exc:
    sys.stderr.write("Error: install python-bitcoinrpc (https://github.com/jgarzik/python-bitcoinrpc)\n")
    exit(-1)

serverUrl = "http://user:pwd@127.0.0.1:28332"
if len(sys.argv) > 1:
    serverUrl = sys.argv[1]

squattersStopCurrent = squattersStop

twister = AuthServiceProxy(serverUrl)

try:
    db = cPickle.load(open(dbFileName))
except:
    db = MyDb()

print "blockchain reading..."

while True:

    block = twister.getblock(db.nextBlockHash)

    if squattersStopCurrent < 0:
        break

    blocksInStep = blocksInStep - 1

    if blocksInStep < 0:
        break

    print "read block", str(block["height"])# + "\r",

    squattersStopCurrent = squattersStop

    for u in block["usernames"]:
        print "follow", u
        twister.follow(nodeUserName, [u])
        squattersStopCurrent = squattersStopCurrent - 1

    if block.has_key("nextblockhash"):

        db.nextBlockHash = block["nextblockhash"]

        print "save block state."
        cPickle.dump(db, open(dbFileName, "w"))

    else:
        print "database is up to date..."
        break

print "task completed."

else:
    print "operation locked by the running process."
