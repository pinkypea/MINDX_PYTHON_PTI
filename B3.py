class AnimeItem:
    def __init__(self, id, title, release_date, rating, link):
        self.id = id
        self.title = title
        self.release_date = release_date
        self.rating = rating
        self.link = link
    
    def update(self, title, release_date, rating, link):
        self.title = title
        self.release_date = release_date
        self.rating = rating
        self.link = link

anime1 = AnimeItem("011", "Naruto", "2000", 8.5, "abc.naruto.com")

anime1.update("Dragon ball", "1990", 8.0, "abc.dragon_ball.com")
print(anime1.id)
print(anime1.title)
print(anime1.release_date)
print(anime1.rating)
print(anime1.link)

# Dictionary datatype
# Create a dictionary datatype
my_dict = {
    "name": "kien",
    "age": 40,
    "city": "Hanoi",
    "job": "Developer"
}

# Truy cập các phần tử trong từ điển
print("Name: " + my_dict["name"])

# Thay đổi giá trị của một key
my_dict["age"] = 60
print("Age: ", my_dict["age"])

# Thêm giá trị mới
my_dict["gender"] = "male"

# Xoá một phần tử từ từ điển
del my_dict["city"]

print(my_dict)

class AnimeItem:
    def __init__(self, id, title, release_date, rating, link):
        self.id = id
        self.title = title
        self.release_date = release_date
        self.rating = rating
        self.link = link
    
    def update(self, new_data: dict):
        # Thông tin nào không có thì không update
        for attribute, value in new_data.items():
            if value:
                setattr(self, attribute, value)

anime1 = AnimeItem("011", "Naruto", "2000", 8.5, "abc.naruto.com")
anime2 = AnimeItem("002", "Dragon ball", "1990", 8.0, "dragonball")
anime3 = AnimeItem("003", "Fairy tale", "1995", 9.0, "fairytale")
animeItems = [anime1, anime2, anime3]
# Duyệt danh sách
for anime in animeItems:
    print(anime.title)

# Thêm phần tử
anime4 = AnimeItem("004", "One Piece", "1998", 10.0, "onepiece")
animeItems.append(anime4)
for anime in animeItems:
    print(anime.title)
new_data = {
    
    
    "rating": 8.0,
    "link": "abc.dragonball.com"
}
anime.update(new_data)
print(anime.id)
print(anime.title)
print(anime.release_date)
print(anime.rating)
print(anime.link)

