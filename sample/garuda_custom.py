from garuda_dir.garuda_pb2 import Void

class GarudaCustom(object):

    def CustomCallDemo(self, context, void):
        '''
        rpc CustomCallDemo(Void) returns (Void);
        '''
        print("Just a dummy RPC call")
        return Void()
