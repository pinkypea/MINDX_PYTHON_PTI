import json

class AnimeItem:
    def __init__(self, id, title, release_date, image=None, rating=None, link=None):
        self.id = id
        self.title = title
        self.release_date = release_date
        self.image = image
        self.rating = float(rating) if rating else 0
        self.link = link

# anime1 = AnimeItem(1, "One Piece", "01/01/2001")
# # Ghi dữ liệu sang json
# with open("data.json", "w") as file:
#     json.dump(anime1.__dict__, file)

# # Đọc dữ liệu từ json
# with open("data.json", "r") as file:
#     data = json.load(file)
#     loaded_data = AnimeItem(data["id"], data["title"], data["release_date"])
# print(loaded_data.release_date)

with open("data.json", "r") as file:
    anime_data = json.load(file)
anime_item_list = list()
for anime_item_dict in anime_data:
    anime = AnimeItem(
        id=anime_item_dict["id"],
        title=anime_item_dict["title"],
        release_date=anime_item_dict["release_date"],
        rating=anime_item_dict["rating"],
        link=anime_item_dict["link"],
    )
    anime_item_list.append(anime)

print(len(anime_item_list))
