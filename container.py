from typing import Iterator, Optional


class Container:
    size_limit: int
    inventory: list
    current_index: int

    def __init__(self, size_limit: int):
        """Container constructor.

        Args:
            size_limit (int): max capacity of container
        """
        self.size_limit = size_limit
        self.inventory = []
        self.current_index = 0

    def __len__(self) -> int:
        """Returns the current capacity.

        Returns:
            int: current capacity
        """
        return len(self.inventory)

    def __iter__(self) -> Iterator[str]:
        """Iterates over the elements starting up top.

        Yields:
            Iterator[str]: element iterator
        """
        for element in reversed(self.inventory):
            yield element

    def __getitem__(self, index: int) -> Optional[str]:
        """Returns element at given index or None.

        Args:
            index (int): index

        Returns:
            Optional[str]: element or None
        """
        assert index in range(-self.size_limit, self.size_limit)
        try:
            element = self.inventory[index]
        except IndexError:
            element = None
        return element

    def add(self, element: str):
        """Adds an element on top of the container.

        Args:
            element (str): element to add
        """
        if not self.is_full():
            self.inventory.append(element)
            self.current_index += 1

    def pop(self) -> Optional[str]:
        """Pops an element from the container.

        Returns None if container is empty.

        Returns:
            Optional[str]: element or None
        """
        if not self.is_empty():
            element = self.inventory.pop()
            self.current_index -= 1
            return element
        else:
            return None

    def is_empty(self) -> bool:
        """Returns wether the container is empty.

        Returns:
            bool: result
        """
        return not bool(self.inventory)

    def is_full(self) -> bool:
        """Returns wether the maximum capacity is reached.

        Returns:
            bool: result
        """
        return len(self) == self.size_limit

    def is_finished(self) -> bool:
        """Returns  if the container is finished.

        The container is finished if it is full
        and all elements are of the same type.

        Returns:
            bool: result
        """
        if self.is_full():
            return len(set(self)) == 1
        else:
            return False

    def top(self) -> Optional[str]:
        """Returns the top element or None, if empty.

        Returns:
            Optional[str]: top element
        """
        if self.is_empty():
            return None
        return self[-1]

    def bottom(self) -> Optional[str]:
        """Returns the bottom element or None, if empty.

        Returns:
            Optional[str]: bottom element
        """
        if self.is_empty():
            return None
        return self[0]

    def _top_chain_length(self) -> int:  # name is WIP
        tcl = 0
        if self.is_empty():
            return tcl

        for element in reversed(self):
            if element == self.top():
                tcl += 1
            else:
                break
        return tcl

    def _bottom_chain_length(self) -> int:  # name is WIP
        bcl = 0
        if self.is_empty():
            return bcl

        for element in self.inventory:
            if element == self.bottom():
                bcl += 1
            else:
                break
        return bcl
