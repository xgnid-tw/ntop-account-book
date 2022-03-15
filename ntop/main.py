from notion import NotionHelper
from pprint import pprint
from plurk import PlurkHelper
import datetime

plurk_to_notion = {
  '7165510': '7aa7c423c2d44521b9a6867ef335fe70', # 奶舞
  '11438146': '5d2e0492c5f4431e9148d1f22273e2d8', # 米豆
  '4879111': '43bcd66a5f8b486b82ba4f62b5a6ea89', # 蓋蓋
  '9871878': '7781270a2f724fddb5f36b6bf5afc999', # 璃花
  '6006557': 'e21ccabb047d4b34b3f91ff66b05c427', # moai
  '3563336': '80e22b3a411e42dc8932dbc352f7e2ef', # 夏
  '4876914': '4f53c00c9eda4e77844aa15264bb9571', # yuyu
  '10782762': 'd87f8a24f9f44946a6f94e595e80e699', # TX
  '14212214': '3c005729f60d4d1586cd4de46ca28799', # 和雨葉
  '8920462': 'a14976072f93430bb86cace175f4a90b', # KBS
  '8885782': 'd2c329d10c2f4109976a1a5dbe8d7e42', # 米哥
  '14064278': '3114c718e79b4fcc9390ad007a9067fc', # Lan
  '8166270': 'bb09a5c83e3d449e989e11bfe702fde2', # 微冰
  '8060037': '7453c93b5dae4eee85ead3424f4bf4dc', # 橘茶
  'angle840616': 'a157d6d62c4d49c892106b6fd0d4c986' # 茶茶
}


p = PlurkHelper()
n = NotionHelper()
today =  datetime.date.today()
if today.day != 1 and today.day != 16:
  exit()

for plurk_id, notion_id in plurk_to_notion.items():
  result = n.get_notpaid(notion_id)
  rows = [] 
  for r in result['results']:
    rows.append(r['properties']['台幣']['number'])
  if sum(rows) > 2000:
    p.call_private_plurk(plurk_id, notion_id)