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

import sys

nodeUserName = "twisterdataguard" # twister wallet (user)
readMaxPosts = 1000000            # posts reading limit per each following user

try:
    from bitcoinrpc.authproxy import AuthServiceProxy
except ImportError as exc:
    sys.stderr.write("Error: install python-bitcoinrpc (https://github.com/jgarzik/python-bitcoinrpc)\n")
    exit(-1)

serverUrl = "http://user:pwd@127.0.0.1:28332"
if len(sys.argv) > 1:
    serverUrl = sys.argv[1]

twister = AuthServiceProxy(serverUrl)

followingList = twister.getfollowing(nodeUserName)

for u in followingList:
    print "reading", u, "..."
    print twister.getposts(100000, [{"username":u}])
