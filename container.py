from typing import Iterator


class Container:
    size_limit: int
    inventory: list

    def __init__(self, size_limit: int):
        self.size_limit = size_limit
        self.inventory = []

    def __len__(self) -> int:
        return len(self.inventory)

    def __iter__(self) -> Iterator:
        for element in reversed(self.inventory):
            yield element

    def __getitem__(self, index: int):
        assert index in range(-self.size_limit, self.size_limit)
        try:
            element = self.inventory[index]
        except IndexError:
            element = None
        return element

    def add(self, element):
        if not self.is_full():
            self.inventory.append(element)

    def pop(self):
        if len(self) > 0:
            element = self.inventory.pop()
            return element

    def is_empty(self) -> bool:
        return not bool(self.inventory)

    def is_full(self) -> bool:
        return len(self) == self.size_limit

    def is_finished(self) -> bool:
        if self.is_full():
            return len(set(self)) == 1
        else:
            return False

    def _top_chain_length(self) -> int:  # name is WIP
        tcl = 0
        if self.is_empty():
            return tcl

        top_element = self[-1]
        for element in reversed(self):
            if element == top_element:
                tcl += 1
            else:
                break
        return tcl

    def _bottom_chain_length(self) -> int:  # name is WIP
        bcl = 0
        if self.is_empty():
            return bcl

        bottom_element = self[0]
        for element in self.inventory:
            if element == bottom_element:
                bcl += 1
            else:
                break
        return bcl
