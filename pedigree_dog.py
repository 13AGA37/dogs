from dog import Dog

class PedigreeDog(Dog):
    def __init__(self, name, age, color, breed):
        super().__init__(name, age, color)
        self.__breed = breed

    def get_breed(self):
        return self.__breed

    def bark(self):
        return f"Собака {self.get_name()}, породы {self.get_breed()} гавкает громко"

    def go_to_dog_show(self):
        return f"Собака {self.get_name()}, породы {self.get_breed()} участвует в выставке"