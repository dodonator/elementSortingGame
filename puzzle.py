from string import ascii_uppercase
from collections import Counter
import random
import sys


class Puzzle:

    def __init__(self, element_type_num: int, container_size: int, spare_container: int) -> None:

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
        self.container: list[list] = []

        for i in range(self.container_num):
            self.container.append([])

    def fill_randomly(self):
        # fill the puzzle only if it is empty
        if hasattr(self, 'seed'):
            # ToDo: raise Exception
            return

        # setting up rng
        self.seed = random.randrange(sys.maxsize)
        rng = random.Random(self.seed)

        # set up a counter to count how many elements of the same type were already used
        element_counter: Counter = Counter(
            zip(self.element_types, [0]*self.element_type_num))

        for _ in range(self.element_type_num * self.container_size):

            # filter element types whose counters have reached the size limit
            available_types = list(filter(
                lambda e_type: element_counter[e_type] < self.container_size, self.element_types))

            # filter container which are already filled
            available_container_idx = list(
                filter(lambda con_idx: len(
                    self.container[con_idx]) < self.container_size, range(self.container_num)))

            # randomly choose a type of element
            e_type = rng.choice(available_types)

            # select a available container to add the element to
            container_idx = rng.choice(available_container_idx)

            # push the chosen element on top of the container
            selected_container = self.container[container_idx]
            selected_container.append(e_type)

            # update the counter for the chosen element type
            element_counter[e_type] += 1

    def move(self, source: int, target: int) -> str:
        assert source in range(self.container_num)
        assert target in range(self.container_num)

        # check if the target container still has space
        if len(self.container[target]) >= self.container_size:
            # target container is already full
            return

        # pull the first element from the source container
        element = self.container[source].pop()

        # push the element on the target container
        self.container[target].append(element)
        return element

    def print(self) -> None:
        for height in range(self.container_size-1, -1, -1):
            print(f'{height} |', end='')
            for container in self.container:
                try:
                    element = container[height]
                except IndexError:
                    element = ' '
                print(f'{element}|', end='')
            print()
        print(f'--|{"-|"*self.container_num}')
        print(f'  |{"|".join(map(str, range(self.container_num)))}|')


p = Puzzle(4, 4, 2)
p.fill_randomly()
p.print()