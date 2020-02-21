import sys
sys.path.insert(1, './')
sys.path.insert(1, '../protoCompiled')

from enum import Enum
from src.geom import Vector2D
from protoCompiled import common_pb2
from protoCompiled.REF2CLI import messages_pb2


ROBOTS_NUM = 5


class ColorEnum(Enum):
    Yellow = 1
    Blue = 2


class Robot:
    def __init__(self):
        self.id = -1
        self.pos = Vector2D()    #meter
        self.vel = Vector2D()    #meter per cycle
        self.ang = 0             #radian
        self.angVel = 0          #radian per cycle


class Ball:
    def __init__(self):
        self.pos = Vector2D()    #meter
        self.vel = Vector2D()    #meter per cycle


class WorldModel:
    def __init__(self):
        self.our = []
        self.opp = []
        for i in range(ROBOTS_NUM):
            self.our.append(Robot())
            self.opp.append(Robot())
        self.ball = Ball()

    def update_wm(self, frame, last_frame, our_color):
        self.ball.pos = Vector2D(frame.ball.x, frame.ball.y)
        self.ball.vel = Vector2D(frame.ball.x - last_frame.ball.x, frame.ball.y - last_frame.ball.x)

        for i in range(ROBOTS_NUM):
            self.our[i].id = frame.robots_yellow[i].robot_id
            self.our[i].pos = Vector2D(frame.robots_yellow[i].x, frame.robots_yellow[i].y)
            self.our[i].vel = Vector2D(frame.robots_yellow[i].x - lastframe.robots_yellow[i].x, frame.robots_yellow[i].y - last_frame.robots_yellow[i].y)
            self.our[i].ang = frame.robots_yellow[i].orientation
            self.our[i].angVel = frame.robots_yellow[i].orientation - last_frame.robots_yellow[i].orientation

            self.opp[i].id = frame.robots_blue[i].robot_id
            self.opp[i].pos = Vector2D(frame.robots_blue[i].x, frame.robots_blue[i].y)
            self.opp[i].vel = Vector2D(frame.robots_blue[i].x - last_frame.robots_blue[i].x,
                                       frame.robots_blue[i].y - last_frame.robots_blue[i].y)
            self.opp[i].ang = frame.robots_blue[i].orientation
            self.opp[i].angVel = frame.robots_blue[i].orientation - last_frame.robots_blue[i].orientation

        if our_color == ColorEnum.Blue:
            self.our, self.opp = self.opp, self.our

class GameStateEnum(Enum):
    PlayOn = 1
    OurPlaceKick = 2
    OurPenaltyKick = 3
    OurFreeKick = 4
    OurGoalKick = 5
    OurFreeBallLeftTop = 6
    OurFreeBallRightTop = 7
    OurFreeBallLeftBot = 8
    OurFreeBallRightBot = 9

    TheirPlaceKick = 2
    TheirPenaltyKick = 3
    TheirFreeKick = 4
    TheirGoalKick = 5
    TheirFreeBallLeftTop = 6
    TheirFreeBallRightTop = 7
    TheirFreeBallLeftBot = 8
    TheirFreeBallRightBot = 9


class GamePhaseEnum(Enum):
    FirstHalf = 1
    SecondHalf = 2
    PenaltyShootout = 3


class GameState:
    def __init__(self):
        self.state = GameStateEnum.PlayOn
        self.phase = GamePhaseEnum.FirstHalf

        self.dict_state_our = {
                        messages_pb2.FoulInfo.FoulType.PlayOn               :   GameStateEnum.PlayOn,
                        messages_pb2.FoulInfo.FoulType.PlaceKick            :   GameStateEnum.OurPlaceKick,
                        messages_pb2.FoulInfo.FoulType.PenaltyKick          :   GameStateEnum.OurPenaltyKick,
                        messages_pb2.FoulInfo.FoulType.FreeKick             :   GameStateEnum.OurFreeKick,
                        messages_pb2.FoulInfo.FoulType.GoalKick             :   GameStateEnum.OurGoalKick,
                        messages_pb2.FoulInfo.FoulType.FreeBallLeftTop      :   GameStateEnum.OurFreeBallLeftTop,
                        messages_pb2.FoulInfo.FoulType.FreeBallRightTop     :   GameStateEnum.OurFreeBallRightTop,
                        messages_pb2.FoulInfo.FoulType.FreeBallLeftBot      :   GameStateEnum.OurFreeBallLeftBot,
                        messages_pb2.FoulInfo.FoulType.FreeBallRightBot     :   GameStateEnum.OurFreeBallRightBot
                        }
        self.dict_state_their = {
                        messages_pb2.FoulInfo.FoulType.PlayOn               :   GameStateEnum.PlayOn,
                        messages_pb2.FoulInfo.FoulType.PlaceKick            :   GameStateEnum.TheirPlaceKick,
                        messages_pb2.FoulInfo.FoulType.PenaltyKick          :   GameStateEnum.TheirPenaltyKick,
                        messages_pb2.FoulInfo.FoulType.FreeKick             :   GameStateEnum.TheirFreeKick,
                        messages_pb2.FoulInfo.FoulType.GoalKick             :   GameStateEnum.TheirGoalKick,
                        messages_pb2.FoulInfo.FoulType.FreeBallLeftTop      :   GameStateEnum.TheirFreeBallLeftTop,
                        messages_pb2.FoulInfo.FoulType.FreeBallRightTop     :   GameStateEnum.TheirFreeBallRightTop,
                        messages_pb2.FoulInfo.FoulType.FreeBallLeftBot      :   GameStateEnum.TheirFreeBallLeftBot,
                        messages_pb2.FoulInfo.FoulType.FreeBallRightBot     :   GameStateEnum.TheirFreeBallRightBot
                        }
        self.dict_phase = {
                        messages_pb2.FoulInfo.PhaseType.FirstHalf           :   GamePhaseEnum.FirstHalf,
                        messages_pb2.FoulInfo.PhaseType.SecondHalf          :   GamePhaseEnum.SecondHalf,
                        messages_pb2.FoulInfo.PhaseType.PenaltyShootout     :   GamePhaseEnum.PenaltyShootout
                        }

    def update_gamestate(self, foul_info):
        dict_state = {}
        if foul_info.actor == messages_pb2.Side.Self:
            dict_state = self.dict_state_our
        else:
            dict_state = self.dict_state_their

            self.state = dict_state[foul_info.type]
            self.phase = self.dict_phase[foul_info.phase]


if __name__ == "__main__":
    wm = WorldModel()
    frame = common_pb2.Frame()
    lastframe = common_pb2.Frame()
    for i in range(ROBOTS_NUM):
        tmp = frame.robots_yellow.add()
        tmp.robot_id = i
        tmp.x = i
        tmp.y = i
        tmp.orientation = i
        tmp1 = frame.robots_blue.add()
        tmp1.robot_id = 10 - i
        tmp1.x = 10 - i
        tmp1.y = 10 - i
        tmp1.orientation = 10 - i
    lastframe = frame

    wm.update_wm(frame, lastframe, ColorEnum.Blue)
    print(wm.opp[2].pos)

