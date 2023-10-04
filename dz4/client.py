import logging

import grpc
import echo_pb2
import echo_pb2_grpc

channel = grpc.insecure_channel('localhost:50051')
stub = echo_pb2_grpc.EchoServiceStub(channel)

request1 = echo_pb2.Vect2(val_x = 3.0,
                         val_y = 4.0)
responce1 = stub.PointEcho(request1)
print('Point {', request1, '} is at {', responce1, '}')

request2 = echo_pb2.RotaryFieldRequest(point = request1,
                                       direction = 'clockwise',
                                       vector = {'clockwise': echo_pb2.Vect2(val_x = 1, val_y = -1),
                                                 'counterclockwise': echo_pb2.Vect2(val_x = -1, val_y = 1)})
responce2 = stub.RotaryFieldEcho(request2)
print('Field at point {', request2, '} is {', responce2, '}')


request3 = echo_pb2.Sequence(numbers = [8888, 8080, 1])
responce3 = stub.SequenceEcho(request3)
print('Sequence {', request3, '} is {', responce3, '}')
