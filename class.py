

#  Create a basic class
class Book:
    def __init__(self,title):
        self.title = title

# create instance of the class
b1 = Book("Brave new world")
b2 = Book("War and peace")

# print class and property
print (b1)
print (b1.title)
print (b2.title)