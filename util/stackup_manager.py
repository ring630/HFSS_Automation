
class Layer:
    COLOR = None
    ALPHA = 0
    _PARAM_LIST = ["type", "layer", "thickness", "vertical_location"]

    def __init__(self, param):
        self.param = param
        self._validate()
        self.type = param["type"]
        self.layer = param["layer"]
        self.thickness = param["thickness"]
        self.vertical_location = param["vertical_location"]

    def _validate(self, ):
        for i in self._PARAM_LIST:
            if not i in self.param:
                raise ValueError("{} is not defined".format(i))



class CondLayer(Layer):
    def __init__(self, param):
        Layer.__init__(self, param)




def debug():
    param = {"type":"conductor",
             "layer":"1",
             "thickness":"0.05",
             "vertical_location":"0"}
    CondLayer(param)

if __name__=="__main__":
    debug()

