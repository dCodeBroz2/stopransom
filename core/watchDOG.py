import time
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
import os.path
import detectionAPI
from pathlib import Path


class watchDOG:
  """
  [Is responsible for monitoring the events in directory and repeating this method
   It has 2 purposes: 
    1. Testing detection in various phases
    2. Checks anti ransom appliance it self for ransom movement]
  
    Attributes:
      observer: is an object from class Observer
      
    Methods:
    __init__(): initializes the observer class and gets the path to monitor
    getPath(): Gets the path from user
    run(): Recuresively monitors path for events
  """
    
  def __init__(self):
    self.observer = Observer()
    self.getPath()
    
  def getPath(self):
    """
    [Responsible for getting the directory to monitor]
    """

    print("Enter directory to watch.")
    self.DIRECTORY_TO_WATCH = Path(input(">"))   
    # print(f"Directory that is entered for monitoring is: {DIRECTORY_TO_WATCH}")

  def run(self):
    """
    [monitors filesystem events every 5 second]
    """
    
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
  """[This class is responsible for the ransom appliance itself]

  Args:
      FileSystemEventHandler ([class inheritence]): [inherits from FileSystemEventHandler to use event attribute, like event.src_path and event.event_type, etc]
  """

  def __init__(self):
    """
    [initializes an object from class detectionAPI to call its warningRansom method]
    """
    
    # let create an instance of class ransomware
    self.dAPIObj = detectionAPI.detectionAPI() 
    # print("*"*20)
    
  # @staticmethod
  def on_any_event(self,event):
    """
    [responsible for ransom check on any event]

    Args:
        event ([object]): [object from class FileSystemEventHandler]
    """
    
    # save file name here
    fileName = os.path.basename(event.src_path)
    # print(f"fileName is now: {fileName}")
    
    if event.is_directory:
      pass
    else:
      self.dAPIObj.warningRansom(fileName, event.event_type, event.src_path)

