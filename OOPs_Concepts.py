class Animal():
    # Constructor
    def __init__(self, name, sound):
        self.name = name          # public attribute
        self.__sound = sound      # private attribute (Encapsulation)

    # Method to access private attribute
    def make_sound(self):
        print("Make Sound:",self.__sound)

    # Abstract method (Abstraction)
    def show_info(self):
        raise NotImplementedError()
# Inheritance
class Dog(Animal):
    def __init__(self, name, breed):
        # Calling parent constructor
        super().__init__(name, "Woof!")
        self.breed = breed

    # Polymorphism (method overriding)
    def show_info(self):
        print("Name:",self.name)
        print("Breed:",self.breed)
        super().make_sound()
# Creating object
dog1 = Dog("Buddy", "Golden Retriever")
dog1.show_info()
