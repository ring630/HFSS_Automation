import pandas as pd

class Layer:
    _PARAM_LIST = ["usage", "layer", "thickness", "zloc", "material"]

    def __init__(self, param):
        self.param = param
        self._validate()

        self.usage = param["usage"]
        self.layer = param["layer"]
        self.thickness = param["thickness"]
        self.zloc = param["zloc"]
        self.material = param["material"]

    def _validate(self):
        for i in self._PARAM_LIST:
            if not i in self.param:
                raise ValueError("{} is not defined".format(i))


class ConductorLayer(Layer):
    def __init__(self, param):
        Layer.__init__(self, param)


class DielectricLayer(Layer):
    def __init__(self, param):
        Layer.__init__(self, param)


class Stackup:
    BOARD_THICKNESS = 0
    def __init__(self, fname):
        self.layers = {}
        self.layer_count = 0

        self.load_stackup(fname)

    def load_stackup(self, fname):
        df = pd.read_csv(fname)
        param = {}
        vloc = 0

        for r, val in df.iterrows():
            param["zloc"] = vloc
            param["usage"] = val["usage"]
            param["layer"] = val["layer"]
            param["thickness"] = val["thickness"]
            param["material"] = val["material"]
            print(param)
            self.layers[r] = Layer(param)
            vloc += val["thickness"]
            self.layer_count += 1
        self.layer_count = (self.layer_count + 1) // 2
        self.BOARD_THICKNESS = vloc


    def _check(self):
        for i, j in self.layers.items():
            print(i, j.usage, j.layer, j.thickness, j.zloc, j.material)

def debug():
    param = {"thickness":"0.05",
             "zloc":"0"}
    fname = "stackup.csv"
    debug = Stackup(fname)
    debug._check()



if __name__=="__main__":
    debug()

