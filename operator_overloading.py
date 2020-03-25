class Books:
    def __init__(self,pages):
        self.pages = pages

    def __add__(self, other):
        return self.pages + other.pages
    
b1 = Books(100)
b2 = Books(200)

print (b1+b2) # b1.__add__(b2) also this can be used for diffrent classes

