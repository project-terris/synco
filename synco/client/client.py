import zmq
import msgpack

class Client:


    def __init__(self):
        pass

    def run(self):

        context = zmq.Context()
        socket = context.socket(zmq.CLIENT)

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

if __name__ == '__main__':

    client = Client()
    client.run()


