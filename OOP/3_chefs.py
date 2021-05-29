class AbstractCook:
    food, drink = None, None
    def __init__(self):
        self.foods = {self.food: 0, self.drink: 0}

    def add_food(self, food_amount, food_price):
        '''adds to the client's order the value of the food which he had chosen'''
        self.foods[self.food] +=  food_amount * food_price

    def add_drink(self, drink_amount,drink_price):
        '''adds to the client's order the value of the drink which he had chosen'''
        self.foods[self.drink] +=  drink_amount * drink_price

    def total(self):
        '''returns a string like: 'Foods: 150, Drinks: 50, Total: 200',
        and for the each chef instead of the Foods and Drinks will be the national food and drink that he’s used'''
        all_sum = self.foods[self.food] + self.foods[self.drink]
        return f"{self.food}: {self.foods[self.food]}, {self.drink}: {self.foods[self.drink]}, Total: {all_sum}"                


# You are the owner of a cafe where 3 chefs work: a JapaneseCook, RussianCook and ItalianCook. 
# Each of them can prepare the national food and beverage.
# Subclasses are the children of an AbstractCook.
    
class ItalianCook(AbstractCook):
    food, drink = 'Pizza', 'Juice'
    
class JapaneseCook(AbstractCook):
    food, drink = 'Sushi', 'Tea'
     
class RussianCook(AbstractCook):
    food, drink = 'Dumplings', 'Compote'
     

# Example

client_1 = JapaneseCook()
client_1.add_food(2, 20)
client_1.add_drink(5, 4)
client_1.total() == "Sushi: 40, Tea: 20, Total: 60"

client_2 = RussianCook()
client_2.add_food(1, 40)
client_2.add_drink(5, 20)
client_2.total() == "Dumplings: 40, Compote: 100, Total: 140"

client_3 = ItalianCook()
client_3.add_food(2, 20)
client_3.add_drink(2, 10)
client_3.total() == "Pizza: 40, Juice: 20, Total: 60"
