from turtle import Turtle
ALIGNMENT = "center"
FONT = ("arial", 18, "normal")
class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        y = open("data.txt")
        z= y.read()
        y.close()
        self.score = 0
        self.high_score= int(z)
        self.penup()
        self.color("white")
        self.hideturtle()
        self.goto(0,270)
        self.board()

    def board(self):
        self.clear()
        self.write(f"SCORE: {self.score}  HIGH SCORE : {self.high_score}", align=ALIGNMENT,font=FONT)

    # def gameover(self):
    #     self.goto(0,0)
    #     self.write(" GAME OVER ", align=ALIGNMENT,font=FONT)

    def reset_game(self):
        if self.score > self.high_score:
            self.high_score = self.score
            with open("data.txt" ,mode="w") as data:
                data.write(f"{self.high_score}")
        self.score =0
        self.board()



    def increase_score(self):
        self.score += 1

        self.clear()
        self.board()