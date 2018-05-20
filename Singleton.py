class Singleton(type):
    _instances = {}
    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super(Singleton, cls).__call__(*args, **kwargs)
            return cls._instances[cls]
        else:
            pass

class Object(metaclass=Singleton):
    def __init__(self, name):
        self.name = name;

firstObject = Object("nameOfFirstObject")
secondObject = Object("nameOfSecondObject")
try:
    secondObject.name
except:
    print ("There can only be one instance of type: {0}.".format(type(firstObject)))
else:
    print ("There are two instances of the same class.")
