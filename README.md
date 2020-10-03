# stopransom
1. install deps:
 a. watchdog
 b. colored
 c. requests
2. run agenthandler on server and grab server's ip address
3. configure server's ip address on agent.py and run it, address the directory 
 you like to watch for ransomware movements.
4. the agent detects ransom files and reports back to the agenthandler 
 server and then ransom file events are stored in a local sqlite file for further investigation.
