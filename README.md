# synco
NAT Traversing, Scheduled File Synchronization Program


# design

- Dumb server, smart clients
- Server holds onto a status page of where all files are located / complete and partial
- files are moved in chunks of 1kb
- client starts up and requests latest states, then checks local for changes, then requests transactions 

Actions:

GET Records

Client:
1) connects to server
2) fetch records - server gives transaction information of changes that have happened
3) check with local files for changes - check who came first, server changes or our local changes (look at file edit times)
4) FOREACH file
4a) request lock on file to be changed
4b) download all changes that came first
4c) apply local changes
4d) submit change request to server

