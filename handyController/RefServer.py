import subprocess
subprocess.call("./protoCompiler.bash", shell=True)
import sys
sys.path.insert(1, './messages')

import grpc
import time
from concurrent import futures
import handyWidget
from handyWidget import wheelspeedsLeft, wheelspeedsRight
from REF2CLI import service_pb2_grpc
from REF2CLI import messages_pb2
import common_pb2
from PyQt5.QtWidgets import (QWidget, QGridLayout,QPushButton, QApplication, QLabel, QComboBox)


class RefereeServicer(service_pb2_grpc.RefereeServicer):

    def Register(self, request, context):
        print("Register")
        response = messages_pb2.TeamName()
        response.name = "parsian"
        return response

    def RunStrategy(self, request, context):
        # print('RunStrategy')
        command = messages_pb2.Command()
        for i in range(5):
            wheelspeed = command.wheels.add()
            wheelspeed.robot_id = i
            wheelspeed.right = wheelspeedsRight[i]
            wheelspeed.left = wheelspeedsLeft[i]
        return command

    def SetBall(self, request, context):
        print("SetBall")
        ball = common_pb2.Ball()
        ball.x = 0.5
        ball.y = 0.5
        ball.z = 0
        return ball

    def SetFormerRobots(self, request, context):
        print("SetFormerRobots")
        robot = messages_pb2.Robots()
        for i in range(5):
            myrobot = robot.robots.add()
            myrobot.robot_id = i
            myrobot.x = 5+i
            myrobot.y = 5+i
            myrobot.orientation = 0
        return robot

    def SetLaterRobots(self, request, context):
        print("SetLaterRobots")
        robot = messages_pb2.Robots()
        for i in range(5):
            myrobot = robot.robots.add()
            myrobot.robot_id = i
            myrobot.x = 5 + i
            myrobot.y = 5 + i
            myrobot.orientation = 0
        return robot



print('Handy controller is running')
server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
service_pb2_grpc.add_RefereeServicer_to_server(RefereeServicer(),server)
server.add_insecure_port('127.0.0.1:50052')
server.start()


def color_changed(index):
    port = '50052'
    if index == 1:
        port = '50053'
    global server
    server.stop(0)
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    service_pb2_grpc.add_RefereeServicer_to_server(RefereeServicer(), server)
    server.add_insecure_port('127.0.0.1:'+ port)
    server.start()


# while True:
#     time.sleep(5000)
app = QApplication(sys.argv)
myWidget = handyWidget.HandyWidget()
myWidget.combocolor.currentIndexChanged.connect(color_changed)
sys.exit(app.exec_())

