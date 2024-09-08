from turtle import Turtle
file = open('data.txt')
high_score = file.read()
file.close()

class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.highscore = int(high_score)
        self.hideturtle()
        self.color('white')
        self.penup()
        self.goto(0, 270)
        self.show_score()
    def show_score(self):
        self.clear()
        self.write(f"Score : {self.score} High Score : {self.highscore}" , align="center", font=("Arial", 16, "normal"))

    def increase_score(self):
        self.score += 1
        self.show_score()


    # def game_over(self):
    #     self.goto(0,0)
    #     self.write("Game Over !", align='center', font=("Arial", 20, "normal"))

    def reset(self):
        if self.score > self.highscore:
            self.highscore = self.score
            file = open("data.txt","w")
            file.write(str(self.highscore))
            file.close()
        self.score = 0
        self.show_score()

