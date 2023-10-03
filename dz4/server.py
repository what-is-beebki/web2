from concurrent import futures
import logging

import grpc
import echo_pb2
import echo_pb2_grpc

class EchoServiceServicer(echo_pb2_grpc.EchoServiceServicer):
    def PointEcho(self, request, context):
        response = echo_pb2.Vect2(val_x=request.val_x,
                                  val_y=request.val_y)
        return response
    def RotaryFieldEcho(self, request, context):
        direction_v = request.vector[request.direction]
        ret_field = echo_pb2.Vect2(val_x=request.point[0].val_y * direction_v.val_x,
                                   val_y=request.point[0].val_x * direction_v.val_y)
        response = echo_pb2.RotaryFieldResponce(point=[request.point[0]],
                                                field = [ret_field],
                                                direction = request.direction)
        return response
    
def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    echo_pb2_grpc.add_EchoServiceServicer_to_server(EchoServiceServicer(), server)
    server.add_insecure_port("[::]:50051")
    server.start()
    server.wait_for_termination()
    
if __name__ == '__main__':
    serve()
