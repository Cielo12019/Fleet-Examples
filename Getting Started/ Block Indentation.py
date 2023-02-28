a = b = 2
def my_function():
    b = 14
    return b

b=my_function()
print (b)

if a > b : print(a)
else: print(b)

#An empty block causes an IndentationError. Use pass (a command that does nothing) when you have a block with
#no content:

def will_be_implemented_later():
    pass

will_be_implemented_later()

# subclass
# class myObj is a subclass of myAge

class myAge:
    age = 36

class myObj(myAge):
    name = "John"
    age = myAge

m = issubclass(myObj, myAge)

print(m)

# instance


# Python program to demonstrate
# instance methods


class shape:

    # Calling Constructor
    def __init__(self, edge, color):
        self.edge = edge
        self.color = color

    # Instance Method
    def finEdges(self):
        return self.edge

    # Instance Method
    def modifyEdges(self, newedge):
        self.edge = newedge


circle = shape(0, 'red')
square = shape(4, 'blue')

# Calling Instance Method
print("No. of edges for circle: "+ str(circle.finEdges()))

# Calling Instance Method
square.modifyEdges(6)

print("No. of edges for square: "+ str(square.finEdges()))