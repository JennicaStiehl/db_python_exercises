class Animal:
    __name = None
    __sound = ""
    __height = 0
    __weight = 0

    def __init__(self, name, height, weight, sound):
        self.__name = name
        self.__height = height
        self.__weight = weight
        self.__sound = sound

    def set_name(self, name):
        self.__name = name

    def get_name(self):
        return self._name

    def set_height(self, height):
        self.__height = height

    def get_height(self):
        return self._height

    def set_weight(self, weight):
        self.__weight = weight

    def get_weight(self):
        return self._weight

    def set_sound(self, sound):
        self.__sound = sound

    def get_sound(self):
        return self._sound

    def toString(self):
        return "{} is {} cm tall and {} kilograms and is the sound {}".format(self.__name,
                                                                            self.__height,
                                                                            self.__weight,
                                                                            self.__sound)
cat = Animal('Whiskers', 33, 10, 'brown')
print(cat.toString())

class Dog(Animal):
    __owner = None

    def __init__(self, name, height, weight, sound, owner):
        self.__owner = owner
        super(Dog, self).__init__(name, height, weight, sound)

    def set_owner(self, owner):
        self.__owner = owner

    def get_owner(self):
        return self.__owner

    def get_type(self):
        print("We are using a dog obj")

    def multiple_sounds(self, how_many=None):
        if how_many is None:
            print(self.get_sound())
        else:
            print(self.get_sound()* how_many)

    def toString(self):
        return "{} is {} cm tall and {} kilograms and makes the sound {} and has an owner named {}.".format(self.__name,
                                                                            self.__height,
                                                                            self.__weight,
                                                                            self.__sound,
                                                                            self.__owner)


dog = Dog("Todd", 34, 12, "bark", "Derek")
print(dog.toString())
