from notion_client import Client
import os
import json

class Notion:
    def __init__(self, token):
        self.client = Client(auth=token)


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
            dead_line_exceed = pro_data.get('期限越え判定').get('formula').get('boolean')

            for okperson_name in okpersons:
                okperson=okperson_name.get('name')
                okperson=okperson.replace("\u3000"," ")
                person.append(okperson)

            out_data={"title":title,"select":select,"timeschedul":timeschedul,"person":person}
            return_data.append(out_data)
        return return_data #期限越え判定 ＝dead_line_exceed

    def get_page_id(self, database_id, title):
        notion_data = self.get_pages(database_id)
        if notion_data is None:  # 追加: notion_dataがNoneの場合の処理
            return None

        for data in notion_data["results"]:
            title_notif = notion_data.get("results")[0].get('properties').get('名前').get('title')[0].get('plain_text').replace("\u3000"," ")

            if title_notif == title:
                return data["id"].replace("-", "")
        return None

    def create_page(self, database_id,title,):
        return self.client.pages.update()


    # def update(self, database_id: str, **kwargs: Any) -> SyncAsync[Any]:
    #     """Update an existing database as specified by the parameters.

    #     *[🔗 Endpoint documentation](https://developers.notion.com/reference/update-a-database)*
    #     """  # noqa: E501
    #     return self.parent.request(
    #         path=f"databases/{database_id}",
    #         method="PATCH",
    #         body=pick(
    #             kwargs,
    #             "properties",
    #             "title",
    #             "description",
    #             "icon",
    #             "cover",
    #             "is_inline",
    #         ),
    #         auth=kwargs.get("auth"),
    #     )


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
    # str=[]
    # str=notion.get_notion_data(database_id)
    # print(str)
    str = notion.get_page_id(database_id, "データベース中間")
    print(str)
