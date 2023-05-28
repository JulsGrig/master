class Restaurant:
    def __init__(self,name, type, rating):
        self.restaurant_name = name
        self.cuisine_type = type
        self.rating = rating
    def describe_restaurant(self):
        print(" Название ресторана: ",self.restaurant_name,"\n Тип кухни:  ", self.cuisine_type)
    def open_restaurant(self):
        print(" Ресторан открыт")
    def new_rating_restaurant(self, new_rating):
        self.rating = new_rating
        print("Рейтинг ресторана ",self.restaurant_name, "обновлен до",self.rating, "\nОбновлённый рейтинг ресторана - ", self.restaurant_name, "-", self.rating)

r = Restaurant("Кукуруза", "Грузинская кухня", 4)
print("Изначальный рейтинг ресторана", r.restaurant_name, r.rating)
r.new_rating_restaurant(5)