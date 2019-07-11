from synco.lib.socket.socketmanagerfactory import SocketManagerFactory
from synco.lib.socket.target import Target

class Client:

    def __init__(self):
        pass

    def run(self):

        socket_manager = SocketManagerFactory.create_client_socket(Target.init("tcp://localhost:8000"))

        dict_obj = {
            'message': 'Hello World!',
            'meta': {
                'time': 'now',
                'id': 6,
                'code': 839021.8392
            }
        }

        socket_manager.send_message(dict_obj)

        response = socket_manager.recv_message()
        print(response)


        socket_manager.send_message(response)

        response_2 = socket_manager.recv_message()
        print(response_2)
'''
        context = zmq.Context()
        socket = context.socket(zmq.REQ)

        socket.connect("tcp://localhost:8000")

        dict_obj = {
            'message': 'Hello World!',
            'meta': {
                'time': 'now',
                'id': 6,
                'code': 839021.8392
            }
        }

        message = msgpack.packb(dict_obj, use_bin_type=True)
        socket.send(message)

        response = socket.recv()
        unpacked_response = msgpack.unpackb(response, raw=False)

        print(response)
        print(unpacked_response)

        socket.send(message)

        response = socket.recv()
        unpacked_response = msgpack.unpackb(response, raw=False)

        print(response)
        print(unpacked_response)
'''


if __name__ == '__main__':

    client = Client()
    client.run()


