class Scores:

    score_1 = 0
    score_2 = 0

    def update_score_1(self):
        self.score_1 += 1

    def update_score_2(self):
        self.score_2 += 1

    def game_over(self):
        if self.score_1 == 11 or self.score_2 == 11:
            return f"{sth}"