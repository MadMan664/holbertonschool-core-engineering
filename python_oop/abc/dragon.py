#!/usr/bin/env python3
"""Define SwimMixin, FlyMixin, and a Dragon composed from both."""


class SwimMixin:
    """Provide swimming behavior."""

    def swim(self):
        """Print that the creature swims."""
        print("The creature swims!")


class FlyMixin:
    """Provide flying behavior."""

    def fly(self):
        """Print that the creature flies."""
        print("The creature flies!")


class Dragon(SwimMixin, FlyMixin):
    """Represent a dragon that can swim, fly, and roar."""

    def roar(self):
        """Print that the dragon roars."""
        print("The dragon roars!")
