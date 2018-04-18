class Singleton(type):
    _instances = {}
    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super(Singleton, cls).__call__(*args, **kwargs)
            return cls._instances[cls]
        else:
            pass

class Alien(metaclass=Singleton):
    def __init__(self, name):
        self.name = name;

myAlien = Alien("PiuViu")
mySecondAlien = Alien("E.T.")
try:
    mySecondAlien.name
except:
    print ("There can only be one alien: named {0}.".format(myAlien.name))
else:
    print ("Now there are two aliens.")