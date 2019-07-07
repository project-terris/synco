import zmq
import msgpack

class Server:

    def __init__(self):
        pass

    def run(self):
        context = zmq.Context()
        socket = context.socket(zmq.SERVER)

        socket.bind("tcp://*:8000")

        message = socket.recv()
        unpacked_response = msgpack.unpackb(message, raw=False)
        print(message)
        print(unpacked_response)

        message = msgpack.packb(unpacked_response, use_bin_type=True)
        socket.send(message)

        message = socket.recv()
        unpacked_response = msgpack.unpackb(message, raw=False)
        print(message)
        print(unpacked_response)

        message = msgpack.packb(unpacked_response, use_bin_type=True)
        socket.send(message)


if __name__ == '__main__':

    server = Server()
    server.run()