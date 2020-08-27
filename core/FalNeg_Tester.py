import json
import re
import fnmatch
from progress.bar import Bar

 
def counterStat(opString):
  global bs, gs, fn, fp
  if opString == "bs":
    bs += 1
  elif opString == "gs":
    gs += 1
  elif  opString == "fn":
    fn += 1
  elif opString == "fp":
    fp += 1  


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


def knownBadChecker(regEX):
  badSuccess = 0
  falseNegetive = 0

  try:
    with open("known_BAD.txt", "r") as knownBAD:
      for item in knownBAD:
        if (re.search(regEX, item) != None):
          # print("Pattern found on knownBAD: {} for rule {}".format(item, regEX))
          badSuccess = 1
          counterStat("bs")
          break
        else:
          # print("Pattern not matched on knownBAD: {} for rule {}".format(item, regEX))
          pass
  except Exception as ex:
    print(f"ERROR IN BAD CHECKER: {ex}")
  
  if badSuccess == 0:
    falseNegetive = 1
    counterStat("fn")
    
      
def knownGoodChecker(regEX):
  goodSuccess = 0
  falsePositive = 0
  
  try:
    with open("known_GOOD.txt", "r") as knownGOOD:
      for item in knownGOOD:
        if (re.search(regEX, item) != None):
          # print("Pattern found on knownGOOD: {} for rule {}".format(item, regEX))
          falsePositive = 1
          counterStat("fp")
          break
        else:
          # print("Pattern not matched on knownBAD: {} for rule {}".format(item, regEX))
          pass
  except Exception as ex:
    print(f"ERROR IN GOOD CHECKER: {ex}")
  
  if falsePositive == 0:
    goodSuccess = 1
    counterStat("gs")
    
  
def ruleChecker():
  bar = Bar('Processing Files', max=4089)
  # try:
    # this will iterate through the ransomDB.json
  with open("ransomDB.json", "r") as rDB:
    ransomRegEX = json.load(rDB)['filters']
    for items in ransomRegEX:
      item = fixFromPAT2REGEX(items)
      knownBadChecker(item)
      knownGoodChecker(item)
      
      # lets count them

      bar.next()
    # rDB.close()
    bar.finish()
  # except Exception as ex:
  #   print(f"Error: {ex}")
      
if __name__ == "__main__":
  # public variables:
  bs = 0
  gs = 0
  fn = 0
  fp = 0

  print("Fuzzing test status: \n======================")
  ruleChecker()
  print(f"1. Known Bad SUCCESS ratio: {int(bs/4089*100)}%")
  print(f"2. Known Good SUCCESS ratio: {int(gs/4089*100)}%")
  print(f"3. False Negetive FAILRE ratio: {int(fn/4089*100)}%")
  print(f"4. False Positive FAILURE ratio: {int(fp/4089*100)}%")
