from puzzle import Puzzle

# create random puzzle
puzzle = Puzzle(4, 4, 2)
puzzle.fill_randomly()

print("rules:")
print("The goal of the game is to sort the different elements")
print("into the containers based on their type.")
print("To do this, you take an element from the top of one container")
print("and put it on another container.")
print("You can only move one element at a time.")
print("The goal is reached when there is one container")
print("for each element type, in which all elements of this type are stacked.")

print("How to play:")
print("Input your movements in the format <source>-<target>")
print("Leave input blank to repeat last move")
print("Enter any character to undo the last move")
print("")

movement_counter = 0
last_move: tuple[int, int] = (-1, -1)
while True:
    puzzle.print()
    print()

    # check the win condition
    if puzzle.is_finished():
        break

    print(f"Your last move was {last_move}")

    cmd = input("source-target: ")
    match list(cmd):
        case []:
            # repeat last move
            source, target = last_move
        case [src, "-", tgt]:
            # do move
            source, target = int(src), int(tgt)
        case _:
            # undo last move
            target, source = last_move

    element = puzzle.move(source, target)
    if element is None:
        print("This move is not allowed.")
        continue

    movement_counter += 1
    last_move = source, target
    print("\n")

print()
print("you finished the puzzle")
print(f"it took you {movement_counter} moves")

puzzle.print()
