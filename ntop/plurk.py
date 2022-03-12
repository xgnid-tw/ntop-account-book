from plurk_oauth import PlurkAPI

class PlurkHelper:
  plurk = None
  def __init__(self):
    self.plurk = PlurkAPI("PLURK_USER_KEY", "PLURK_USER_SECRET")
    self.plurk.authorize("PLURK_API_TOKEN","PLURK_API_SECRET")

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