import subprocess
subprocess.call("./protoCompiler.bash", shell=True)
#
# import grpc
# from concurrent import futures
# import time
# from messages.REF2CLI import service_pb2
# from messages.REF2CLI import service_pb2_grpc
# from messages.REF2CLI import messages_pb2
# from messages import common_pb2
#
#
#
#
#
#
# class RefereeServicer(service_pb2_grpc.RefereeServicer):
#
#     def Register(self, request, context):
#         print("Register")
#         response = messages_pb2.TeamName()
#         response.name = "parsian"
#         print('salam')
#         return response
#
#     def RunStrategy(self, request, context):
#         print('RunStrategy')
#         command = messages_pb2.Command()
#         for i in range(5):
#             wheelspeed = command.wheels.add()
#             wheelspeed.robot_id = i
#             wheelspeed.right = 0
#             wheelspeed.left = 0
#         return command
#
#     def SetBall(self, request, context):
#         print("SetBall")
#         ball = common_pb2.Ball()
#         ball.x = 0.5
#         ball.y = 0.5
#         ball.z = 0
#         return ball
#
#     def SetFormerRobots(self, request, context):
#         print("SetFormerRobots")
#         robot = messages_pb2.Robots()
#         for i in range(5):
#             myrobot = robot.robots.add()
#             myrobot.robot_id = i
#             myrobot.x = 5+i
#             myrobot.y = 5+i
#             myrobot.orientation = 0
#         return robot
#
#     def SetLaterRobots(self, request, context):
#         print("SetLaterRobots")
#         robot = messages_pb2.Robots()
#         for i in range(5):
#             myrobot = robot.robots.add()
#             myrobot.robot_id = i
#             myrobot.x = 5 + i
#             myrobot.y = 5 + i
#             myrobot.orientation = 0
#         return robot
#
#
#
#
#
#
# server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
# service_pb2_grpc.add_RefereeServicer_to_server(RefereeServicer(),server)
# server.add_insecure_port('127.0.0.1:50053')
# server.start()
#
# while True:
#     time.sleep(85000)
