import msgpack

class Serializer:

    def __init__(self):
        pass

    def serialize(self, message:dict)->bytes:
        return msgpack.packb(message, use_bin_type=True)

    def deserialize(self, raw_message:bytes)->dict:
        return msgpack.unpackb(raw_message, raw=False)