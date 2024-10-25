from notion_client import Client
import os
import json

class Notion:
    def __init__(self, token):
        self.client = Client(auth=token)

    def get_database(self, database_id):
        return self.client.databases.retrieve(database_id)

    def get_pages(self, database_id):
        return self.client.databases.query(database_id)

    def get_notion_data(self, database_id):
        # template =[{"title":value,"select":value,"timeschedul":value,"okperson":value},{"title":value,"select":value,"timeschedul":value,"okperson":value},...]
        return_data=[]
        notion_data = self.get_pages(database_id)
        datas=notion_data['results']
        for data in datas:
            pro_data = data.get('properties')
            title=pro_data.get('名前').get('title')[0].get('plain_text')
            title = title.replace("\u3000"," ")

            select_property = pro_data.get('セレクト')
            select = select_property.get('select').get('name') if select_property and select_property.get('select') else None
            if select is not None:
                select =select.replace("\u3000"," ")

            timeschedul=pro_data.get('提出期限').get('date').get('start')
            if "T" in timeschedul:
                timeschedul=timeschedul.split("T")[0]
            timeschedul = timeschedul.replace("-","/")
            timeschedul=timeschedul.replace("\u3000"," ")

            okpersons=pro_data.get('完了済').get('people')
            person=[]

            for okperson_name in okpersons:
                okperson=okperson_name.get('name')
                okperson=okperson.replace("\u3000"," ")
                person.append(okperson)
            # print(title,select,timeschedul,person)
            # print(person)
            out_data={"title":title,"select":select,"timeschedul":timeschedul,"person":person}
            return_data.append(out_data)
        return return_data
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
    str=[]
    str=notion.get_notion_data(database_id)
    print(str)
