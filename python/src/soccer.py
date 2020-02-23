import sys
sys.path.insert(1, '../')
sys.path.insert(1, '../protoCompiled')

from src.refServer import Communication, set_functions
from src.utilities import ColorEnum, GameState, WorldModel, ROBOTS_NUM
from protoCompiled import common_pb2
from src.geom import Vector2D
from src.playon import PlayOn


class Soccer(PlayOn):
    def __init__(self):
        super().__init__()
        set_functions(self.Register, self.RunStrategy, self.SetBall, self.SetFormerRobots, self.SetLaterRobots)
        self.our_color = ColorEnum.Yellow
        self.game_state = GameState()
        self.wm = WorldModel()
        self.lastframe = common_pb2.Frame()
        for i in range(ROBOTS_NUM):
            tmp = self.lastframe.robots_yellow.add()
            tmp.robot_id = 0
            tmp.x = 0
            tmp.y = 0
            tmp.orientation = 0
            tmp1 = self.lastframe.robots_blue.add()
            tmp1.robot_id = 0
            tmp1.x = 0
            tmp1.y = 0
            tmp1.orientation = 0
        self.communication = Communication('127.0.0.1', 50052)

    def update_environment(self, frame, foul_info):
        self.game_state.update_gamestate(foul_info)
        self.wm.update_wm(frame, self.lastframe, self.our_color)
        self.lastframe = frame

    def Register(self, our_color):
        self.our_color = our_color
        print('team registration')
        return 'kian'

    def RunStrategy(self, frame, foul_info):
        self.update_environment(frame, foul_info)
        wheel_speeds = self.playon(self.wm)
        return wheel_speeds

    def SetBall(self, frame, foul_info):
        self.update_environment(frame, foul_info)
        ball_position = Vector2D(-0.9, 0)
        return ball_position

    def SetFormerRobots(self, frame, foul_info):
        self.update_environment(frame, foul_info)
        positions = []
        for i in range(ROBOTS_NUM):
            positions.append(Vector2D())
        positions[0] = Vector2D(-1, 0)
        positions[1] = Vector2D(-0.5, -0.5)
        positions[2] = Vector2D(-0.5, -0.1)
        positions[3] = Vector2D(-0.5, 0.1)
        positions[4] = Vector2D(-0.5, 0.5)
        return positions

    def SetLaterRobots(self, frame, foul_info):
        self.update_environment(frame, foul_info)
        positions = []
        for i in range(ROBOTS_NUM):
            positions.append(Vector2D())
        positions[0] = Vector2D(-1, 0)
        positions[1] = Vector2D(-0.5, -0.5)
        positions[2] = Vector2D(-0.5, -0.1)
        positions[3] = Vector2D(-0.5, 0.1)
        positions[4] = Vector2D(-0.5, 0.5)
        return positions


if __name__ == "__main__":
    soccer = Soccer()