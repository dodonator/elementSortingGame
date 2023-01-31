from string import ascii_uppercase
from collections import Counter
import random
import sys
from container import Container
from typing import Iterator


class Puzzle:
    def __init__(
        self, element_type_num: int, container_size: int, spare_container: int
    ) -> None:

        self.element_type_num: int = element_type_num  # number of types of elements

        # generate the required number of elements
        self.element_types: list[str] = ascii_uppercase[:element_type_num]

        # set the size of a container
        self.container_size: int = container_size

        # set the number of extra containers
        self.spare_container: int = spare_container

        # calculate the total number of containers
        self.container_num: int = self.element_type_num + self.spare_container

        # creating an empty puzzle
        self.storage: list[Container] = []

        for i in range(self.container_num):
            con = Container(self.container_size)
            self.storage.append(con)

    def fill_randomly(self):
        # fill the puzzle only if it is empty
        if hasattr(self, "seed"):
            # ToDo: raise Exception
            return

        # setting up rng
        self.seed = random.randrange(sys.maxsize)
        rng = random.Random(self.seed)

        # set up a counter to count how many elements of the same type were already used
        element_counter: Counter = Counter(
            zip(self.element_types, [0] * self.element_type_num)
        )

        for _ in range(self.element_type_num * self.container_size):

            # filter element types whose counters have reached the size limit
            available_types = list(
                filter(
                    lambda e_type: element_counter[e_type] < self.container_size,
                    self.element_types,
                )
            )

            # filter container which are already filled
            available_container = list(
                filter(lambda con: not con.is_full(), self.storage)
            )

            # randomly choose a type of element
            e_type = rng.choice(available_types)

            # select a available container to add the element to
            selected_container = rng.choice(available_container)

            # push the chosen element on top of the container
            selected_container.add(e_type)

            # update the counter for the chosen element type
            element_counter[e_type] += 1

    def move(self, source: int, target: int) -> str:
        assert source in range(self.container_num)
        assert target in range(self.container_num)

        source_container: Container = self.storage[source]
        target_container: Container = self.storage[target]

        # check if the source container contains elements
        if source_container.is_empty():
            return

        # check if the target container still has space
        if target_container.is_full():
            return

        # pull the first element from the source container
        element = source_container.pop()

        # push the element on the target container
        target_container.add(element)

        # return the moved element
        return element

    def moveable(self) -> Iterator[tuple[int, int]]:
        for container_idx, container in enumerate(self.storage):
            yield container_idx, container.top()

    def is_finished(self) -> bool:
        for container in self.storage:
            if container.is_empty():
                continue
            elif container.is_finished():
                continue
            else:
                return False
        return True

    def print(self) -> None:
        for height in range(self.container_size - 1, -1, -1):
            print(f"{height} |", end="")
            for container in self.storage:
                element = container[height]
                if element is None:
                    element = " "
                print(f"{element}|", end="")
            print()
        print(f'--|{"-|"*self.container_num}')
        print(f'  |{"|".join(map(str, range(self.container_num)))}|')

    def __iter__(self) -> Iterator[Container]:
        for container in self.storage:
            yield container
