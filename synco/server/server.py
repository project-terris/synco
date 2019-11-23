import zmq
import msgpack

from synco.lib.socket.socketmanagerfactory import SocketManagerFactory
from synco.lib.socket.target import Target

class Server:

    def __init__(self):
        pass

    def run(self):
        socket_manager = SocketManagerFactory.create_server_socket()

        #context = zmq.Context()
        #socket = context.socket(zmq.REP)

        #socket.bind("tcp://*:8000")

        #message = socket.recv()
        unpacked_response = socket_manager.recv_message()

        response = dict()
        #parse action
        if unpacked_response["action"] == "GET":
            # parse message
            if unpacked_response["message"] == "RECORDS":
                # grab records from database

                # add records to dictionary response


        #unpacked_response = msgpack.unpackb(message, raw=False)
        #print(message)
        #print(unpacked_response)
        print(unpacked_response)

        #message = msgpack.packb(unpacked_response, use_bin_type=True)
        socket_manager.send_message(unpacked_response)

        #message = socket.recv()
        #unpacked_response = msgpack.unpackb(message, raw=False)
        #print(message)
        #print(unpacked_response)

        unpacked_response = socket_manager.recv_message()
        print(unpacked_response)
        socket_manager.send_message(unpacked_response)
        #message = msgpack.packb(unpacked_response, use_bin_type=True)
        #socket.send(message)


if __name__ == '__main__':

    server = Server()
    server.run()