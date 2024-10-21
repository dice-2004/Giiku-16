from notion_client import Client
import os

class Notion:
    def __init__(self, token):
        self.client = Client(auth=token)

    def get_database(self, database_id):
        return self.client.databases.retrieve(database_id)

    def get_pages(self, database_id):
        return self.client.databases.query(database_id)

    # def create_page(self, database_id, properties):
    #     return self.client.pages.create(parent={"database_id": database_id}, properties=properties)


if __name__ == "__main__":
    # from dotenv import load_dotenv

    # load_dotenv()
    # notion_token = str(os.getenv("NOTION_TOKEN"))
    # page_id = str(os.getenv("PAGE_ID"))
    # database_id = str(os.getenv("DATABASE_ID"))


    import configparser
    config=configparser.ConfigParser()
    config.read('../config.ini',encoding='utf-8')
    notion_token = config['NOTION']['NOTION_TOKEN']
    page_id = config['NOTION']['PAGE_ID']
    database_id = config['NOTION']['DATABASE_ID']

    notion = Notion(notion_token)
    str=notion.get_database(database_id)
    print(str)
