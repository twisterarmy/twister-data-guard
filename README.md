# twister-data-guard

Twister is a community driven microblogging platform, that have a distributed database, stored between the independent DHT nodes by the Following relationships.  

At this moment it has a low online activity, so that toolkit written to safe the users data as the part of our history, memories, loses and wins.  

This toolkit should be runned with the interactive twister-core node, to collect a live, not dumped content using the twisterverse protocol and return it to the other nodes. So if you want to participate - contribute to this project, or run the existing scripts provided.  

### Usage

Add py scripts to the crontab task according to your server powers and the current network activity.  
@ twisterdataguard node is open sourced, including the profile database and the private key for data operating needs:  

`KymxWUUeX7ZwEdkbVs78KAVvERBZz8YXGEfzmjqSDk68HTSXRQPa`  

Existing Node would be launched using the actual profile slice provided in the .twister directory (soon) with all the data collected and prepared by latest twisterd release.  
Launching the new node, requires a lot of the time and/or CPU resources. Also, part of the data may be losten in DHT/BitTorrent network.  

File twisterDataGuard.pickle contain the latest number of the block indexed. Will be publiched on the next profile slice.  

If you have any question, visit our feedback page to get a support:  
https://github.com/twisterarmy/twister-data-guard/issues  

### Roadmap

1. follower.py - search and auto follow all users in the twister blockchain (completed)  
2. reader.py - loading and auto reading public post of the followed users (todo)  
3. publisher.py - sending data collected into the DHT to make database visible for the other nodes (todo, may be integrated in 1/2 scripts)  
3. unlock.py - temporary solution, that used to unlock the indexing on the twisterd crashes (issue #2)  
