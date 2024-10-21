import configparser
class fetcher:
    def __init__(self):
        config=configparser.ConfigParser()
        config.read('./config.ini',encoding='utf-8')
        self.notion_token = config['NOTION']['NOTION_TOKEN']
        self.page_id = config['NOTION']['PAGE_ID']
        self.database_id = config['NOTION']['DATABASE_ID']
        self.discord_token = config['DISCORD']['DISCORD_TOKEN']

    def fetch(self):
        return {'notion_token':self.notion_token,'page_id':self.page_id,'database_id':self.database_id,'discord_token':self.discord_token}
