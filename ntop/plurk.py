from plurk_oauth import PlurkAPI

class PlurkHelper:
  plurk = None
  def __init__(self):
    self.plurk = PlurkAPI("ZU9ie5fgOf96", "W7M0ELaafqlj8Vy4ynnOT7jlNU9QyUXN")
    self.plurk.authorize("LnpIjEaQ6V65","55bkYLXrEpGcbohmBu31g9ds1iI1twxN")

  def call_private_plurk(self,target):
    self.plurk.call()

  def call(self):
    self.plurk = PlurkAPI("ZU9ie5fgOf96", "W7M0ELaafqlj8Vy4ynnOT7jlNU9QyUXN")
    self.plurk.authorize("LnpIjEaQ6V65","55bkYLXrEpGcbohmBu31g9ds1iI1twxN")
    result = self.plurk.callAPI('/APP/Timeline/plurkAdd', options={
      'content' : "test12345",
      'qualifier' : ':',
      'limited_to' : "[5574239]"
    });
    if result == None :
      print(self.plurk.error())