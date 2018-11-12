from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from database_setup import Restaurant, Base, MenuItem, User

engine = create_engine('sqlite:///restaurantmenuwithusers.db')
# Bind the engine to the metadata of the Base class so that the
# declaratives can be accessed through a DBSession instance
Base.metadata.bind = engine

DBSession = sessionmaker(bind=engine)
# A DBSession() instance establishes all conversations with the database
# and represents a "staging zone" for all the objects loaded into the
# database session object. Any change made against the objects in the
# session won't be persisted into the database until you call
# session.commit(). If you're not happy about the changes, you can
# revert all of them back to the last commit by calling
# session.rollback()
session = DBSession()


# Create dummy user
User1 = User(name="Corie Wilson", email="wilsoncorie@udacity.com",
             picture='https://image.shutterstock.com/image-photo/healthy-food-sources-folic-acid-260nw-543889855.jpg')
session.add(User1)
session.commit()


# American Cookies Menu
restaurant1 = Restaurant(user_id=4, name="American Cookies")

session.add(restaurant1)
session.commit()



menuItem1 = MenuItem(user_id=4, name="Ice Cream Cookies Sandwich", description="Small Size Vanilla Ice Cream Cookie Sandwich",
                     price="$12.99", course="Appetizer", restaurant=restaurant1)

session.add(menuItem1)
session.commit()

menuItem2 = MenuItem(user_id=4, name="Chocolate Vegan Cookie", description="Vegan Cookie",
                     price="$4.99", course="Entree", restaurant=restaurant1)

session.add(menuItem2)
session.commit()

menuItem3 = MenuItem(user_id=4, name="Gummie Bears", description="topping to add to any cookie",
                     price="$2.99", course="Dessert", restaurant=restaurant1)

session.add(menuItem3)
session.commit()

menuItem4 = MenuItem(user_id=4, name="Dr. Pepper", description="Small Dr. Pepper",
                     price="$1.99", course="Beverage", restaurant=restaurant1)

session.add(menuItem4)
session.commit()


# Chocolate World Menu
restaurant1 = Restaurant(user_id=4, name="Chocolate World")

session.add(restaurant1)
session.commit()



menuItem1 = MenuItem(user_id=4, name="Assorted Mix of Chocolate", description="Small Size of Assorted Mix of Chocolate",
                     price="$15.99", course="Appetizer", restaurant=restaurant1)

session.add(menuItem1)
session.commit()

menuItem2 = MenuItem(user_id=4, name="Vegan Chocolate Milkshake", description="Vegan Chocolate Milkshake",
                     price="$4.99", course="Entree", restaurant=restaurant1)

session.add(menuItem2)
session.commit()

menuItem3 = MenuItem(user_id=4, name="Chocolate Chip Sprinkles", description="fresh baked cake with free birthday signage",
                     price="$0.99", course="Dessert", restaurant=restaurant1)

session.add(menuItem3)
session.commit()

menuItem4 = MenuItem(user_id=4, name="Coke", description="Small Coke",
                     price="$1.99", course="Beverage", restaurant=restaurant1)

session.add(menuItem4)
session.commit()


# Craz Yogurt Menu
restaurant1 = Restaurant(user_id=4, name="Craz Yogurt")

session.add(restaurant1)
session.commit()



menuItem1 = MenuItem(user_id=4, name="Yogurt Waffle Cone", description="Yogurt waffle cone",
                     price="$7.99", course="Appetizer", restaurant=restaurant1)

session.add(menuItem1)
session.commit()

menuItem2 = MenuItem(user_id=4, name="Vegan Yogurt Milkshake", description="Vegan Yogurt Milkshake",
                     price="$4.99", course="Entree", restaurant=restaurant1)

session.add(menuItem2)
session.commit()

menuItem3 = MenuItem(user_id=4, name="Fruit", description="Fresh fruit for topping",
                     price="$1.99", course="Dessert", restaurant=restaurant1)

session.add(menuItem3)
session.commit()

menuItem4 = MenuItem(user_id=4, name="Milk", description="Small Milk",
                     price="$1.99", course="Beverage", restaurant=restaurant1)

session.add(menuItem4)
session.commit()


# Ice Cream World Menu
restaurant1 = Restaurant(user_id=4, name="Ice Cream World")

session.add(restaurant1)
session.commit()



menuItem1 = MenuItem(user_id=4, name="Ice Cream Cake", description="Medium Ice Cream Cake. Best seller is cookies and cream.",
                     price="$27.99", course="Appetizer", restaurant=restaurant1)

session.add(menuItem1)
session.commit()

menuItem2 = MenuItem(user_id=4, name="Vegan Chips", description="Vegan Chips Birthday Cake Ice Cream flavor",
                     price="$4.99", course="Entree", restaurant=restaurant1)

session.add(menuItem2)
session.commit()

menuItem3 = MenuItem(user_id=4, name="Chocolate Chips", description="fresh chocolate chips topping",
                     price="$13.99", course="Dessert", restaurant=restaurant1)

session.add(menuItem3)
session.commit()

menuItem4 = MenuItem(user_id=4, name="Water", description="Large water/Free refills",
                     price="$0.99", course="Beverage", restaurant=restaurant1)

session.add(menuItem4)
session.commit()


# Krisby Cream Menu
restaurant1 = Restaurant(user_id=4, name="Krisby Cream")

session.add(restaurant1)
session.commit()



menuItem1 = MenuItem(user_id=4, name="Assorted Box of DoughNuts", description="12 Assorted Doughnuts",
                     price="$2.99", course="Appetizer", restaurant=restaurant1)

session.add(menuItem1)
session.commit()

menuItem2 = MenuItem(user_id=4, name="Vegan Chocolate Milkshake", description="Vegan Chocolate Milkshake",
                     price="$4.99", course="Entree", restaurant=restaurant1)

session.add(menuItem2)
session.commit()

menuItem3 = MenuItem(user_id=4, name="Cinnamon", description="fresh cinnamon for coffee and lattee",
                     price="$13.99", course="Dessert", restaurant=restaurant1)

session.add(menuItem3)
session.commit()

menuItem4 = MenuItem(user_id=4, name="Coffee", description="Small Coffee",
                     price="$5.99", course="Beverage", restaurant=restaurant1)

session.add(menuItem4)
session.commit()

#Pastries Oh Pastries Menu
restaurant1 = Restaurant(user_id=4, name="Pastries Oh Pastries")

session.add(restaurant1)
session.commit()

#Pie Face Menu
restaurant1 = Restaurant(user_id=4, name="Pie Face")

session.add(restaurant1)
session.commit()

#Pudding Shop Menu
restaurant1 = Restaurant(user_id=4, name="Pudding Shop")

session.add(restaurant1)
session.commit()

#Smoothies King Menu
restaurant1 = Restaurant(user_id=4, name="Smoothies King")

session.add(restaurant1)
session.commit()

#Sweet Breads Menu
restaurant1 = Restaurant(user_id=4, name="Sweet Breads")

session.add(restaurant1)
session.commit()

#We Bake Cakes Menu
restaurant1 = Restaurant(user_id=4, name="We Bake Cakes")

session.add(restaurant1)
session.commit()
print "added menu items!"

