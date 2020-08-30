import watchDOG

if __name__ == '__main__':
    w = watchDOG.watchDOG()
    w.run()
  

###########################################
#TODO: 

# STEP 1- Write core functionality, the ransom class and class watchdog detector
## a. Core consist of two parts, part one is the core class ransomware and also another class which its job is to detect ransomware, something that we do in watchdog now.
## b. the second component is class reciever which only recieves events and handle them to class ransomDETECT. receiver should take raw events in a function call and also should have a listening port which is going to listen for events that are sent to it.

# STEP 2- Write agent module, for windows, mac and linux. bind and reverse.

# STEP 3- Write GUI for the app, admin should be able to view stats and stuff like that, this is gonna be done through FLASK and REACT with probably mongo or some other DB.

# STEP 4- Write prevention mechanisms, this should order agent to do something.
###########################################