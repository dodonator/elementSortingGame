class Container:
    size_limit: int
    inventory: list

    def __init__(self, size_limit: int):
        self.size_limit = size_limit
        self.inventory = []

    def __len__(self) -> int:
        return len(self.inventory)

    def add(self, element):
        if len(self) < self.size_limit:
            self.inventory.append(element)

    def pop(self, element):
        if len(self) > 0:
            element = self.inventory.pop()
            return element

    def is_empty(self) -> bool:
        return len(self)
