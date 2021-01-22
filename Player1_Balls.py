class Player1Balls:     # used to make and move balls for player1

    def __init__(self, canvas, x, y, diameter, x_velocity, y_velocity, color):
        self.canvas = canvas
        self.x0 = x - diameter
        self.y0 = y - diameter
        self.x1 = x + diameter
        self.y1 = y + diameter
        self.image = canvas.create_oval(self.x0, self.y0, self.x1, self.y1,fill=color)  # create_oval takes x and y position and width and height in this case its a circles so width and height are equal thus the use of diameter twice
        self.x_velocity = x_velocity
        self.y_velocity = y_velocity

    def movePlayer1(self):
        coordinates = self.canvas.coords(self.image)

        self.canvas.move(self.image, self.x_velocity, self.y_velocity)
