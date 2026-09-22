#!/usr/bin/env python3
"""Demonstrate inheritance and polymorphism with a small example."""


class Animal:
    """Represent a generic animal."""

    def speak(self):
        """Return the sound this animal makes."""
        return "Some sound"


class Dog(Animal):
    """Represent a dog."""

    def speak(self):
        """Return the sound a dog makes."""
        return "Woof"


class Cat(Animal):
    """Represent a cat."""

    def speak(self):
        """Return the sound a cat makes."""
        return "Meow"


animals = [Dog(), Cat(), Dog()]

for animal in animals:
    print(animal.speak())

dog = Dog()

print(isinstance(dog, Dog))
print(isinstance(dog, Animal))

print(issubclass(Dog, Animal))
