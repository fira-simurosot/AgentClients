import sys
sys.path.insert(1, './')
sys.path.insert(1, '../protoCompiled')

from protoCompiled.REF2CLI import service_pb2, service_pb2_grpc, messages_pb2
from protoCompiled import common_pb2
import grpc, time
from concurrent import futures
from src.utilities import ColorEnum


client_Register = None
client_RunStrategy = None
client_SetBall = None
client_SetFormerRobots = None
client_SetLaterRobots = None


def set_functions(client_Register_, client_RunStrategy_, client_SetBall_, client_SetFormerRobots_, client_SetLaterRobots_):
    global client_Register, client_RunStrategy, client_SetBall, client_SetFormerRobots, client_SetLaterRobots
    client_Register = client_Register_
    client_RunStrategy = client_RunStrategy_
    client_SetBall = client_SetBall_
    client_SetFormerRobots = client_SetFormerRobots_
    client_SetLaterRobots = client_SetLaterRobots_


class RefereeServicer(service_pb2_grpc.RefereeServicer):
    def Register(self, request, context):
        color = ColorEnum.Yellow if request.color == messages_pb2.Color.Y else ColorEnum.Blue
        team_name = client_Register(color)
        response = messages_pb2.TeamName()
        response.name = team_name
        return response

    def RunStrategy(self, request, context):
        # print('RunStrategy')
        command = messages_pb2.Command()
        for i in range(5):
            wheelspeed = command.wheels.add()
            wheelspeed.robot_id = i
            wheelspeed.right = 10
            wheelspeed.left = -10
        return command

    def SetBall(self, request, context):
        # print("SetBall")
        ball = common_pb2.Ball()
        ball.x = 0.5
        ball.y = 0.5
        ball.z = 0
        return ball

    def SetFormerRobots(self, request, context):
        # print("SetFormerRobots")
        robot = messages_pb2.Robots()
        for i in range(5):
            myrobot = robot.robots.add()
            myrobot.robot_id = i
            myrobot.x = 5+i
            myrobot.y = 5+i
            myrobot.orientation = 0
        return robot

    def SetLaterRobots(self, request, context):
        # print("SetLaterRobots")
        robot = messages_pb2.Robots()
        for i in range(5):
            myrobot = robot.robots.add()
            myrobot.robot_id = i
            myrobot.x = 5 + i
            myrobot.y = 5 + i
            myrobot.orientation = 0
        return robot



class Communication:
    def __init__(self, ip, port):
        self.ip = ip
        self.port = port

        server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
        service_pb2_grpc.add_RefereeServicer_to_server(RefereeServicer(),server)
        server.add_insecure_port(self.ip + ':' + str(self.port))
        server.start()
        while True:
            time.sleep(5000)


if __name__ == "__main__":
    def aa():
        print('aa')
    def bb():
        print('bb')
        return 'hh'
    def cc():
        print('cc')
    def dd():
        print('dd')
    def ee():
        print('ee')
    set_functions(aa, bb, cc, dd, ee)
    communication = Communication('127.0.0.1', 50052)