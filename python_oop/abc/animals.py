#!/usr/bin/env python3
"""Define an abstract Animal class and concrete subclasses."""
from abc import ABC, abstractmethod


class Animal(ABC):
    """Represent a generic animal with a required sound method."""

    @abstractmethod
    def sound(self):
        """Return the sound this animal makes."""


class Dog(Animal):
    """Represent a dog."""

    def sound(self):
        """Return the sound a dog makes."""
        return "Bark"


class Cat(Animal):
    """Represent a cat."""

    def sound(self):
        """Return the sound a cat makes."""
        return "Meow"
