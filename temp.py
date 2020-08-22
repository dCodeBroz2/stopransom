import json
import re
import fnmatch
from progress.bar import Bar

# general variables
badSuccess = 0
goodSuccess = 0
falseNegetive = 0
falsePositive = 0

  
def fixFromPAT2REGEX(pattern):
  # multiple stars are not handled, so handle it here
  # Lets fix, convert from pattern to regex:
  # 1. first convert [-] to asghar, antar, akbar
  # 2. fnmatch.translate() the item
  # 3. again replace asghar, antar, akbar to [-]
  # 4. return values

  if "********" in pattern:
    pattern = pattern.replace("********", "*")
  elif "*********" in pattern:
    pattern = pattern.replace("*********" "*")
    
  # print("pattern is : {}".format(pattern))
  pattern = pattern.replace("[", "asghar")
  pattern = pattern.replace("-", "antar")
  pattern = pattern.replace("]", "akbar")
  
  pattern = fnmatch.translate(pattern)
  
  pattern = pattern.replace("asghar", "\[")
  pattern = pattern.replace("antar", "\-")
  pattern = pattern.replace("akbar", "\]")
  
  # print("pattern is : {}".format(pattern))
  return pattern
  
def ruleChecker():
  bar = Bar('Processing Files', max=4089)
    
  try:
    # this will iterate through the ransomDB.json
    with open("ransomDB.json", "r") as rDB:
      ransomRegEX = json.load(rDB)['filters']
      for items in ransomRegEX:
        item = fixFromPAT2REGEX(items)
        knownBadChecker(item)
        knownGoodChecker(item)        
        bar.next()
      rDB.close()
      bar.finish()
  except:
    pass
  
  print("known bad success rate is : {}".format(badSuccess))
  print("known good success rate is : {}".format(goodSuccess))
  print("known bad false negetive rate is : {}".format(falseNegetive))
  print("known good false positive rate is : {}".format(falsePositive))
      
def knownBadChecker(regEX):
  with open("known_BAD.txt", "r") as knownBAD:
    for item in knownBAD:
      if (re.search(regEX, item) != None):
        # print("Pattern found on knownBAD: {} for rule {}".format(item, regEX))
        badSuccess += 1
        break
      else:
        # print("Pattern not matched on knownBAD: {} for rule {}".format(item, regEX))
        falseNegetive += 1
  knownBAD.close()

def knownGoodChecker(regEX):
  with open("known_GOOD.txt", "r") as knownGOOD:
    for item in knownGOOD:
      if (re.search(regEX, item) != None):
        # print("Pattern found on knownGOOD: {} for rule {}".format(item, regEX))
        falsePositive += 1
        break
      else:
        # print("Pattern not matched on knownBAD: {} for rule {}".format(item, regEX))
        goodSuccess += 1
  knownGOOD.close()


if __name__ == "__main__":
  ruleChecker()

