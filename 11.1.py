class Restaurant:
    def __init__(self,name):
        self.restaurant_name = name
        self.cuisine_type = type
    def describe_restaurant(self):
        print(" Название ресторана: ",self.restaurant_name,"\n Тип кухни:  ", self.cuisine_type)
    def open_restaurant(self):
        print(" Ресторан открыт")

newRestaurant = Restaurant("Кукуруза")
newRestaurant.cuisine_type = " Грузинская кухня "
newRestaurant.describe_restaurant()
newRestaurant.open_restaurant()
