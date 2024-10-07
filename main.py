from dog import Dog
from pedigree_dog import PedigreeDog

def main():
    dog = Dog("Бобик", 3, "черный")
    print(dog.bark())

    pedigree_dog = PedigreeDog("Тузик", 5, "коричневый", "Пудель")
    print(pedigree_dog.bark())
    print(pedigree_dog.go_to_dog_show())

if __name__ == "__main__":
    main()