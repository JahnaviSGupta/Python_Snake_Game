from turtle import Turtle
ALIGNMENT= "Center"
FONT = ("Copperplate Gothic Bold", 18 , "normal")
class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score=0
        self.high_score = 0
        self.hideturtle()
        self.penup()
        self.goto(0, 270)
        self.color("white")

    def reset_score(self):
        if self.score > self.high_score:
            self.high_score = self.score
        self.score = 0
        with open("highest_score.txt", mode="w") as file:
            file.write(f"{self.high_score}")
        self.show_score()
    # def game_over(self):
    #     self.goto(0,0)
    #     self.write(f"     Game Over. \n Your score is : {self.score}", move=False, align=ALIGNMENT, font=FONT)

    def show_score(self):
        self.clear()
        with open("highest_score.txt", mode="r") as file:
            high_score_from_file = file.read()

        self.write(f"Score: {self.score} Highscore: {high_score_from_file}",move=False, align=ALIGNMENT, font= FONT)

    def increase_score(self):
        self.clear()
        self.score+=1
        self.show_score()