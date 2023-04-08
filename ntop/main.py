import json
import sys
import datetime
from os import getenv

from dotenv import load_dotenv
from notion import NotionHelper
from rabbit import RabbitHelper

load_dotenv()

notion_helper = NotionHelper()
# get discord id to notion id list
result = notion_helper.get_discord_list(getenv('NOTION_ID_LIST'))
discord_to_notion = {}
for r in result['results']:
    discord_to_notion[r['properties']['discord_id']['title'][0]['plain_text']] = r['properties']['notion_id']['rich_text'][0]['plain_text']


rabbit_publisher = RabbitHelper()

# check each notion database whethere there is someone's debit over 2000 and two month
for discord_id, notion_id in discord_to_notion.items():
    # get not paid records
    result = notion_helper.get_notpaid(notion_id)
    rows = []
    for r in result['results']:
        rows.append(r['properties']['台幣']['number'])
        # calcuate sum
    if sum(rows) > 2000:
        notion_url = f'https://www.notion.so/{notion_id}'
        #rabbit_publisher.send(json.JSONEncoder().encode({
        #    'user_id': int(discord_id), 
        #    'message': f'[欠費提醒] {notion_url} (回訊息機器人看不到，如果有漏登聯絡一下XG) ',
        #}))
        rabbit_publisher.send(json.JSONEncoder().encode({
            'user_id': 374867612519366657, #temperary change to me
            'message': f'[欠費提醒] {notion_url} (回訊息機器人看不到，如果有漏登聯絡一下XG) ',
        }))

rabbit_publisher.close()
