from modules import notion
import configparser

config=configparser.ConfigParser()
config.read('./config.ini',encoding='utf-8')
notion_token = config['NOTION']['NOTION_TOKEN']
page_id = config['NOTION']['PAGE_ID']
database_id = config['NOTION']['DATABASE_ID']

notion = notion.Notion(notion_token)
str=notion.get_database(database_id)
print(str)
