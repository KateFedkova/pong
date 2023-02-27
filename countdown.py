class Countdown:

    """Class for a countdown"""

    def __init__(self):
        self.counter = 5
        self.text = '5'.rjust(3)
        self.start = False
        self.size = 70
        self.bold = False

    def show_num(self, counter):
        if counter > 0:
            self.text = str(counter).rjust(3)
            text_x = 350
            text_y = 200
        else:
            self.text = "start!"
            text_x = 333
            text_y = 200
            #self.start = True
        return text_x, text_y

