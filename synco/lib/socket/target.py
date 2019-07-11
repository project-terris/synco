

class Target:

    raw_target = None

    def get_target_for_zmq(self)->str:
        return self.raw_target

    @staticmethod
    def init(raw_target:str):
        instance = Target()
        instance.raw_target = raw_target
        return instance
