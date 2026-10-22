
from collections import deque

class SnakeAndLadder:
    def __init__(self, size=100):
        self.size = size
        self.snakes = {99: 54, 70: 55, 52: 42, 25: 2, 95: 72}
        self.ladders = {6: 25, 11: 40, 60: 85, 46: 90, 17: 69}

    def add_snake(self, start, end):
        if 1 < end < start <= self.size:
            if start not in self.ladders:
                self.snakes[start] = end
                print("Snake added successfully.")
            else:
                print("A ladder already starts at this position.")
        else:
            print("Invalid snake positions.")

    def add_ladder(self, start, end):
        if 1 <= start < end <= self.size:
            if start not in self.snakes:
                self.ladders[start] = end
                print("Ladder added successfully.")
            else:
                print("A snake already starts at this position.")
        else:
            print("Invalid ladder positions.")

    def find_shortest_path(self):
        queue = deque([1])
        visited = [False] * (self.size + 1)
        parent = [-1] * (self.size + 1)
        distance = [0] * (self.size + 1)
        visited[1] = True

        while queue:
            position = queue.popleft()

            if position == self.size:
                break

            for dice in range(1, 7):
                next_position = position + dice

                if next_position > self.size:
                    continue

                if next_position in self.snakes:
                    next_position = self.snakes[next_position]
                elif next_position in self.ladders:
                    next_position = self.ladders[next_position]

                if not visited[next_position]:
                    visited[next_position] = True
                    parent[next_position] = position
                    distance[next_position] = distance[position] + 1
                    queue.append(next_position)

        if not visited[self.size]:
            print("Destination cannot be reached.")
            return

        path = []
        current = self.size

        while current != -1:
            path.append(current)
            if current == 1:
                break
            current = parent[current]

        path.reverse()

        print("\n----- BFS RESULT -----")
        print("Starting Position: 1")
        print("Destination Position:", self.size)
        print("Shortest Path:", " -> ".join(map(str, path)))
        print("Minimum Dice Throws:", distance[self.size])

    def display_board(self):
        print("\nBoard Size:", self.size)
        print("Snakes:", self.snakes)
        print("Ladders:", self.ladders)


game = SnakeAndLadder()

while True:
    print("\n===== SNAKE AND LADDER USING BFS =====")
    print("1. Add Snake")
    print("2. Add Ladder")
    print("3. Find Shortest Path")
    print("4. Display Board")
    print("5. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        try:
            start = int(input("Enter snake head position: "))
            end = int(input("Enter snake tail position: "))
            game.add_snake(start, end)
        except ValueError:
            print("Please enter valid numbers.")

    elif choice == "2":
        try:
            start = int(input("Enter ladder bottom position: "))
            end = int(input("Enter ladder top position: "))
            game.add_ladder(start, end)
        except ValueError:
            print("Please enter valid numbers.")

    elif choice == "3":
        game.find_shortest_path()

    elif choice == "4":
        game.display_board()

    elif choice == "5":
        print("Thank you for using Snake and Ladder BFS!")
        break

    else:
        print("Invalid choice. Please try again.")