from plurk_oauth import PlurkAPI
import os

class PlurkHelper:
  plurk = None
  def __init__(self):
    PLURK_USER_KEY    = os.environ['PLURK_USER_KEY']
    PLURK_USER_SECRET = os.environ['PLURK_USER_SECRET']
    PLURK_API_TOKEN   = os.environ['PLURK_API_TOKEN']
    PLURK_API_SECRET  = os.environ['PLURK_API_SECRET']
    self.plurk = PlurkAPI(PLURK_USER_KEY, PLURK_USER_SECRET)
    self.plurk.authorize(PLURK_API_TOKEN,PLURK_API_SECRET)

  def call_private_plurk(self,target):
    self.plurk.call()

  def call(self):
    result = self.plurk.callAPI('/APP/Timeline/plurkAdd', options={
      'content' : "test12345",
      'qualifier' : ':',
      'limited_to' : "[5574239]"
    });
    if result == None :
      print(self.plurk.error())