import http.client, urllib.parse
from watchdog.events import FileSystemEventHandler
from watchdog.observers import Observer
import os.path
from pathlib import Path
import time
from tzlocal import get_localzone
from datetime import datetime
from dateutil import tz


class agent:
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
    try:
      print("Enter directory to watch.")
      self.DIRECTORY_TO_WATCH = Path(input(">"))

    except Exception as e:
      print(f"Error occured: {e}")

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
        time.sleep(60)
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

    # TODO: change time to UTC
    unlocalisedDatetime = datetime.now()
    dateTimeLocal = unlocalisedDatetime.astimezone(tz = tz.tzlocal()).replace(microsecond=0)
    localZoneName = get_localzone()

    self.eventDateTime = str(dateTimeLocal) + " " + str(localZoneName)

  def sendReport(self, eventDateTime, fileName, event_type, src_path):

    base_host = "192.168.1.5"
    base_port = 9090
    base_url = "/sendReports"
    base_method = "POST"
    params = urllib.parse.urlencode({
        "eventDateTime" : eventDateTime,
        "fileName" : fileName,
        "event_type" : event_type,
        "src_path" : src_path
    })
    headers = {"Content-type": "application/x-www-form-urlencoded", "Accept": "text/plain"}
    # params = urllib.parse.urlencode({eventDateTime : None, fileName : None, event_type : None, src_path : None})
    # TODO: make this HTTPS port 443 later on
    try:
      conn = http.client.HTTPConnection(base_host, base_port)
      conn.request(base_method, base_url, params, headers)
      response = conn.getresponse()
      if (response.status == 200):
        print(f"[+]SUCCESS => response.status: {response.status}\n*********")
      else:
        print(f"[-]FAILIRE => response.status: {response.status}\n*********")
      # data = response.read()
      # print(data)
      conn.close()
    except Exception as ex:
      print(f"ERROR occured: {ex}")

  # @staticmethod
  def on_any_event(self, event):
    """
    [responsible for ransom check on any events]

    Args:
        event ([object]): [object from class FileSystemEventHandler]
    """

    # save file name here
    fileName = os.path.basename(event.src_path)
    # print(f"fileName is now: {fileName}")

    if event.is_directory:
      pass
    else:
      self.sendReport(self.eventDateTime, fileName, event.event_type, event.src_path)


if __name__ == "__main__":
  objectAgent = agent()
  objectAgent.run()