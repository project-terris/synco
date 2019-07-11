from synco.lib.socket.serializer import Serializer
from synco.lib.socket.cryptor import Cryptor

class SocketManager:

    serializer = Serializer()
    cryptor = Cryptor()
    socket = None

    def __init__(self, socket):
        self.socket = socket
        pass

    def send_message(self, message:dict)->int:
        raw_message = self.serializer.serialize(message)
        encrypted_message = self.cryptor.encrypt(raw_message)
        return self.socket.send(encrypted_message)


    def recv_message(self)->dict:
        encrypted_message = self.socket.recv()
        raw_message = self.cryptor.decrypt(encrypted_message)
        message = self.serializer.deserialize(raw_message)
        return message
