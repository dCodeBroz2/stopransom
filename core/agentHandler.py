from flask import Flask, request
import DBConn
import detectionAPI

class agentHandler:
  host = '0.0.0.0'
  port = '9090'
  deBug = False

  def __init__(self):
    """
    class agent handler is responsible for receiving agent event logs
    and storing them in DB.
    """

  app = Flask('test')
  @app.route('/sendReports', methods=['POST'])
  def parseRequestDat():
    """
    Parse request from agent and write to DB
    """
    objDB = DBConn.DBConn()
    dAPIObj = detectionAPI.detectionAPI()

    req = request.form

    eventDateTime=req['eventDateTime']
    fileName=req['fileName']
    event_type=req['event_type']
    src_path=req['src_path']

    # print(req)
    # print(eventDateTime, fileName, event_type, src_path)
    # return req
    if (dAPIObj.ransomDetect(eventDateTime, fileName, event_type, src_path)):
      # if True, the file is a ransomware, otherwise get over it
      objDB.writeToDB(eventDateTime, fileName, event_type, src_path)
    else:
      pass

    # lets tell them we got the event
    return '200'

  app.run(host, port, deBug)
