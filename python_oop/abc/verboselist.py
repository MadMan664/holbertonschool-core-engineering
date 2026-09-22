#!/usr/bin/env python3
"""Define VerboseList, a list that announces its own mutations."""


class VerboseList(list):
    """Represent a list that prints a message on each mutation."""

    def append(self, item):
        """Add item to the list, then announce it.

        Args:
            item: the value to append.
        """
        super().append(item)
        print("Added [{}] to the list.".format(item))

    def extend(self, iterable):
        """Extend the list with iterable, then announce the count.

        Args:
            iterable: the values to add to the list.
        """
        items = list(iterable)
        super().extend(items)
        print("Extended the list with [{}] items.".format(len(items)))

    def remove(self, item):
        """Announce item, then remove it from the list.

        Args:
            item: the value to remove.
        """
        print("Removed [{}] from the list.".format(item))
        super().remove(item)

    def pop(self, index=-1):
        """Announce the item at index, then pop it from the list.

        Args:
            index (int): the position to pop. Defaults to the last
                item.
        """
        print("Popped [{}] from the list.".format(self[index]))
        return super().pop(index)
