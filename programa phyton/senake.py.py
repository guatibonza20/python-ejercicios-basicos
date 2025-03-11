import tkinter as tk
import random

class SnakeGame:
    def __init__(self, master):
        self.master = master
        self.master.title("Snake Game")
        self.canvas = tk.Canvas(master, width=400, height=400, bg="black")
        self.canvas.pack()
        self.snake = [(20, 20)]
        self.food = self.spawn_food()
        self.direction = "Right"
        self.score = 0
        self.draw()

        self.master.bind("w", lambda event: self.change_direction("Up"))
        self.master.bind("a", lambda event: self.change_direction("Left"))
        self.master.bind("s", lambda event: self.change_direction("Down"))
        self.master.bind("d", lambda event: self.change_direction("Right"))
        self.move_snake()

    def draw(self):
        self.canvas.delete("all")
        for segment in self.snake:
            self.canvas.create_rectangle(segment[0], segment[1], segment[0] + 20, segment[1] + 20, fill="green")
        self.canvas.create_oval(self.food[0], self.food[1], self.food[0] + 20, self.food[1] + 20, fill="red")
        self.canvas.create_text(50, 10, text=f"Score: {self.score}", fill="white", anchor="nw")
        self.master.update_idletasks()

    def move_snake(self):
        head = self.snake[0]
        if self.direction == "Right":
            new_head = (head[0] + 20, head[1])
        elif self.direction == "Left":
            new_head = (head[0] - 20, head[1])
        elif self.direction == "Up":
            new_head = (head[0], head[1] - 20)
        elif self.direction == "Down":
            new_head = (head[0], head[1] + 20)

        if new_head == self.food:
            self.score += 1
            self.snake.append(self.snake[-1])
            self.food = self.spawn_food()
        else:
            self.snake.pop()
            self.snake.insert(0, new_head)

        if (new_head in self.snake[1:] or
                new_head[0] < 0 or new_head[0] >= 400 or
                new_head[1] < 0 or new_head[1] >= 400):
            self.canvas.create_text(200, 200, text="Game Over!", fill="white", font=("Arial", 30))
            return

        self.draw()
        self.master.after(100, self.move_snake)

    def spawn_food(self):
        x = random.randrange(0, 400, 20)
        y = random.randrange(0, 400, 20)
        return x, y

    def change_direction(self, new_direction):
        opposite_directions = {"Up": "Down", "Down": "Up", "Left": "Right", "Right": "Left"}
        if new_direction != opposite_directions.get(self.direction):
            self.direction = new_direction

root = tk.Tk()
game = SnakeGame(root)
root.mainloop()