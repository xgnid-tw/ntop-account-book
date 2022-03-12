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

  def call_private_plurk(self,target="5574239", notion_id="GX-Ver-4-e196bc4b09694d9993d9738e1065dec0"):
    notionUrl = "https://www.notion.so/" + notion_id
    options={
      'content' : "[提醒]目前累積金額超過2000且兩個月以上囉，請直接點選 "+ notionUrl + " (notion) 確認",
      'qualifier' : 'wants',
      'limited_to' : "["+ target +"]"
    }
    self.plurk.callAPI('/APP/Timeline/plurkAdd', options=options)