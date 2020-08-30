import re
import fnmatch
import ransomWare


class detectionAPI:
  def __init__(self):
    
    """
    This is class is going to check an event and for now prints if ransomware 
    is detected.
    """
    self.extList = ransomWare.ransomWare()
  
  def fixRegEx(self, item):
    """[file pattern to regex converter]

    Args:
        item ([string]): [gets a string which is a pattern from ransomDB.json and fix it
         to match in regex format, actually converts from pattern to regex]

    Returns:
        [string]: [returns regex format of pattern]
    """

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

    return regexRAW

  def ransomDetect(self, eventFileName, eventType, eventPath):
    """[Main ransomware detection method which can be used anywhere]

    Args:
        eventFileName ([str]): [file name in event]
        eventType ([str,CRUD]): [create, read, update, delete]
        eventPath ([str]): [full path of the file in event]

    Returns:
        [boolean]: [returns true if it is a ransom or false if it is not.]
    """

    try:
      for item in self.extList.fileTypes:
        regexRAW = self.fixRegEx(item)
        
        # item is fixed lets check if ransom or not
        if (re.search(regexRAW, eventFileName)):
          return True
        continue
      
      return False

    except Exception as ex:
        print("ERROR at : {}".format(ex))
        print("Searched ITEM was:{} ||||| searched REGEXT was: {} ".format(eventFileName, regexRAW))

        
  def warningRansom(self, eventFileName, eventType, eventPath):
    """[Prints warning on console]

    Args:
        eventFileName ([str]): [the name of the file in event]
        eventType ([str, mod, del, cre]): [type of the event, CRUD]
        eventPath ([type]): [the full path of the file in event]
    """
    
    redColor = '\033[1;31;48m'
    endColoring = '\033[1;37;0m'
    underLine = '\033[4;37;48m'
    
    if (self.ransomDetect(eventFileName, eventType, eventPath)):
      # It is a ransomware let print warning
      print(redColor + f"Suspeciuos Ransom file or format detected in action (\"{eventType}\"): " + underLine +  f"{eventPath}" + endColoring)
    else:
      print("NOT A RANSOMWARE!!!!!!!!!!!!!!!!!!!!!!!!!!!")
