#!/usr/bin/env python3
import pika
import sys
import os
from time import sleep
from sequence_msg_pb2 import Sequence

def main():
    connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))
    channel = connection.channel()

    channel.queue_declare(queue='sequence_q')

    def callback(ch, method, properties, body):
        sleep(4)
        message = Sequence()
        message.ParseFromString(body)
        print("Sequence {}".format(message.numbers))

    channel.basic_consume(queue='sequence_q', on_message_callback=callback, auto_ack=True)

    print('Start consuming')
    channel.start_consuming()

if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        print('\nInterrupted')
        try:
            sys.exit(0)
        except SystemExit:
            os._exit(0)
