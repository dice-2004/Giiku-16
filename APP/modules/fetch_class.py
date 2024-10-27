import configparser


class fetcher:
    def __init__(self):
        config = configparser.ConfigParser()
        config.read("../config.ini", encoding="utf-8")
        self.notion_token = config["NOTION"]["NOTION_TOKEN"]
        self.page_id = config["NOTION"]["PAGE_ID"]
        self.database_id = config["NOTION"]["DATABASE_ID"]
        self.discord_token = config["DISCORD"]["DISCORD_TOKEN"]
        self.dix={}
        for section in config.sections():
            if section=='NOTION' or section=='DISCORD':
                # print(section)
                pass
            else:
                for key in config[section]:
                    self.dix[section] = config[section][key]


    def fetch(self):
        return {
            "notion_token": self.notion_token,
            "page_id": self.page_id,
            "database_id": self.database_id,
            "discord_token": self.discord_token,
        }

    def name_fetch(self):
        return dict(self.dix)


if __name__ == "__main__":
    fetch = fetcher()
    config_data = fetch.fetch()
    sss=fetch.name_fetch()
    fetch.write_config('DATABASE_ID','aaa')
