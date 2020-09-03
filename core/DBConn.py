import sqlite3
from pathlib import Path

class DBConn:
  """class for handling ransomed hosts and files events
  """
  def __init__(self):

    if (self.createConnection() != None):
      self.dbConn = self.createConnection()
      print("[+]Successfully connected to DB")
    else:
      print("[-]Database Connection not possible working offline!")

    # database is connected, lets create tables if not exists
    self.createDB_Table()

  def createConnection(self):
    """ create a database connection to the SQLite database
    specified by db_file
    :return: Connection object or None
    """
    conn = None
    try:
      db_file = Path("db/ransomSTATS.DB")
      conn = sqlite3.connect(db_file)
      # if (conn != "None"):
      #   # print("[+]Connected to database successfully!")
      #   return conn
      # else:
      return conn
    except Exception as e:
      print(f"Error occured: {e}")

  def createDB_Table(self):

    # Note that sqlite creates database if not exists!, so we don't check
    # create db and/or connect to it
    # conn = self.createConnection()
    c = self.dbConn.cursor()

    # Create table
    # TODO: Get time from event
    c.execute('''CREATE TABLE IF NOT EXISTS RansomedFiles(
        ID INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
        TIME TIMESTAMP DEFAULT CURRENT_TIMESTAMP NOT NULL,
        EventFileName varchar(10),
        EventType varchar(10),
        EventPath varchar(10)
      )''')

  def writeToDB(self, eventDateTime, eventFileName, eventType, eventPath):
    """
    [Responsible for writing to database, for now sqlite db]

    Args:
        eventFileName ([str]): [name of the file in event]
        eventType ([str]): [type of the event, CRUD]
        eventPath ([str]): [path of the file in event]
    """
    conn = self.createConnection()
    c = conn.cursor()

    c.execute("INSERT INTO RansomedFiles (TIME, EventFileName, EventType, EventPath) VALUES (?,?,?,?)", (eventDateTime, eventFileName, eventType, eventPath))
    conn.commit()
    conn.close()

    # print("[+]Wrote to the database successfully!")