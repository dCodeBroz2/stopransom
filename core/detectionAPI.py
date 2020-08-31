import re
import ransomWare
from colored import fg, attr

class detectionAPI:
  def __init__(self):
    """
    [This class uses ransomWare extList attribute for its methods.]
      attributes: 
        extList: List of regexed ransom patterns
      methods:
        ransomDetect(): checks for ransom, returns true or false
        warningRansom(): prints or later dumps to web gui detections
        
    """
    self.extList = ransomWare.ransomWare()

  def ransomDetect(self, eventFileName, eventType, eventPath):
    """
    [Main ransomware detection method which can be used anywhere]
    Args:
        eventFileName ([str]): [file name in event]
        eventType ([str,CRUD]): [create, read, update, delete]
        eventPath ([str]): [full path of the file in event]

    Returns:
        [boolean]: [returns true if it is a ransom or false if it is not.]
    """

    try:
      for regexRAW in self.extList.fileTypes:
        # regexRAW = self.extList.patternToREGEX(item)
        # item is fixed lets check if ransom or not
        if (re.match(regexRAW, eventFileName)):
          return True
        continue
      
      return False

    except Exception as ex:
        print("ERROR at : {}".format(ex))
        print("Searched ITEM was:{} ||||| searched REGEXT was: {} ".format(eventFileName, regexRAW))

  def warningRansom(self, eventFileName, eventType, eventPath):
    """
    [Prints warning on console or web GUI]

    Args:
        eventFileName ([str]): [the name of the file in event]
        eventType ([str, mod, del, cre]): [type of the event, CRUD]
        eventPath ([type]): [the full path of the file in event]
    """
    boldFont = attr('bold')
    greenColor = fg('green')
    redColor = fg('red')
    endColoring = attr('reset')
    underLine = attr('underlined')
    blinked = attr('blink')
    pinkColor = fg('deep_pink_4c')
    violetRed = fg('medium_violet_red')
    
    if (self.ransomDetect(eventFileName, eventType, eventPath)):
      # It is a ransomware let print warning
      print(boldFont + redColor + "Suspeciuos Ransom file or format detected:" + pinkColor + f"\nACTION: (\"{eventType}\")" + underLine + redColor + violetRed + f"\nFULL PATH: {eventPath}" + endColoring + "\n=============================") 
    else:
      print(greenColor + "NOT A RANSOMWARE !" + "\n=============================")
