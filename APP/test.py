from modules import fetch_class
from modules import notion_class

fetch = fetch_class.fetcher()
config_data = fetch.fetch()

database_id = config_data["database_id"]
notion_token = config_data["notion_token"]

nc = notion_class.Notion(notion_token)


def main():
    try:
        data = nc.get_notion_data(database_id)
        if len(data) >= 3:
            for i in range(3):
                print(data[i]["person"])
        else:
            print("Insufficient data to display 3 items.")
    except Exception as e:
        print(f"An error occurred: {e}")

main()
