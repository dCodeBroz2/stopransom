import time
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
import ransomWare
import os.path
import colored
import re
import fnmatch

class watchDOG:
  print("Enter directory to watch.")
  DIRECTORY_TO_WATCH = input(">")
  
  def __init__(self):
    self.observer = Observer()

  def run(self):
    print("[+]Watching directory closely!")
    event_handler = Handler()
    self.observer.schedule(event_handler, self.DIRECTORY_TO_WATCH, recursive=True)
    self.observer.start()
    try:
      while True:
        time.sleep(5)
    except:
      self.observer.stop()
      print ("Error")

    self.observer.join()

class Handler(FileSystemEventHandler):

  def __init__(self):
    # let create an instance of class ransomware
    self.extList = ransomWare.ransomWare()
    print("*"*20)
    
  # @staticmethod
  def on_any_event(self,event):
    
    # save file name here
    fileName = os.path.basename(event.src_path)
    
    # TODO: Sometimes file create also flags as file modification, so for 1 event 1 alerts are fired
          # fix this or make it conditional. Sometimes ommiting things like this might lead to bypasses.

    if event.is_directory:
      return None

    elif event.event_type == 'created':
      # Take any action here when a file is first created.
#      print("Received created event - {}".format(event.src_path))

      try:
        for item in self.extList.fileTypes:
          # multiple stars are not handled, so handle it here
          if "********" in item:
            item = item.replace("********", "*")
          elif "*********" in item:
            item = item.replace("*********" "*")
      
          # print("pattern is : {}".format(pattern))
          item = item.replace("[", "asghar")
          item = item.replace("-", "antar")
          item = item.replace("]", "akbar")
          
          regexRAW = fnmatch.translate(item)
          
          regexRAW = regexRAW.replace("asghar", "\[")
          regexRAW = regexRAW.replace("antar", "\-")
          regexRAW = regexRAW.replace("akbar", "\]")
          
          # item is fixed lets check if ransom or not
          if (re.search(regexRAW, fileName)):
            print("\033[1;31;48m" + "Suspeciuos Ransom file or format detected in (CREATE): " + "\033[4;37;48m" +  "{}".format(event.src_path) + "\033[1;37;0m")
            print("PATTERN MATCHED WAS : {}".format(regexRAW))
            break
      except Exception as ex:
        print("ERROR at : {}".format(ex))
        print("Searched ITEM was:{} ||||| searched REGEXT was: {} ".format(fileName, regexRAW))

    elif event.event_type == 'modified':
      # Taken any action here when a file is modified.
 #     print("Received modified event - {}".format(event.src_path))
      
      try:
        for item in self.extList.fileTypes:
          # multiple stars are not handled, so handle it here
          if "********" in item:
            item = item.replace("********", "*")
          elif "*********" in item:
            item = item.replace("*********" "*")
      
          # print("pattern is : {}".format(pattern))
          item = item.replace("[", "asghar")
          item = item.replace("-", "antar")
          item = item.replace("]", "akbar")
          
          regexRAW = fnmatch.translate(item)
          
          regexRAW = regexRAW.replace("asghar", "\[")
          regexRAW = regexRAW.replace("antar", "\-")
          regexRAW = regexRAW.replace("akbar", "\]")
          
          if (re.search(regexRAW, fileName)):
            print("\033[1;31;48m" + "Suspeciuos Ransom file or format detected in (MODIFIED): " + "\033[4;37;48m" +  "{}".format(event.src_path) + "\033[1;37;0m")
            print("PATTERN MATCHED WAS : {}".format(regexRAW))
            break
      except Exception as ex:
        print("ERROR at : {}".format(ex))
        print("Searched ITEM was:{} ||||| searched REGEXT was: {} ".format(fileName, regexRAW))

    elif event.event_type == 'deleted':
      # Taken any action here when a file is modified.
#      print("Received deleted event - {}".format(event.src_path))

      try:
        for item in self.extList.fileTypes:
          # multiple stars are not handled, so handle it here
          if "********" in item:
            item = item.replace("********", "*")
          elif "*********" in item:
            item = item.replace("*********" "*")
      
          # print("pattern is : {}".format(pattern))
          item = item.replace("[", "asghar")
          item = item.replace("-", "antar")
          item = item.replace("]", "akbar")
          
          regexRAW = fnmatch.translate(item)
          
          regexRAW = regexRAW.replace("asghar", "\[")
          regexRAW = regexRAW.replace("antar", "\-")
          regexRAW = regexRAW.replace("akbar", "\]")
          
          if (re.search(regexRAW, fileName)):
            print("\033[1;31;48m" + "Suspeciuos Ransom file or format detected in (DELETE): " + "\033[4;37;48m" +  "{}".format(event.src_path) + "\033[1;37;0m")
            print("PATTERN MATCHED WAS : {}".format(regexRAW))
            break
      except Exception as ex:
        print("ERROR at : {}".format(ex))
        print("Searched ITEM was:{} ||||| searched REGEXT was: {} ".format(fileName, regexRAW))
