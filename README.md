# twister-data-guard

Twister is a community driven microblogging platform, that have a distributed database, stored between the independent DHT nodes by the Following relationships.  

At this moment it has a low online activity, so that toolkit written to safe the users data as the part of our history, memories, loses and wins.  

This toolkit should be runned with the interactive twister-core node, to collect a live, not dumped content using the twisterverse protocol and return it to the other nodes. So if you want to participate - contribute to this project, or run the existing scripts provided.  

### Usage

Add py scripts to the crontab task according to your server powers and the current network activity.  
@ twisterdataguard node is open sourced, including the profile database and the private key for recovery needs:  
`KymxWUUeX7ZwEdkbVs78KAVvERBZz8YXGEfzmjqSDk68HTSXRQPa`  
Node would be runned using the actual profile slice provided in the .twister directory with all the actual data collected.  
File twisterDataGuard.pickle contain the latest hash of it block indexed.  

### Roadmap

1. follower.py - search and auto follow all users in the twister blockchain (completed)  
2. reader.py - loading and auto reading public post of the followed users (todo)  
3. publisher.py - sending data collected into the DHT to make database visible for the other nodes (todo, may be integrated in 1/2 scripts)  
3. unlock.py - temporary solution, that used to unlock the indexing on the twisterd crashes (issue #2)  
