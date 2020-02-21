from src.refServer import Communication, set_functions
from src.utilities import ColorEnum

class Soccer:
    def __init__(self):
        set_functions(self.Register, self.RunStrategy, self.SetBall, self.SetFormerRobots, self.SetLaterRobots)
        self.communication = Communication('127.0.0.1', 50052)
        self.our_color = ColorEnum.Yellow

    def Register(self, our_color):
        self.our_color = our_color
        print('team registration')
        return 'kian'

    def RunStrategy(self):
        pass

    def SetBall(self):
        pass

    def SetFormerRobots(self):
        pass

    def SetLaterRobots(self):
        pass


if __name__ == "__main__":
    soccer = Soccer()