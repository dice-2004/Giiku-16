from modules import fetch_class,notion_class
import discord

fetch=fetch_class.fetcher()
config_data=fetch.fetch()
notion=notion_class.Notion(config_data['notion_token'])

print(config_data)
str=notion.get_database(config_data['database_id'])
print(str)
