import pika
from sequence_msg_pb2 import Sequence

connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = connection.channel()
channel.queue_declare(queue='sequence_q')

message = Sequence(numbers = [2, 10, 63])
message_s = message.SerializeToString()

print("Sending sequence\n{}".format(message))
channel.basic_publish(exchange='', routing_key='sequence_q', body=message_s)
connection.close()
