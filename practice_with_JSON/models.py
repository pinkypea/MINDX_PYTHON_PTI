import operator
from data_io import load_json_data, write_json_data
from datetime import datetime

class AnimeItem:
    def __init__(self, anime_id, title, release_date, image=None, rating=None, link=None):
        self.id = anime_id
        self.title = title
        self.release_date = release_date
        self.image = image
        self.rating = float(rating)
        self.link = link

class AnimeDatabase:

    def __init__(self):
        self.anime_item_list = list()
        self.anime_dict_data = load_json_data()
        self.anime_title_list = self.get_title_list()

    def items_to_data(self):
        json_data = list()
        for anime in self.anime_item_list:
            json_data.append(anime.__dict__)
        return json_data

    def load_data(self):
        for anime_dict in self.anime_dict_data:
            anime = AnimeItem(
                anime_id=anime_dict["id"],
                title=anime_dict["title"],
                release_date=anime_dict["release_date"],
                image=anime_dict["image"],
                rating=anime_dict["rating"],
                link=anime_dict["link"],
            )
            self.anime_item_list.append(anime)

    def get_first_item_by_title(self, anime_title):
        for anime_item in self.anime_item_list:
            if anime_item.title == anime_title:
                return anime_item
        # No item found
        return False

    def add_item(self, anime_dict):
        anime_dict["id"] = len(self.anime_item_list)
        new_item = AnimeItem(
            anime_id=anime_dict["id"],
            title=anime_dict["title"],
            release_date=anime_dict["release_date"],
            image=anime_dict["image"],
            rating=anime_dict["rating"],
            link=anime_dict["link"],
        )
        self.anime_item_list.append(new_item)
        self.anime_dict_data.append(anime_dict)
        write_json_data(self.anime_dict_data)

    def edit_item(self, edit_title, new_dict):
        matched = self.get_first_item_by_title(edit_title)
        if matched:
            matched.update(new_dict)
            self.anime_dict_data = self.items_to_data()
            write_json_data(self.anime_dict_data)

    def delete_item(self, delete_title):
        matched = self.get_first_item_by_title(delete_title)
        if matched:
            self.anime_item_list.remove(matched)
            self.anime_dict_data = self.items_to_data()
            write_json_data(self.anime_dict_data)

    def search_by_title(self, search_title) -> list[AnimeItem]:
        matched_items = []
        for anime_item in self.anime_item_list:
            if search_title in anime_item.title.lower():
                matched_items.append(anime_item)

        return matched_items

    def sort_item_by_rating(self, top=None):
        self.anime_item_list = sorted(
            self.anime_item_list, key=operator.attrgetter("rating"), reverse=True
        )
        if top:
            return self.anime_item_list[top]

    def sort_item_by_title(self, top=None):
        self.anime_item_list = sorted(
            self.anime_item_list, key=operator.attrgetter("title")
        )
        if top:
            return self.anime_item_list[top]

    def sort_item_by_title(self, top=None):
        self.anime_item_list = sorted(
            self.anime_item_list, key=operator.attrgetter("title")
        )
        if top:
            return self.anime_item_list[top]

    def sort_item_by_date(self, top=None):
        self.anime_item_list = sorted(
            self.anime_item_list,
            key=lambda x: format_date(x.release_date),
            reverse=True,
        )
        if top:
            return self.anime_item_list[top]

    def get_title_list(self):
        titles = [anime["title"] for anime in self.anime_dict_data]
        return titles
