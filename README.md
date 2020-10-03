# stopransom
This is an educational project for detecting and in the future 
 stoping ransomwares on any operating system or storages.
For now it only stores the ransom files that are created on a target directory inside a DB.

#TODO:
 1. Add graphical interface with react-js
 2. Add prevention mechanisms, kill pid or stop the handle that is doing ransom.

SETUP:
1. install deps:
 a. watchdog
 b. colored
 c. requests
2. run agenthandler on server and grab server's ip address
3. configure server's ip address on agent.py and run it, address the directory 
 you like to watch for ransomware movements.
4. the agent detects ransom files and reports back to the agenthandler 
 server and then ransom file events are stored in a local sqlite file for further investigation.
