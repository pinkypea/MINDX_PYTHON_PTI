class Anime:
    def __init__(self, id, title):
        self.id = id
        self.title = title

class AnimeList:
    def __init__(self):
        self.anime_list = []

    def search_by_title_or_id(self, query):
        for anime in self.anime_list:
            if anime.title == query or anime.id == query:
                return anime
        return None
    
    def add_anime(self, anime):
        self.anime_list.append(anime)

    def update_anime(self, title, new_title):
        anime = self.search_by_title_or_id(title)
        if anime:
            anime.title = new_title

    def remove_anime(self, title):
        anime = self.search_by_title_or_id(title)
        if anime:
            self.anime_list.remove(anime)

# Example:
if __name__ == "__main__":
    anime_db = AnimeList()

    anime_db.add_anime(Anime(1, "Naruto"))
    anime_db.add_anime(Anime(2, "One Piece"))
    anime_db.add_anime(Anime(3, "Dragon Ball Z"))

    print("Initial anime list:")
    for anime in anime_db.anime_list:
        print(anime.title)

    anime_db.update_anime("Naruto", "Boruto")
    print("\nUpdated anime list:")
    for anime in anime_db.anime_list:
        print(anime.title)

    anime_db.remove_anime("One Piece")
    print("\nAnime list after removing 'One Piece':")
    for anime in anime_db.anime_list:
        print(anime.title)
