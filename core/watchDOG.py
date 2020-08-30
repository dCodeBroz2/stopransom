import time
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
import os.path
import detectionAPI
from pathlib import Path


class watchDOG:
  """
  [Is responsible for monitoring the events in directory and repeating this method]
  """
  
  print("Enter directory to watch.")
  DIRECTORY_TO_WATCH = Path(input(">"))
  print(f"Directory that is entered for monitoring is: {DIRECTORY_TO_WATCH}")
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
  """[This class is responsible for the ransom appliance itself]

  Args:
      FileSystemEventHandler ([class inheritence]): [inherits from FileSystemEventHandler to use event attribute, like event.src_path and event.event_type, etc]
  """

  def __init__(self):
    # let create an instance of class ransomware
    self.dAPIObj = detectionAPI.detectionAPI() 
    print("*"*20)
    
  # @staticmethod
  def on_any_event(self,event):
    
    # save file name here
    fileName = os.path.basename(event.src_path)
    print(f"fileName is now: {fileName}")
    
    if event.is_directory:
      pass
    else:
      self.dAPIObj.warningRansom(fileName, event.event_type, event.src_path)

