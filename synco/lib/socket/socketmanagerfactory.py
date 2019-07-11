import zmq
from synco.lib.socket.socketmanager import SocketManager
from synco.lib.socket.target import Target

class SocketManagerFactory:

    @staticmethod
    def create_server_socket()->SocketManager:
        context = zmq.Context()
        socket = context.socket(zmq.REP)
        #TODO: server configuration should be parsed out of the configuration files
        return SocketManager(socket)

    @staticmethod
    def create_client_socket(target: Target)->SocketManager:
        context = zmq.Context()
        socket = context.socket(zmq.REQ)
        socket.connect(target.get_target_for_zmq())
        return SocketManager(socket)
